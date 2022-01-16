from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaBuildLocalizationsEndpoint(Endpoint):
    path = '/v1/betaBuildLocalizations'

    def fields(self, *, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BetaBuildLocalizationsEndpoint:
        '''Fields to return for included related types.

        :param beta_build_localization: the fields to include for returned resources of type betaBuildLocalizations
        :type beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationsEndpoint
        '''
        if beta_build_localization: self._set_fields('betaBuildLocalizations',beta_build_localization if type(beta_build_localization) is list else [beta_build_localization])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'

    def filter(self, *, locale: Union[str, list[str]]=None, build: Union[str, list[str]]=None) -> BetaBuildLocalizationsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param locale: filter by attribute 'locale'
        :type locale: Union[str, list[str]] = None

        :param build: filter by id(s) of related 'build'
        :type build: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationsEndpoint
        '''
        if locale: self._set_filter('locale', locale if type(locale) is list else [locale])
        
        if build: self._set_filter('build', build if type(build) is list else [build])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BetaBuildLocalizationsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> BetaBuildLocalizationsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaBuildLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of BetaBuildLocalizations
        :rtype: BetaBuildLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaBuildLocalizationsResponse.parse_obj(json)

    def create(self, request: BetaBuildLocalizationCreateRequest) -> BetaBuildLocalizationResponse:
        '''Create the resource.

        :param request: BetaBuildLocalization representation
        :type request: BetaBuildLocalizationCreateRequest

        :returns: Single BetaBuildLocalization
        :rtype: BetaBuildLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BetaBuildLocalizationResponse.parse_obj(json)

class BetaBuildLocalizationEndpoint(IDEndpoint):
    path = '/v1/betaBuildLocalizations/{id}'

    @endpoint('/v1/betaBuildLocalizations/{id}/build')
    def build(self) -> BuildOfBetaBuildLocalizationEndpoint:
        return BuildOfBetaBuildLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BetaBuildLocalizationEndpoint:
        '''Fields to return for included related types.

        :param beta_build_localization: the fields to include for returned resources of type betaBuildLocalizations
        :type beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationEndpoint
        '''
        if beta_build_localization: self._set_fields('betaBuildLocalizations',beta_build_localization if type(beta_build_localization) is list else [beta_build_localization])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaBuildLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BetaBuildLocalizationResponse:
        '''Get the resource.

        :returns: Single BetaBuildLocalization
        :rtype: BetaBuildLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaBuildLocalizationResponse.parse_obj(json)

    def update(self, request: BetaBuildLocalizationUpdateRequest) -> BetaBuildLocalizationResponse:
        '''Modify the resource.

        :param request: BetaBuildLocalization representation
        :type request: BetaBuildLocalizationUpdateRequest

        :returns: Single BetaBuildLocalization
        :rtype: BetaBuildLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BetaBuildLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class BuildOfBetaBuildLocalizationEndpoint(IDEndpoint):
    path = '/v1/betaBuildLocalizations/{id}/build'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildOfBetaBuildLocalizationEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildOfBetaBuildLocalizationEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    def get(self) -> BuildResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: BuildResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildResponse.parse_obj(json)

