from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppClipDomainCacheStatusOfBuildBundleEndpoint(IDEndpoint):
    path = '/v1/buildBundles/{id}/appClipDomainCacheStatus'

    def fields(self, *, app_clip_domain_statuse: Union[AppClipDomainStatuseField, list[AppClipDomainStatuseField]]=None) -> AppClipDomainCacheStatusOfBuildBundleEndpoint:
        '''Fields to return for included related types.

        :param app_clip_domain_statuse: the fields to include for returned resources of type appClipDomainStatuses
        :type app_clip_domain_statuse: Union[AppClipDomainStatuseField, list[AppClipDomainStatuseField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDomainCacheStatusOfBuildBundleEndpoint
        '''
        if app_clip_domain_statuse: self._set_fields('appClipDomainStatuses',app_clip_domain_statuse if type(app_clip_domain_statuse) is list else [app_clip_domain_statuse])
        return self
        
    def get(self) -> AppClipDomainStatusResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppClipDomainStatusResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDomainStatusResponse.parse_obj(json)

class AppClipDomainDebugStatusOfBuildBundleEndpoint(IDEndpoint):
    path = '/v1/buildBundles/{id}/appClipDomainDebugStatus'

    def fields(self, *, app_clip_domain_statuse: Union[AppClipDomainStatuseField, list[AppClipDomainStatuseField]]=None) -> AppClipDomainDebugStatusOfBuildBundleEndpoint:
        '''Fields to return for included related types.

        :param app_clip_domain_statuse: the fields to include for returned resources of type appClipDomainStatuses
        :type app_clip_domain_statuse: Union[AppClipDomainStatuseField, list[AppClipDomainStatuseField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDomainDebugStatusOfBuildBundleEndpoint
        '''
        if app_clip_domain_statuse: self._set_fields('appClipDomainStatuses',app_clip_domain_statuse if type(app_clip_domain_statuse) is list else [app_clip_domain_statuse])
        return self
        
    def get(self) -> AppClipDomainStatusResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppClipDomainStatusResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDomainStatusResponse.parse_obj(json)

class BetaAppClipInvocationsOfBuildBundleEndpoint(IDEndpoint):
    path = '/v1/buildBundles/{id}/betaAppClipInvocations'

    def fields(self, *, beta_app_clip_invocation: Union[BetaAppClipInvocationField, list[BetaAppClipInvocationField]]=None, beta_app_clip_invocation_localization: Union[BetaAppClipInvocationLocalizationField, list[BetaAppClipInvocationLocalizationField]]=None) -> BetaAppClipInvocationsOfBuildBundleEndpoint:
        '''Fields to return for included related types.

        :param beta_app_clip_invocation: the fields to include for returned resources of type betaAppClipInvocations
        :type beta_app_clip_invocation: Union[BetaAppClipInvocationField, list[BetaAppClipInvocationField]] = None

        :param beta_app_clip_invocation_localization: the fields to include for returned resources of type betaAppClipInvocationLocalizations
        :type beta_app_clip_invocation_localization: Union[BetaAppClipInvocationLocalizationField, list[BetaAppClipInvocationLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppClipInvocationsOfBuildBundleEndpoint
        '''
        if beta_app_clip_invocation: self._set_fields('betaAppClipInvocations',beta_app_clip_invocation if type(beta_app_clip_invocation) is list else [beta_app_clip_invocation])
        if beta_app_clip_invocation_localization: self._set_fields('betaAppClipInvocationLocalizations',beta_app_clip_invocation_localization if type(beta_app_clip_invocation_localization) is list else [beta_app_clip_invocation_localization])
        return self
        
    class Include(StringEnum):
        BETA_APP_CLIP_INVOCATION_LOCALIZATIONS = 'betaAppClipInvocationLocalizations'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaAppClipInvocationsOfBuildBundleEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaAppClipInvocationsOfBuildBundleEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, beta_app_clip_invocation_localizations: int=None) -> BetaAppClipInvocationsOfBuildBundleEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param beta_app_clip_invocation_localizations: maximum number of related betaAppClipInvocationLocalizations returned (when they are included). The maximum limit is 50
        :type beta_app_clip_invocation_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppClipInvocationsOfBuildBundleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if beta_app_clip_invocation_localizations and beta_app_clip_invocation_localizations > 50:
            raise ValueError(f'The maximum limit is 50')
        if beta_app_clip_invocation_localizations: self._set_limit('betaAppClipInvocationLocalizations', beta_app_clip_invocation_localizations)

        return self

    def get(self) -> BetaAppClipInvocationsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BetaAppClipInvocationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppClipInvocationsResponse.parse_obj(json)

class BuildBundleFileSizesOfBuildBundleEndpoint(IDEndpoint):
    path = '/v1/buildBundles/{id}/buildBundleFileSizes'

    def fields(self, *, build_bundle_file_size: Union[BuildBundleFileSizeField, list[BuildBundleFileSizeField]]=None) -> BuildBundleFileSizesOfBuildBundleEndpoint:
        '''Fields to return for included related types.

        :param build_bundle_file_size: the fields to include for returned resources of type buildBundleFileSizes
        :type build_bundle_file_size: Union[BuildBundleFileSizeField, list[BuildBundleFileSizeField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildBundleFileSizesOfBuildBundleEndpoint
        '''
        if build_bundle_file_size: self._set_fields('buildBundleFileSizes',build_bundle_file_size if type(build_bundle_file_size) is list else [build_bundle_file_size])
        return self
        
    def limit(self, number: int=None) -> BuildBundleFileSizesOfBuildBundleEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildBundleFileSizesOfBuildBundleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BuildBundleFileSizesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BuildBundleFileSizesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildBundleFileSizesResponse.parse_obj(json)

class BuildBundleEndpoint(IDEndpoint):
    path = '/v1/buildBundles/{id}'

    @endpoint('/v1/buildBundles/{id}/appClipDomainCacheStatus')
    def app_clip_domain_cache_status(self) -> AppClipDomainCacheStatusOfBuildBundleEndpoint:
        return AppClipDomainCacheStatusOfBuildBundleEndpoint(self.id, self.session)
        
    @endpoint('/v1/buildBundles/{id}/appClipDomainDebugStatus')
    def app_clip_domain_debug_status(self) -> AppClipDomainDebugStatusOfBuildBundleEndpoint:
        return AppClipDomainDebugStatusOfBuildBundleEndpoint(self.id, self.session)
        
    @endpoint('/v1/buildBundles/{id}/betaAppClipInvocations')
    def beta_app_clip_invocations(self) -> BetaAppClipInvocationsOfBuildBundleEndpoint:
        return BetaAppClipInvocationsOfBuildBundleEndpoint(self.id, self.session)
        
    @endpoint('/v1/buildBundles/{id}/buildBundleFileSizes')
    def build_bundle_file_sizes(self) -> BuildBundleFileSizesOfBuildBundleEndpoint:
        return BuildBundleFileSizesOfBuildBundleEndpoint(self.id, self.session)
        
