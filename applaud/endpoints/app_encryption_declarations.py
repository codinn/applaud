from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppEncryptionDeclarationsEndpoint(Endpoint):
    path = '/v1/appEncryptionDeclarations'

    def fields(self, *, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, app: Union[AppField, list[AppField]]=None) -> AppEncryptionDeclarationsEndpoint:
        '''Fields to return for included related types.

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationsEndpoint
        '''
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def filter(self, *, platform: Union[Platform, list[Platform]]=None, app: Union[str, list[str]]=None, builds: Union[str, list[str]]=None) -> AppEncryptionDeclarationsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :param builds: filter by id(s) of related 'builds'
        :type builds: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationsEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        if builds: self._set_filter('builds', builds if type(builds) is list else [builds])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppEncryptionDeclarationsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> AppEncryptionDeclarationsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppEncryptionDeclarationsResponse:
        '''Get one or more resources.

        :returns: List of AppEncryptionDeclarations
        :rtype: AppEncryptionDeclarationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEncryptionDeclarationsResponse.parse_obj(json)

class AppEncryptionDeclarationEndpoint(IDEndpoint):
    path = '/v1/appEncryptionDeclarations/{id}'

    @endpoint('/v1/appEncryptionDeclarations/{id}/app')
    def app(self) -> AppOfAppEncryptionDeclarationEndpoint:
        return AppOfAppEncryptionDeclarationEndpoint(self.id, self.session)
        
    @endpoint('/v1/appEncryptionDeclarations/{id}/relationships/builds')
    def builds_linkages(self) -> BuildsLinkagesOfAppEncryptionDeclarationEndpoint:
        return BuildsLinkagesOfAppEncryptionDeclarationEndpoint(self.id, self.session)
        
    def fields(self, *, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, app: Union[AppField, list[AppField]]=None) -> AppEncryptionDeclarationEndpoint:
        '''Fields to return for included related types.

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationEndpoint
        '''
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def include(self, relationship: Union[Include, list[Include]]) -> AppEncryptionDeclarationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppEncryptionDeclarationResponse:
        '''Get the resource.

        :returns: Single AppEncryptionDeclaration
        :rtype: AppEncryptionDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEncryptionDeclarationResponse.parse_obj(json)

class AppOfAppEncryptionDeclarationEndpoint(IDEndpoint):
    path = '/v1/appEncryptionDeclarations/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppOfAppEncryptionDeclarationEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfAppEncryptionDeclarationEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    def get(self) -> AppResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppResponse.parse_obj(json)

class BuildsLinkagesOfAppEncryptionDeclarationEndpoint(IDEndpoint):
    path = '/v1/appEncryptionDeclarations/{id}/relationships/builds'

    def create(self, request: AppEncryptionDeclarationBuildsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: AppEncryptionDeclarationBuildsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

