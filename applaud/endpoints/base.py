from enum import Enum, auto
from typing import Any, Union, Optional
import requests
from ..schemas.responses import ErrorResponse

class SortOrder(Enum):
    ASC = auto()
    DESC = auto()

ENDPOINT_BASE_URL = 'https://api.appstoreconnect.apple.com'

class EndpointException(Exception):
    """ Base exception for endpoint. """

    response: requests.Response
    request: Optional[requests.Request]
    errors: Optional[list[ErrorResponse.Error]]
    
    def __init__(self, response: requests.Response):
        self.response = response
        self.request = response.request
        self.errors = ErrorResponse.parse_obj(response.json()).errors

        if self.errors == None or len(self.errors) == 0:
            # Code is from python-requests package
            if 400 <= response.status_code < 500:
                error_msg = u'%s Client Error: %s for url: %s' % (response.status_code, response.reason, response.url)
            elif 500 <= response.status_code < 600:
                error_msg = u'%s Server Error: %s for url: %s' % (response.status_code, response.reason, response.url)
        else:
            repr_errors = [repr(error) for error in self.errors]
            error_msg = ',\n'.join(repr_errors)

        super(EndpointException, self).__init__(error_msg)

class Endpoint:
    path: str

    def __init__(self, session: requests.Session):
        self.session = session
        self.endpoint_path = ENDPOINT_BASE_URL + self.path
        self.__query_params = {}

    def _set_includes(self, includes: list[Enum]):
        values = [r.value for r in includes]
        self.__query_params['include'] = ','.join(values)

    def _set_limit(self, key: str, limit: int):
        self.__query_params[f'limit[{key}]'] = limit

    def _set_fields(self, key: str, value: list[Enum]):
        items = [item.value for item in value]
        self.__query_params[f'fields[{key}]'] = ','.join(items)

    def _set_filter(self, key: str, value: list[Union[Enum, str]]):
        items = [item.value if type(item) is Enum else item for item in value]
        self.__query_params[f'filter[{key}]'] = ','.join(items)

    def _set_exists(self, key: str, value: str):
        self.__query_params[f'exists[{key}]'] = value

    def _set_sort(self, expressions: list[str]):
        self.__query_params['sort'] = ','.join(expressions)

    def _perform_get(self) -> Any:
        '''Perform a GET request to the specified endpoint.'''
        response = self.session.get(self.endpoint_path, params=self.__query_params, headers={})

        if response.status_code == 200:
            # 200 is the only success code for a GET request
            return response.json()
        elif response.status_code == [400, 403, 404, 409]:
            # Those are the error codes that we can expect to get from the API
            raise EndpointException(response)
        else:
            response.raise_for_status()

    def _perform_post(self, json: dict) -> Any:
        '''Perform a POST request to the specified endpoint.'''
        response = self.session.post(self.endpoint_path, json=json, headers={})

        if response.status_code == 201 or response.status_code == 204:
            # 201 and 204 are the success codes for a POST request
            return response.json()
        elif response.status_code in [400, 403, 404, 409]:
            # Those are the error codes that we can expect to get from the API
            raise EndpointException(response)
        else:
            response.raise_for_status()

    def _perform_patch(self, json: dict) -> Any:
        '''Perform a PATCH request to the specified endpoint.'''
        response = self.session.patch(self.endpoint_path, json=json, headers={})

        if response.status_code == 200 or response.status_code == 204:
            # 200 and 204 are the success codes for a PATCH request
            return response.json()
        elif response.status_code in [400, 403, 404, 409]:
            # Those are the error codes that we can expect to get from the API
            raise EndpointException(response)
        else:
            response.raise_for_status()

    def _perform_delete(self, json: Optional[dict] = None):
        '''Perform a DELETE request to the specified endpoint.'''
        response = self.session.delete(self.endpoint_path, json=json, headers={})

        if response.status_code == 204:
            #  204 is the success code for a DELETE request
            return
        elif response.status_code in [400, 403, 404, 409]:
            # Those are the error codes that we can expect to get from the API
            raise EndpointException(response)
        else:
            response.raise_for_status()

class IDEndpoint(Endpoint):
    
    def __init__(self, id: str, connection):
        self.id = id
        self.path = self.path.format(id=self.id)
        super().__init__(connection)
