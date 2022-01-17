from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiProductsEndpoint(Endpoint):
    path = '/v1/ciProducts'

    def fields(self, *, ci_product: Union[CiProductField, list[CiProductField]]=None, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None, ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]]=None, app: Union[AppField, list[AppField]]=None, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> CiProductsEndpoint:
        '''Fields to return for included related types.

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param ci_build_run: the fields to include for returned resources of type ciBuildRuns
        :type ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]] = None

        :param ci_workflow: the fields to include for returned resources of type ciWorkflows
        :type ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiProductsEndpoint
        '''
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if ci_build_run: self._set_fields('ciBuildRuns',ci_build_run if type(ci_build_run) is list else [ci_build_run])
        if ci_workflow: self._set_fields('ciWorkflows',ci_workflow if type(ci_workflow) is list else [ci_workflow])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BUNDLE_ID = 'bundleId'
        PRIMARY_REPOSITORIES = 'primaryRepositories'

    def filter(self, *, product_type: Union[CiProductType, list[CiProductType]]=None, app: Union[str, list[str]]=None) -> CiProductsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param product_type: filter by attribute 'productType'
        :type product_type: Union[CiProductType, list[CiProductType]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.CiProductsEndpoint
        '''
        if product_type: self._set_filter('productType', product_type if type(product_type) is list else [product_type])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> CiProductsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiProductsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, primary_repositories: int=None) -> CiProductsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param primary_repositories: maximum number of related primaryRepositories returned (when they are included). The maximum limit is 50
        :type primary_repositories: int = None

        :returns: self
        :rtype: applaud.endpoints.CiProductsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if primary_repositories and primary_repositories > 50:
            raise ValueError(f'The maximum limit of primary_repositories is 50')
        if primary_repositories: self._set_limit(primary_repositories, 'primaryRepositories')

        return self

    def get(self) -> CiProductsResponse:
        '''Get one or more resources.

        :returns: List of CiProducts
        :rtype: CiProductsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiProductsResponse.parse_obj(json)

class CiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}'

    @endpoint('/v1/ciProducts/{id}/additionalRepositories')
    def additional_repositories(self) -> AdditionalRepositoriesOfCiProductEndpoint:
        return AdditionalRepositoriesOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/app')
    def app(self) -> AppOfCiProductEndpoint:
        return AppOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/buildRuns')
    def build_runs(self) -> BuildRunsOfCiProductEndpoint:
        return BuildRunsOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/primaryRepositories')
    def primary_repositories(self) -> PrimaryRepositoriesOfCiProductEndpoint:
        return PrimaryRepositoriesOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/workflows')
    def workflows(self) -> WorkflowsOfCiProductEndpoint:
        return WorkflowsOfCiProductEndpoint(self.id, self.session)
        
    def fields(self, *, ci_product: Union[CiProductField, list[CiProductField]]=None, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None, ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]]=None, app: Union[AppField, list[AppField]]=None, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> CiProductEndpoint:
        '''Fields to return for included related types.

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param ci_build_run: the fields to include for returned resources of type ciBuildRuns
        :type ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]] = None

        :param ci_workflow: the fields to include for returned resources of type ciWorkflows
        :type ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiProductEndpoint
        '''
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if ci_build_run: self._set_fields('ciBuildRuns',ci_build_run if type(ci_build_run) is list else [ci_build_run])
        if ci_workflow: self._set_fields('ciWorkflows',ci_workflow if type(ci_workflow) is list else [ci_workflow])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BUNDLE_ID = 'bundleId'
        PRIMARY_REPOSITORIES = 'primaryRepositories'

    def include(self, relationship: Union[Include, list[Include]]) -> CiProductEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiProductEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, primary_repositories: int=None) -> CiProductEndpoint:
        '''Number of included related resources to return.

        :param primary_repositories: maximum number of related primaryRepositories returned (when they are included). The maximum limit is 50
        :type primary_repositories: int = None

        :returns: self
        :rtype: applaud.endpoints.CiProductEndpoint
        '''
        if primary_repositories and primary_repositories > 50:
            raise ValueError(f'The maximum limit of primary_repositories is 50')
        if primary_repositories: self._set_limit(primary_repositories, 'primaryRepositories')

        return self

    def get(self) -> CiProductResponse:
        '''Get the resource.

        :returns: Single CiProduct
        :rtype: CiProductResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiProductResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AdditionalRepositoriesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/additionalRepositories'

    def fields(self, *, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> AdditionalRepositoriesOfCiProductEndpoint:
        '''Fields to return for included related types.

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AdditionalRepositoriesOfCiProductEndpoint
        '''
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    def filter(self, *, id: Union[str, list[str]]=None) -> AdditionalRepositoriesOfCiProductEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AdditionalRepositoriesOfCiProductEndpoint
        '''
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def limit(self, number: int=None) -> AdditionalRepositoriesOfCiProductEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AdditionalRepositoriesOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ScmRepositoriesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: ScmRepositoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmRepositoriesResponse.parse_obj(json)

class AppOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/app'

    def fields(self, *, game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]]=None, app_clip: Union[AppClipField, list[AppClipField]]=None, beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]]=None, app_info: Union[AppInfoField, list[AppInfoField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, app: Union[AppField, list[AppField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, build: Union[BuildField, list[BuildField]]=None, app_price: Union[AppPriceField, list[AppPriceField]]=None) -> AppOfCiProductEndpoint:
        '''Fields to return for included related types.

        :param game_center_enabled_version: the fields to include for returned resources of type gameCenterEnabledVersions
        :type game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]] = None

        :param app_clip: the fields to include for returned resources of type appClips
        :type app_clip: Union[AppClipField, list[AppClipField]] = None

        :param beta_app_localization: the fields to include for returned resources of type betaAppLocalizations
        :type beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]] = None

        :param app_info: the fields to include for returned resources of type appInfos
        :type app_info: Union[AppInfoField, list[AppInfoField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param app_price: the fields to include for returned resources of type appPrices
        :type app_price: Union[AppPriceField, list[AppPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfCiProductEndpoint
        '''
        if game_center_enabled_version: self._set_fields('gameCenterEnabledVersions',game_center_enabled_version if type(game_center_enabled_version) is list else [game_center_enabled_version])
        if app_clip: self._set_fields('appClips',app_clip if type(app_clip) is list else [app_clip])
        if beta_app_localization: self._set_fields('betaAppLocalizations',beta_app_localization if type(beta_app_localization) is list else [beta_app_localization])
        if app_info: self._set_fields('appInfos',app_info if type(app_info) is list else [app_info])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if app_price: self._set_fields('appPrices',app_price if type(app_price) is list else [app_price])
        return self
        
    class Include(StringEnum):
        APP_CLIPS = 'appClips'
        APP_INFOS = 'appInfos'
        APP_STORE_VERSIONS = 'appStoreVersions'
        AVAILABLE_TERRITORIES = 'availableTerritories'
        BETA_APP_LOCALIZATIONS = 'betaAppLocalizations'
        BETA_GROUPS = 'betaGroups'
        BUILDS = 'builds'
        GAME_CENTER_ENABLED_VERSIONS = 'gameCenterEnabledVersions'
        IN_APP_PURCHASES = 'inAppPurchases'
        PRE_RELEASE_VERSIONS = 'preReleaseVersions'
        PRICES = 'prices'

    def include(self, relationship: Union[Include, list[Include]]) -> AppOfCiProductEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppOfCiProductEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, beta_groups: int=None, app_store_versions: int=None, pre_release_versions: int=None, beta_app_localizations: int=None, builds: int=None, app_infos: int=None, app_clips: int=None, prices: int=None, available_territories: int=None, in_app_purchases: int=None, game_center_enabled_versions: int=None) -> AppOfCiProductEndpoint:
        '''Number of included related resources to return.

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param app_store_versions: maximum number of related appStoreVersions returned (when they are included). The maximum limit is 50
        :type app_store_versions: int = None

        :param pre_release_versions: maximum number of related preReleaseVersions returned (when they are included). The maximum limit is 50
        :type pre_release_versions: int = None

        :param beta_app_localizations: maximum number of related betaAppLocalizations returned (when they are included). The maximum limit is 50
        :type beta_app_localizations: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :param app_infos: maximum number of related appInfos returned (when they are included). The maximum limit is 50
        :type app_infos: int = None

        :param app_clips: maximum number of related appClips returned (when they are included). The maximum limit is 50
        :type app_clips: int = None

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :param available_territories: maximum number of related availableTerritories returned (when they are included). The maximum limit is 50
        :type available_territories: int = None

        :param in_app_purchases: maximum number of related inAppPurchases returned (when they are included). The maximum limit is 50
        :type in_app_purchases: int = None

        :param game_center_enabled_versions: maximum number of related gameCenterEnabledVersions returned (when they are included). The maximum limit is 50
        :type game_center_enabled_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.AppOfCiProductEndpoint
        '''
        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit of beta_groups is 50')
        if beta_groups: self._set_limit(beta_groups, 'betaGroups')

        if app_store_versions and app_store_versions > 50:
            raise ValueError(f'The maximum limit of app_store_versions is 50')
        if app_store_versions: self._set_limit(app_store_versions, 'appStoreVersions')

        if pre_release_versions and pre_release_versions > 50:
            raise ValueError(f'The maximum limit of pre_release_versions is 50')
        if pre_release_versions: self._set_limit(pre_release_versions, 'preReleaseVersions')

        if beta_app_localizations and beta_app_localizations > 50:
            raise ValueError(f'The maximum limit of beta_app_localizations is 50')
        if beta_app_localizations: self._set_limit(beta_app_localizations, 'betaAppLocalizations')

        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        if app_infos and app_infos > 50:
            raise ValueError(f'The maximum limit of app_infos is 50')
        if app_infos: self._set_limit(app_infos, 'appInfos')

        if app_clips and app_clips > 50:
            raise ValueError(f'The maximum limit of app_clips is 50')
        if app_clips: self._set_limit(app_clips, 'appClips')

        if prices and prices > 50:
            raise ValueError(f'The maximum limit of prices is 50')
        if prices: self._set_limit(prices, 'prices')

        if available_territories and available_territories > 50:
            raise ValueError(f'The maximum limit of available_territories is 50')
        if available_territories: self._set_limit(available_territories, 'availableTerritories')

        if in_app_purchases and in_app_purchases > 50:
            raise ValueError(f'The maximum limit of in_app_purchases is 50')
        if in_app_purchases: self._set_limit(in_app_purchases, 'inAppPurchases')

        if game_center_enabled_versions and game_center_enabled_versions > 50:
            raise ValueError(f'The maximum limit of game_center_enabled_versions is 50')
        if game_center_enabled_versions: self._set_limit(game_center_enabled_versions, 'gameCenterEnabledVersions')

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

class BuildRunsOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/buildRuns'

    def fields(self, *, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BuildRunsOfCiProductEndpoint:
        '''Fields to return for included related types.

        :param ci_build_run: the fields to include for returned resources of type ciBuildRuns
        :type ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiProductEndpoint
        '''
        if ci_build_run: self._set_fields('ciBuildRuns',ci_build_run if type(ci_build_run) is list else [ci_build_run])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILDS = 'builds'

    def filter(self, *, builds: Union[str, list[str]]=None) -> BuildRunsOfCiProductEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param builds: filter by id(s) of related 'builds'
        :type builds: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiProductEndpoint
        '''
        if builds: self._set_filter('builds', builds if type(builds) is list else [builds])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BuildRunsOfCiProductEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiProductEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, builds: int=None) -> BuildRunsOfCiProductEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        return self

    def get(self) -> CiBuildRunsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: CiBuildRunsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildRunsResponse.parse_obj(json)

class PrimaryRepositoriesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/primaryRepositories'

    def fields(self, *, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> PrimaryRepositoriesOfCiProductEndpoint:
        '''Fields to return for included related types.

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.PrimaryRepositoriesOfCiProductEndpoint
        '''
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    def filter(self, *, id: Union[str, list[str]]=None) -> PrimaryRepositoriesOfCiProductEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PrimaryRepositoriesOfCiProductEndpoint
        '''
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def limit(self, number: int=None) -> PrimaryRepositoriesOfCiProductEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PrimaryRepositoriesOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ScmRepositoriesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: ScmRepositoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmRepositoriesResponse.parse_obj(json)

class WorkflowsOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/workflows'

    def fields(self, *, ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]]=None) -> WorkflowsOfCiProductEndpoint:
        '''Fields to return for included related types.

        :param ci_workflow: the fields to include for returned resources of type ciWorkflows
        :type ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]] = None

        :returns: self
        :rtype: applaud.endpoints.WorkflowsOfCiProductEndpoint
        '''
        if ci_workflow: self._set_fields('ciWorkflows',ci_workflow if type(ci_workflow) is list else [ci_workflow])
        return self
        
    def limit(self, number: int=None) -> WorkflowsOfCiProductEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.WorkflowsOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiWorkflowsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: CiWorkflowsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiWorkflowsResponse.parse_obj(json)

