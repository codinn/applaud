from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class UserInvitationsEndpoint(Endpoint):
    path = '/v1/userInvitations'

    def fields(self, *, user_invitation: Union[UserInvitationField, list[UserInvitationField]]=None, app: Union[AppField, list[AppField]]=None) -> UserInvitationsEndpoint:
        '''Fields to return for included related types.

        :param user_invitation: the fields to include for returned resources of type userInvitations
        :type user_invitation: Union[UserInvitationField, list[UserInvitationField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.UserInvitationsEndpoint
        '''
        if user_invitation: self._set_fields('userInvitations',user_invitation if type(user_invitation) is list else [user_invitation])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        VISIBLE_APPS = 'visibleApps'

    def filter(self, *, email: Union[str, list[str]]=None, roles: Union[UserRole, list[UserRole]]=None, visible_apps: Union[str, list[str]]=None) -> UserInvitationsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param email: filter by attribute 'email'
        :type email: Union[str, list[str]] = None

        :param roles: filter by attribute 'roles'
        :type roles: Union[UserRole, list[UserRole]] = None

        :param visible_apps: filter by id(s) of related 'visibleApps'
        :type visible_apps: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.UserInvitationsEndpoint
        '''
        if email: self._set_filter('email', email if type(email) is list else [email])
        
        if roles: self._set_filter('roles', roles if type(roles) is list else [roles])
        
        if visible_apps: self._set_filter('visibleApps', visible_apps if type(visible_apps) is list else [visible_apps])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> UserInvitationsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.UserInvitationsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, email: SortOrder=None, last_name: SortOrder=None) -> UserInvitationsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.UserInvitationsEndpoint
        '''
        if email: self.sort_expressions.append('email' if email == SortOrder.ASC else '-email')
        if last_name: self.sort_expressions.append('lastName' if last_name == SortOrder.ASC else '-lastName')
        return self
        
    def limit(self, number: int=None, *, visible_apps: int=None) -> UserInvitationsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param visible_apps: maximum number of related visibleApps returned (when they are included). The maximum limit is 50
        :type visible_apps: int = None

        :returns: self
        :rtype: applaud.endpoints.UserInvitationsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if visible_apps and visible_apps > 50:
            raise ValueError(f'The maximum limit of visible_apps is 50')
        if visible_apps: self._set_limit(visible_apps, 'visibleApps')

        return self

    def get(self) -> UserInvitationsResponse:
        '''Get one or more resources.

        :returns: List of UserInvitations
        :rtype: UserInvitationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return UserInvitationsResponse.parse_obj(json)

    def create(self, request: UserInvitationCreateRequest) -> UserInvitationResponse:
        '''Create the resource.

        :param request: UserInvitation representation
        :type request: UserInvitationCreateRequest

        :returns: Single UserInvitation
        :rtype: UserInvitationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return UserInvitationResponse.parse_obj(json)

class UserInvitationEndpoint(IDEndpoint):
    path = '/v1/userInvitations/{id}'

    @endpoint('/v1/userInvitations/{id}/visibleApps')
    def visible_apps(self) -> VisibleAppsOfUserInvitationEndpoint:
        return VisibleAppsOfUserInvitationEndpoint(self.id, self.session)
        
    def fields(self, *, user_invitation: Union[UserInvitationField, list[UserInvitationField]]=None, app: Union[AppField, list[AppField]]=None) -> UserInvitationEndpoint:
        '''Fields to return for included related types.

        :param user_invitation: the fields to include for returned resources of type userInvitations
        :type user_invitation: Union[UserInvitationField, list[UserInvitationField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.UserInvitationEndpoint
        '''
        if user_invitation: self._set_fields('userInvitations',user_invitation if type(user_invitation) is list else [user_invitation])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        VISIBLE_APPS = 'visibleApps'

    def include(self, relationship: Union[Include, list[Include]]) -> UserInvitationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.UserInvitationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, visible_apps: int=None) -> UserInvitationEndpoint:
        '''Number of included related resources to return.

        :param visible_apps: maximum number of related visibleApps returned (when they are included). The maximum limit is 50
        :type visible_apps: int = None

        :returns: self
        :rtype: applaud.endpoints.UserInvitationEndpoint
        '''
        if visible_apps and visible_apps > 50:
            raise ValueError(f'The maximum limit of visible_apps is 50')
        if visible_apps: self._set_limit(visible_apps, 'visibleApps')

        return self

    def get(self) -> UserInvitationResponse:
        '''Get the resource.

        :returns: Single UserInvitation
        :rtype: UserInvitationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return UserInvitationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class VisibleAppsOfUserInvitationEndpoint(IDEndpoint):
    path = '/v1/userInvitations/{id}/visibleApps'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> VisibleAppsOfUserInvitationEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.VisibleAppsOfUserInvitationEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    def limit(self, number: int=None) -> VisibleAppsOfUserInvitationEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VisibleAppsOfUserInvitationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
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

