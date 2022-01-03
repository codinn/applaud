from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BuildBetaDetailListEndpoint(Endpoint):
    path = '/v1/buildBetaDetails'

    def fields(self, *, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BuildBetaDetailListEndpoint:
        '''Fields to return for included related types.

        :param build_beta_detail: the fields to include for returned resources of type buildBetaDetails
        :type build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailListEndpoint
        '''
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'

    def filter(self, *, build: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> BuildBetaDetailListEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param build: filter by id(s) of related 'build'
        :type build: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailListEndpoint
        '''
        if build: self._set_filter('build', build if type(build) is list else [build])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BuildBetaDetailListEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailListEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> BuildBetaDetailListEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailListEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BuildBetaDetailsResponse:
        '''Get one or more resources.

        :returns: List of BuildBetaDetails
        :rtype: BuildBetaDetailsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildBetaDetailsResponse.parse_obj(json)

class BuildBetaDetailEndpoint(IDEndpoint):
    path = '/v1/buildBetaDetails/{id}'

    def fields(self, *, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BuildBetaDetailEndpoint:
        '''Fields to return for included related types.

        :param build_beta_detail: the fields to include for returned resources of type buildBetaDetails
        :type build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailEndpoint
        '''
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'

    def include(self, relationship: Union[Include, list[Include]]) -> BuildBetaDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BuildBetaDetailResponse:
        '''Get the resource.

        :returns: Single BuildBetaDetail
        :rtype: BuildBetaDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildBetaDetailResponse.parse_obj(json)

    def update(self, request: BuildBetaDetailUpdateRequest) -> BuildBetaDetailResponse:
        '''Modify the resource.

        :param request: BuildBetaDetail representation
        :type request: BuildBetaDetailUpdateRequest

        :returns: Single BuildBetaDetail
        :rtype: BuildBetaDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_patch(json)
        return BuildBetaDetailResponse.parse_obj(response_json)

class BuildOfBuildBetaDetailEndpoint(IDEndpoint):
    path = '/v1/buildBetaDetails/{id}/build'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildOfBuildBetaDetailEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildOfBuildBetaDetailEndpoint
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

