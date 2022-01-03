from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class UserListEndpoint(Endpoint):
    path = '/v1/users'

    def fields(self, *, user: Union[UserField, list[UserField]]=None, app: Union[AppField, list[AppField]]=None) -> UserListEndpoint:
        '''Fields to return for included related types.

        :param user: the fields to include for returned resources of type users
        :type user: Union[UserField, list[UserField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.UserListEndpoint
        '''
        if user: self._set_fields('users',user if type(user) is list else [user])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        VISIBLE_APPS = 'visibleApps'

    def filter(self, *, roles: Union[UserRole, list[UserRole]]=None, username: Union[str, list[str]]=None, visible_apps: Union[str, list[str]]=None) -> UserListEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param roles: filter by attribute 'roles'
        :type roles: Union[UserRole, list[UserRole]] = None

        :param username: filter by attribute 'username'
        :type username: Union[str, list[str]] = None

        :param visible_apps: filter by id(s) of related 'visibleApps'
        :type visible_apps: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.UserListEndpoint
        '''
        if roles: self._set_filter('roles', roles if type(roles) is list else [roles])
        
        if username: self._set_filter('username', username if type(username) is list else [username])
        
        if visible_apps: self._set_filter('visibleApps', visible_apps if type(visible_apps) is list else [visible_apps])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> UserListEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.UserListEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, last_name: SortOrder=None, username: SortOrder=None) -> UserListEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.UserListEndpoint
        '''
        if last_name: self.sort_expressions.append('lastName' if last_name == SortOrder.ASC else '-lastName')
        if username: self.sort_expressions.append('username' if username == SortOrder.ASC else '-username')
        return self
        
    def limit(self, number: int=None, *, visible_apps: int=None) -> UserListEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param visible_apps: maximum number of related visibleApps returned (when they are included). The maximum limit is 50
        :type visible_apps: int = None

        :returns: self
        :rtype: applaud.endpoints.UserListEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if visible_apps and visible_apps > 50:
            raise ValueError(f'The maximum limit is 50')
        if visible_apps: self._set_limit('visibleApps', visible_apps)

        return self

    def get(self) -> UsersResponse:
        '''Get one or more resources.

        :returns: List of Users
        :rtype: UsersResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return UsersResponse.parse_obj(json)

class UserEndpoint(IDEndpoint):
    path = '/v1/users/{id}'

    def fields(self, *, user: Union[UserField, list[UserField]]=None, app: Union[AppField, list[AppField]]=None) -> UserEndpoint:
        '''Fields to return for included related types.

        :param user: the fields to include for returned resources of type users
        :type user: Union[UserField, list[UserField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.UserEndpoint
        '''
        if user: self._set_fields('users',user if type(user) is list else [user])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        VISIBLE_APPS = 'visibleApps'

    def include(self, relationship: Union[Include, list[Include]]) -> UserEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.UserEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, visible_apps: int=None) -> UserEndpoint:
        '''Number of included related resources to return.

        :param visible_apps: maximum number of related visibleApps returned (when they are included). The maximum limit is 50
        :type visible_apps: int = None

        :returns: self
        :rtype: applaud.endpoints.UserEndpoint
        '''
        if visible_apps and visible_apps > 50:
            raise ValueError(f'The maximum limit is 50')
        if visible_apps: self._set_limit('visibleApps', visible_apps)

        return self

    def get(self) -> UserResponse:
        '''Get the resource.

        :returns: Single User
        :rtype: UserResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return UserResponse.parse_obj(json)

    def update(self, request: UserUpdateRequest) -> UserResponse:
        '''Modify the resource.

        :param request: User representation
        :type request: UserUpdateRequest

        :returns: Single User
        :rtype: UserResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_patch(json)
        return UserResponse.parse_obj(response_json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class VisibleAppListOfUserRelationshipsEndpoint(IDEndpoint):
    path = '/v1/users/{id}/relationships/visibleApps'

    def limit(self, number: int=None) -> VisibleAppListOfUserRelationshipsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VisibleAppListOfUserRelationshipsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> UserVisibleAppsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: UserVisibleAppsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return UserVisibleAppsLinkagesResponse.parse_obj(json)

    def create(self, request: UserVisibleAppsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: UserVisibleAppsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        super()._perform_post(json)

    def update(self, request: UserVisibleAppsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: UserVisibleAppsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        super()._perform_patch(json)

    def delete(self, request: UserVisibleAppsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: UserVisibleAppsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        super()._perform_delete(json)

class VisibleAppListOfUserEndpoint(IDEndpoint):
    path = '/v1/users/{id}/visibleApps'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> VisibleAppListOfUserEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.VisibleAppListOfUserEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    def limit(self, number: int=None) -> VisibleAppListOfUserEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VisibleAppListOfUserEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> AppsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppsResponse.parse_obj(json)

