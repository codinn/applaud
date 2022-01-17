from enum import Enum, auto
from typing import Any, Union, Optional, TypeVar
import requests
from ..schemas.responses import ApplaudResponse, ErrorResponse
from ..schemas.requests import ApplaudRequest
import functools

class SortOrder(Enum):
    ASC = auto()
    DESC = auto()

ENDPOINT_BASE_URL = 'https://api.appstoreconnect.apple.com'

def endpoint(path: str):
    '''Mark a function as an endpoint'''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        return wrapper

    return decorator

class EndpointException(Exception):
    """ Base exception for endpoint. """

    response: requests.Response
    request: Optional[requests.Request]
    errors: list[ErrorResponse.Error]
    
    def __init__(self, errors: list[ErrorResponse.Error], response: requests.Response):
        self.response = response
        self.request = response.request
        self.errors = errors

        repr_errors = [repr(error) for error in self.errors]
        error_msg = ',\n'.join(repr_errors)

        super(EndpointException, self).__init__(error_msg)

class Endpoint:
    path: str

    def __init__(self, session: requests.Session):
        self.session = session
        self.endpoint_path = ENDPOINT_BASE_URL + self.path
        self._query_params = {}

    def _set_includes(self, includes: list[Enum]):
        values = [r.value for r in includes]
        self._query_params['include'] = ','.join(values)

    def _set_limit(self, limit: int, related: Optional[str]=None):
        if related:
            self._query_params[f'limit[{related}]'] = limit
        else:
            self._query_params['limit'] = limit

    def _set_fields(self, key: str, value: list[Enum]):
        items = [item.value for item in value]
        self._query_params[f'fields[{key}]'] = ','.join(items)

    def _set_filter(self, key: str, value: list[Union[Enum, str]]):
        items = [item.value if type(item) is Enum else item for item in value]
        self._query_params[f'filter[{key}]'] = ','.join(items)

    def _set_exists(self, key: str, value: str):
        self._query_params[f'exists[{key}]'] = value

    def _set_sort(self, expressions: list[str]):
        self._query_params['sort'] = ','.join(expressions)

    def __parse_response(self, response: requests.Response) -> Any:
        try:
            json = response.json()
            if response.ok:
                return json
            
            errors: list[ErrorResponse.Error] = ErrorResponse.parse_obj(json).errors if json else None

            if errors:
                # Errors from the App Store Connect service
                raise EndpointException(errors, response)

            response.raise_for_status()
        except requests.exceptions.JSONDecodeError as error:
            # Response body does not contain valid json.
            return None

    def _perform_get(self) -> Any:
        '''Perform a GET request to the specified endpoint.'''
        response = self.session.get(self.endpoint_path, params=self._query_params, headers={})
        return self.__parse_response(response)

    def _perform_post(self, request: Union[ApplaudRequest, dict, None]=None) -> Any:
        '''Perform a POST request to the specified endpoint.'''
        request_json = request.request_dict() if isinstance(request, ApplaudRequest) else request
        response = self.session.post(self.endpoint_path, json=request_json, headers={})
        return self.__parse_response(response)

    def _perform_patch(self, request: Union[ApplaudRequest, dict, None]=None) -> Any:
        '''Perform a PATCH request to the specified endpoint.'''
        request_json = request.request_dict() if isinstance(request, ApplaudRequest) else request
        response = self.session.patch(self.endpoint_path, json=request_json, headers={})
        return self.__parse_response(response)

    def _perform_delete(self, request: Union[ApplaudRequest, dict, None]=None):
        '''Perform a DELETE request to the specified endpoint.'''
        request_json = request.request_dict() if isinstance(request, ApplaudRequest) else request
        response = self.session.delete(self.endpoint_path, json=request_json, headers={})
        self.__parse_response(response)

class IDEndpoint(Endpoint):
    
    def __init__(self, id: str, session: requests.Session):
        self.id = id
        self.path = self.path.format(id=self.id)
        super().__init__(session)

class GenericEndpoint(Endpoint):

    RESPONSE = TypeVar("RESPONSE", bound=Optional[ApplaudResponse])

    def __init__(self, session: requests.Session, url: str):
        self.path = url.removeprefix(ENDPOINT_BASE_URL)
        super().__init__(session)
        self.endpoint_path = url

    def get(self, *, response_class: type[RESPONSE]) -> RESPONSE:
        '''Get one or more resources.'''
        response_json = self._perform_get()
        return response_class.parse_obj(response_json)

    def create(self, request: Union[ApplaudRequest, dict], *, response_class: type[RESPONSE]=type(None)) -> RESPONSE:
        '''Create one or more resources.'''
        response_json = self._perform_post(request)
        return response_class.parse_obj(response_json) if response_class else None

    def update(self, request: Union[ApplaudRequest, dict], *, response_class: type[RESPONSE]=type(None)) -> RESPONSE:
        '''Modify one or more resources.'''
        response_json = self._perform_patch(request)
        return response_class.parse_obj(response_json) if response_class else None

    def delete(self, request: Union[ApplaudRequest, dict, None]=None):
        '''Delete one or more resources.'''
        self._perform_delete(request)
