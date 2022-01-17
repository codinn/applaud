from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaAppLocalizationsEndpoint(Endpoint):
    path = '/v1/betaAppLocalizations'

    def fields(self, *, beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]]=None, app: Union[AppField, list[AppField]]=None) -> BetaAppLocalizationsEndpoint:
        '''Fields to return for included related types.

        :param beta_app_localization: the fields to include for returned resources of type betaAppLocalizations
        :type beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationsEndpoint
        '''
        if beta_app_localization: self._set_fields('betaAppLocalizations',beta_app_localization if type(beta_app_localization) is list else [beta_app_localization])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def filter(self, *, locale: Union[str, list[str]]=None, app: Union[str, list[str]]=None) -> BetaAppLocalizationsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param locale: filter by attribute 'locale'
        :type locale: Union[str, list[str]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationsEndpoint
        '''
        if locale: self._set_filter('locale', locale if type(locale) is list else [locale])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BetaAppLocalizationsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> BetaAppLocalizationsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaAppLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of BetaAppLocalizations
        :rtype: BetaAppLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppLocalizationsResponse.parse_obj(json)

    def create(self, request: BetaAppLocalizationCreateRequest) -> BetaAppLocalizationResponse:
        '''Create the resource.

        :param request: BetaAppLocalization representation
        :type request: BetaAppLocalizationCreateRequest

        :returns: Single BetaAppLocalization
        :rtype: BetaAppLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BetaAppLocalizationResponse.parse_obj(json)

class BetaAppLocalizationEndpoint(IDEndpoint):
    path = '/v1/betaAppLocalizations/{id}'

    @endpoint('/v1/betaAppLocalizations/{id}/app')
    def app(self) -> AppOfBetaAppLocalizationEndpoint:
        return AppOfBetaAppLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]]=None, app: Union[AppField, list[AppField]]=None) -> BetaAppLocalizationEndpoint:
        '''Fields to return for included related types.

        :param beta_app_localization: the fields to include for returned resources of type betaAppLocalizations
        :type beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationEndpoint
        '''
        if beta_app_localization: self._set_fields('betaAppLocalizations',beta_app_localization if type(beta_app_localization) is list else [beta_app_localization])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaAppLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BetaAppLocalizationResponse:
        '''Get the resource.

        :returns: Single BetaAppLocalization
        :rtype: BetaAppLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppLocalizationResponse.parse_obj(json)

    def update(self, request: BetaAppLocalizationUpdateRequest) -> BetaAppLocalizationResponse:
        '''Modify the resource.

        :param request: BetaAppLocalization representation
        :type request: BetaAppLocalizationUpdateRequest

        :returns: Single BetaAppLocalization
        :rtype: BetaAppLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BetaAppLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppOfBetaAppLocalizationEndpoint(IDEndpoint):
    path = '/v1/betaAppLocalizations/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppOfBetaAppLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfBetaAppLocalizationEndpoint
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

