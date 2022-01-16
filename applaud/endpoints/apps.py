from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppsEndpoint(Endpoint):
    path = '/v1/apps'

    def fields(self, *, app: Union[AppField, list[AppField]]=None, beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]]=None, beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]]=None, app_clip: Union[AppClipField, list[AppClipField]]=None, app_info: Union[AppInfoField, list[AppInfoField]]=None, beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, ci_product: Union[CiProductField, list[CiProductField]]=None, app_price: Union[AppPriceField, list[AppPriceField]]=None, app_pre_order: Union[AppPreOrderField, list[AppPreOrderField]]=None, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]]=None, end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, perf_power_metric: Union[PerfPowerMetricField, list[PerfPowerMetricField]]=None, build: Union[BuildField, list[BuildField]]=None) -> AppsEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param beta_license_agreement: the fields to include for returned resources of type betaLicenseAgreements
        :type beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]] = None

        :param beta_app_review_detail: the fields to include for returned resources of type betaAppReviewDetails
        :type beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]] = None

        :param app_clip: the fields to include for returned resources of type appClips
        :type app_clip: Union[AppClipField, list[AppClipField]] = None

        :param app_info: the fields to include for returned resources of type appInfos
        :type app_info: Union[AppInfoField, list[AppInfoField]] = None

        :param beta_app_localization: the fields to include for returned resources of type betaAppLocalizations
        :type beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param app_price: the fields to include for returned resources of type appPrices
        :type app_price: Union[AppPriceField, list[AppPriceField]] = None

        :param app_pre_order: the fields to include for returned resources of type appPreOrders
        :type app_pre_order: Union[AppPreOrderField, list[AppPreOrderField]] = None

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :param game_center_enabled_version: the fields to include for returned resources of type gameCenterEnabledVersions
        :type game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]] = None

        :param end_user_license_agreement: the fields to include for returned resources of type endUserLicenseAgreements
        :type end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param perf_power_metric: the fields to include for returned resources of type perfPowerMetrics
        :type perf_power_metric: Union[PerfPowerMetricField, list[PerfPowerMetricField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if beta_license_agreement: self._set_fields('betaLicenseAgreements',beta_license_agreement if type(beta_license_agreement) is list else [beta_license_agreement])
        if beta_app_review_detail: self._set_fields('betaAppReviewDetails',beta_app_review_detail if type(beta_app_review_detail) is list else [beta_app_review_detail])
        if app_clip: self._set_fields('appClips',app_clip if type(app_clip) is list else [app_clip])
        if app_info: self._set_fields('appInfos',app_info if type(app_info) is list else [app_info])
        if beta_app_localization: self._set_fields('betaAppLocalizations',beta_app_localization if type(beta_app_localization) is list else [beta_app_localization])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if app_price: self._set_fields('appPrices',app_price if type(app_price) is list else [app_price])
        if app_pre_order: self._set_fields('appPreOrders',app_pre_order if type(app_pre_order) is list else [app_pre_order])
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        if game_center_enabled_version: self._set_fields('gameCenterEnabledVersions',game_center_enabled_version if type(game_center_enabled_version) is list else [game_center_enabled_version])
        if end_user_license_agreement: self._set_fields('endUserLicenseAgreements',end_user_license_agreement if type(end_user_license_agreement) is list else [end_user_license_agreement])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if perf_power_metric: self._set_fields('perfPowerMetrics',perf_power_metric if type(perf_power_metric) is list else [perf_power_metric])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        APP_CLIPS = 'appClips'
        APP_INFOS = 'appInfos'
        APP_STORE_VERSIONS = 'appStoreVersions'
        AVAILABLE_TERRITORIES = 'availableTerritories'
        BETA_APP_LOCALIZATIONS = 'betaAppLocalizations'
        BETA_APP_REVIEW_DETAIL = 'betaAppReviewDetail'
        BETA_GROUPS = 'betaGroups'
        BETA_LICENSE_AGREEMENT = 'betaLicenseAgreement'
        BUILDS = 'builds'
        CI_PRODUCT = 'ciProduct'
        END_USER_LICENSE_AGREEMENT = 'endUserLicenseAgreement'
        GAME_CENTER_ENABLED_VERSIONS = 'gameCenterEnabledVersions'
        IN_APP_PURCHASES = 'inAppPurchases'
        PRE_ORDER = 'preOrder'
        PRE_RELEASE_VERSIONS = 'preReleaseVersions'
        PRICES = 'prices'

    def exists(self, *, game_center_enabled_versions: bool=None) -> AppsEndpoint:
        ''' Filter by existence or non-existence of related resource.
        
        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if game_center_enabled_versions == None:
            return
        
        self._set_exists('gameCenterEnabledVersions', 'true' if game_center_enabled_versions  else 'false')
        return self
        
    def filter(self, *, app_store_versions_app_store_state: Union[AppStoreVersionState, list[AppStoreVersionState]]=None, app_store_versions_platform: Union[Platform, list[Platform]]=None, bundle_id: Union[str, list[str]]=None, name: Union[str, list[str]]=None, sku: Union[str, list[str]]=None, app_store_versions: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> AppsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param app_store_versions_app_store_state: filter by attribute 'appStoreVersions.appStoreState'
        :type app_store_versions_app_store_state: Union[AppStoreVersionState, list[AppStoreVersionState]] = None

        :param app_store_versions_platform: filter by attribute 'appStoreVersions.platform'
        :type app_store_versions_platform: Union[Platform, list[Platform]] = None

        :param bundle_id: filter by attribute 'bundleId'
        :type bundle_id: Union[str, list[str]] = None

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param sku: filter by attribute 'sku'
        :type sku: Union[str, list[str]] = None

        :param app_store_versions: filter by id(s) of related 'appStoreVersions'
        :type app_store_versions: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if app_store_versions_app_store_state: self._set_filter('appStoreVersions.appStoreState', app_store_versions_app_store_state if type(app_store_versions_app_store_state) is list else [app_store_versions_app_store_state])
        
        if app_store_versions_platform: self._set_filter('appStoreVersions.platform', app_store_versions_platform if type(app_store_versions_platform) is list else [app_store_versions_platform])
        
        if bundle_id: self._set_filter('bundleId', bundle_id if type(bundle_id) is list else [bundle_id])
        
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if sku: self._set_filter('sku', sku if type(sku) is list else [sku])
        
        if app_store_versions: self._set_filter('appStoreVersions', app_store_versions if type(app_store_versions) is list else [app_store_versions])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, bundle_id: SortOrder=None, name: SortOrder=None, sku: SortOrder=None) -> AppsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if bundle_id: self.sort_expressions.append('bundleId' if bundle_id == SortOrder.ASC else '-bundleId')
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if sku: self.sort_expressions.append('sku' if sku == SortOrder.ASC else '-sku')
        return self
        
    def limit(self, number: int=None, *, app_clips: int=None, app_infos: int=None, app_store_versions: int=None, available_territories: int=None, beta_app_localizations: int=None, beta_groups: int=None, builds: int=None, game_center_enabled_versions: int=None, in_app_purchases: int=None, pre_release_versions: int=None, prices: int=None) -> AppsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_clips: maximum number of related appClips returned (when they are included). The maximum limit is 50
        :type app_clips: int = None

        :param app_infos: maximum number of related appInfos returned (when they are included). The maximum limit is 50
        :type app_infos: int = None

        :param app_store_versions: maximum number of related appStoreVersions returned (when they are included). The maximum limit is 50
        :type app_store_versions: int = None

        :param available_territories: maximum number of related availableTerritories returned (when they are included). The maximum limit is 50
        :type available_territories: int = None

        :param beta_app_localizations: maximum number of related betaAppLocalizations returned (when they are included). The maximum limit is 50
        :type beta_app_localizations: int = None

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :param game_center_enabled_versions: maximum number of related gameCenterEnabledVersions returned (when they are included). The maximum limit is 50
        :type game_center_enabled_versions: int = None

        :param in_app_purchases: maximum number of related inAppPurchases returned (when they are included). The maximum limit is 50
        :type in_app_purchases: int = None

        :param pre_release_versions: maximum number of related preReleaseVersions returned (when they are included). The maximum limit is 50
        :type pre_release_versions: int = None

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if app_clips and app_clips > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_clips: self._set_limit('appClips', app_clips)

        if app_infos and app_infos > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_infos: self._set_limit('appInfos', app_infos)

        if app_store_versions and app_store_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_store_versions: self._set_limit('appStoreVersions', app_store_versions)

        if available_territories and available_territories > 50:
            raise ValueError(f'The maximum limit is 50')
        if available_territories: self._set_limit('availableTerritories', available_territories)

        if beta_app_localizations and beta_app_localizations > 50:
            raise ValueError(f'The maximum limit is 50')
        if beta_app_localizations: self._set_limit('betaAppLocalizations', beta_app_localizations)

        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit is 50')
        if beta_groups: self._set_limit('betaGroups', beta_groups)

        if builds and builds > 50:
            raise ValueError(f'The maximum limit is 50')
        if builds: self._set_limit('builds', builds)

        if game_center_enabled_versions and game_center_enabled_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if game_center_enabled_versions: self._set_limit('gameCenterEnabledVersions', game_center_enabled_versions)

        if in_app_purchases and in_app_purchases > 50:
            raise ValueError(f'The maximum limit is 50')
        if in_app_purchases: self._set_limit('inAppPurchases', in_app_purchases)

        if pre_release_versions and pre_release_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if pre_release_versions: self._set_limit('preReleaseVersions', pre_release_versions)

        if prices and prices > 50:
            raise ValueError(f'The maximum limit is 50')
        if prices: self._set_limit('prices', prices)

        return self

    def get(self) -> AppsResponse:
        '''Get one or more resources.

        :returns: List of Apps
        :rtype: AppsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppsResponse.parse_obj(json)

class AppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}'

    @endpoint('/v1/apps/{id}/appClips')
    def app_clips(self) -> AppClipsOfAppEndpoint:
        return AppClipsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appInfos')
    def app_infos(self) -> AppInfosOfAppEndpoint:
        return AppInfosOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appStoreVersions')
    def app_store_versions(self) -> AppStoreVersionsOfAppEndpoint:
        return AppStoreVersionsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/availableTerritories')
    def available_territories(self) -> AvailableTerritoriesOfAppEndpoint:
        return AvailableTerritoriesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/betaAppLocalizations')
    def beta_app_localizations(self) -> BetaAppLocalizationsOfAppEndpoint:
        return BetaAppLocalizationsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/betaAppReviewDetail')
    def beta_app_review_detail(self) -> BetaAppReviewDetailOfAppEndpoint:
        return BetaAppReviewDetailOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/betaGroups')
    def beta_groups(self) -> BetaGroupsOfAppEndpoint:
        return BetaGroupsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/betaLicenseAgreement')
    def beta_license_agreement(self) -> BetaLicenseAgreementOfAppEndpoint:
        return BetaLicenseAgreementOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/builds')
    def builds(self) -> BuildsOfAppEndpoint:
        return BuildsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/ciProduct')
    def ci_product(self) -> CiProductOfAppEndpoint:
        return CiProductOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/endUserLicenseAgreement')
    def end_user_license_agreement(self) -> EndUserLicenseAgreementOfAppEndpoint:
        return EndUserLicenseAgreementOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/gameCenterEnabledVersions')
    def game_center_enabled_versions(self) -> GameCenterEnabledVersionsOfAppEndpoint:
        return GameCenterEnabledVersionsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/inAppPurchases')
    def in_app_purchases(self) -> InAppPurchasesOfAppEndpoint:
        return InAppPurchasesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/perfPowerMetrics')
    def perf_power_metrics(self) -> PerfPowerMetricsOfAppEndpoint:
        return PerfPowerMetricsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/preOrder')
    def pre_order(self) -> PreOrderOfAppEndpoint:
        return PreOrderOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/preReleaseVersions')
    def pre_release_versions(self) -> PreReleaseVersionsOfAppEndpoint:
        return PreReleaseVersionsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/prices')
    def prices(self) -> PricesOfAppEndpoint:
        return PricesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/betaTesters')
    def beta_testers_linkages(self) -> BetaTestersLinkagesOfAppEndpoint:
        return BetaTestersLinkagesOfAppEndpoint(self.id, self.session)
        
    def fields(self, *, app: Union[AppField, list[AppField]]=None, beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]]=None, beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]]=None, app_clip: Union[AppClipField, list[AppClipField]]=None, app_info: Union[AppInfoField, list[AppInfoField]]=None, beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, ci_product: Union[CiProductField, list[CiProductField]]=None, app_price: Union[AppPriceField, list[AppPriceField]]=None, app_pre_order: Union[AppPreOrderField, list[AppPreOrderField]]=None, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]]=None, end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, perf_power_metric: Union[PerfPowerMetricField, list[PerfPowerMetricField]]=None, build: Union[BuildField, list[BuildField]]=None) -> AppEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param beta_license_agreement: the fields to include for returned resources of type betaLicenseAgreements
        :type beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]] = None

        :param beta_app_review_detail: the fields to include for returned resources of type betaAppReviewDetails
        :type beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]] = None

        :param app_clip: the fields to include for returned resources of type appClips
        :type app_clip: Union[AppClipField, list[AppClipField]] = None

        :param app_info: the fields to include for returned resources of type appInfos
        :type app_info: Union[AppInfoField, list[AppInfoField]] = None

        :param beta_app_localization: the fields to include for returned resources of type betaAppLocalizations
        :type beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param app_price: the fields to include for returned resources of type appPrices
        :type app_price: Union[AppPriceField, list[AppPriceField]] = None

        :param app_pre_order: the fields to include for returned resources of type appPreOrders
        :type app_pre_order: Union[AppPreOrderField, list[AppPreOrderField]] = None

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :param game_center_enabled_version: the fields to include for returned resources of type gameCenterEnabledVersions
        :type game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]] = None

        :param end_user_license_agreement: the fields to include for returned resources of type endUserLicenseAgreements
        :type end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param perf_power_metric: the fields to include for returned resources of type perfPowerMetrics
        :type perf_power_metric: Union[PerfPowerMetricField, list[PerfPowerMetricField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if beta_license_agreement: self._set_fields('betaLicenseAgreements',beta_license_agreement if type(beta_license_agreement) is list else [beta_license_agreement])
        if beta_app_review_detail: self._set_fields('betaAppReviewDetails',beta_app_review_detail if type(beta_app_review_detail) is list else [beta_app_review_detail])
        if app_clip: self._set_fields('appClips',app_clip if type(app_clip) is list else [app_clip])
        if app_info: self._set_fields('appInfos',app_info if type(app_info) is list else [app_info])
        if beta_app_localization: self._set_fields('betaAppLocalizations',beta_app_localization if type(beta_app_localization) is list else [beta_app_localization])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if app_price: self._set_fields('appPrices',app_price if type(app_price) is list else [app_price])
        if app_pre_order: self._set_fields('appPreOrders',app_pre_order if type(app_pre_order) is list else [app_pre_order])
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        if game_center_enabled_version: self._set_fields('gameCenterEnabledVersions',game_center_enabled_version if type(game_center_enabled_version) is list else [game_center_enabled_version])
        if end_user_license_agreement: self._set_fields('endUserLicenseAgreements',end_user_license_agreement if type(end_user_license_agreement) is list else [end_user_license_agreement])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if perf_power_metric: self._set_fields('perfPowerMetrics',perf_power_metric if type(perf_power_metric) is list else [perf_power_metric])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        APP_CLIPS = 'appClips'
        APP_INFOS = 'appInfos'
        APP_STORE_VERSIONS = 'appStoreVersions'
        AVAILABLE_TERRITORIES = 'availableTerritories'
        BETA_APP_LOCALIZATIONS = 'betaAppLocalizations'
        BETA_APP_REVIEW_DETAIL = 'betaAppReviewDetail'
        BETA_GROUPS = 'betaGroups'
        BETA_LICENSE_AGREEMENT = 'betaLicenseAgreement'
        BUILDS = 'builds'
        CI_PRODUCT = 'ciProduct'
        END_USER_LICENSE_AGREEMENT = 'endUserLicenseAgreement'
        GAME_CENTER_ENABLED_VERSIONS = 'gameCenterEnabledVersions'
        IN_APP_PURCHASES = 'inAppPurchases'
        PRE_ORDER = 'preOrder'
        PRE_RELEASE_VERSIONS = 'preReleaseVersions'
        PRICES = 'prices'

    def include(self, relationship: Union[Include, list[Include]]) -> AppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_clips: int=None, app_infos: int=None, app_store_versions: int=None, available_territories: int=None, beta_app_localizations: int=None, beta_groups: int=None, builds: int=None, game_center_enabled_versions: int=None, in_app_purchases: int=None, pre_release_versions: int=None, prices: int=None) -> AppEndpoint:
        '''Number of included related resources to return.

        :param app_clips: maximum number of related appClips returned (when they are included). The maximum limit is 50
        :type app_clips: int = None

        :param app_infos: maximum number of related appInfos returned (when they are included). The maximum limit is 50
        :type app_infos: int = None

        :param app_store_versions: maximum number of related appStoreVersions returned (when they are included). The maximum limit is 50
        :type app_store_versions: int = None

        :param available_territories: maximum number of related availableTerritories returned (when they are included). The maximum limit is 50
        :type available_territories: int = None

        :param beta_app_localizations: maximum number of related betaAppLocalizations returned (when they are included). The maximum limit is 50
        :type beta_app_localizations: int = None

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :param game_center_enabled_versions: maximum number of related gameCenterEnabledVersions returned (when they are included). The maximum limit is 50
        :type game_center_enabled_versions: int = None

        :param in_app_purchases: maximum number of related inAppPurchases returned (when they are included). The maximum limit is 50
        :type in_app_purchases: int = None

        :param pre_release_versions: maximum number of related preReleaseVersions returned (when they are included). The maximum limit is 50
        :type pre_release_versions: int = None

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEndpoint
        '''
        if app_clips and app_clips > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_clips: self._set_limit('appClips', app_clips)

        if app_infos and app_infos > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_infos: self._set_limit('appInfos', app_infos)

        if app_store_versions and app_store_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_store_versions: self._set_limit('appStoreVersions', app_store_versions)

        if available_territories and available_territories > 50:
            raise ValueError(f'The maximum limit is 50')
        if available_territories: self._set_limit('availableTerritories', available_territories)

        if beta_app_localizations and beta_app_localizations > 50:
            raise ValueError(f'The maximum limit is 50')
        if beta_app_localizations: self._set_limit('betaAppLocalizations', beta_app_localizations)

        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit is 50')
        if beta_groups: self._set_limit('betaGroups', beta_groups)

        if builds and builds > 50:
            raise ValueError(f'The maximum limit is 50')
        if builds: self._set_limit('builds', builds)

        if game_center_enabled_versions and game_center_enabled_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if game_center_enabled_versions: self._set_limit('gameCenterEnabledVersions', game_center_enabled_versions)

        if in_app_purchases and in_app_purchases > 50:
            raise ValueError(f'The maximum limit is 50')
        if in_app_purchases: self._set_limit('inAppPurchases', in_app_purchases)

        if pre_release_versions and pre_release_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if pre_release_versions: self._set_limit('preReleaseVersions', pre_release_versions)

        if prices and prices > 50:
            raise ValueError(f'The maximum limit is 50')
        if prices: self._set_limit('prices', prices)

        return self

    def get(self) -> AppResponse:
        '''Get the resource.

        :returns: Single App
        :rtype: AppResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppResponse.parse_obj(json)

    def update(self, request: AppUpdateRequest) -> AppResponse:
        '''Modify the resource.

        :param request: App representation
        :type request: AppUpdateRequest

        :returns: Single App
        :rtype: AppResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppResponse.parse_obj(json)

class AppClipsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appClips'

    def fields(self, *, app_clip: Union[AppClipField, list[AppClipField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None) -> AppClipsOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_clip: the fields to include for returned resources of type appClips
        :type app_clip: Union[AppClipField, list[AppClipField]] = None

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipsOfAppEndpoint
        '''
        if app_clip: self._set_fields('appClips',app_clip if type(app_clip) is list else [app_clip])
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        return self
        
    class Include(StringEnum):
        APP_CLIP_DEFAULT_EXPERIENCES = 'appClipDefaultExperiences'

    def filter(self, *, bundle_id: Union[str, list[str]]=None) -> AppClipsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param bundle_id: filter by attribute 'bundleId'
        :type bundle_id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipsOfAppEndpoint
        '''
        if bundle_id: self._set_filter('bundleId', bundle_id if type(bundle_id) is list else [bundle_id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppClipsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_clip_default_experiences: int=None) -> AppClipsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_clip_default_experiences: maximum number of related appClipDefaultExperiences returned (when they are included). The maximum limit is 50
        :type app_clip_default_experiences: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if app_clip_default_experiences and app_clip_default_experiences > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_clip_default_experiences: self._set_limit('appClipDefaultExperiences', app_clip_default_experiences)

        return self

    def get(self) -> AppClipsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppClipsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipsResponse.parse_obj(json)

class AppInfosOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appInfos'

    def fields(self, *, app_info: Union[AppInfoField, list[AppInfoField]]=None, app_info_localization: Union[AppInfoLocalizationField, list[AppInfoLocalizationField]]=None) -> AppInfosOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_info: the fields to include for returned resources of type appInfos
        :type app_info: Union[AppInfoField, list[AppInfoField]] = None

        :param app_info_localization: the fields to include for returned resources of type appInfoLocalizations
        :type app_info_localization: Union[AppInfoLocalizationField, list[AppInfoLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppInfosOfAppEndpoint
        '''
        if app_info: self._set_fields('appInfos',app_info if type(app_info) is list else [app_info])
        if app_info_localization: self._set_fields('appInfoLocalizations',app_info_localization if type(app_info_localization) is list else [app_info_localization])
        return self
        
    class Include(StringEnum):
        APP_INFO_LOCALIZATIONS = 'appInfoLocalizations'

    def include(self, relationship: Union[Include, list[Include]]) -> AppInfosOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppInfosOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_info_localizations: int=None) -> AppInfosOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_info_localizations: maximum number of related appInfoLocalizations returned (when they are included). The maximum limit is 50
        :type app_info_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppInfosOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if app_info_localizations and app_info_localizations > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_info_localizations: self._set_limit('appInfoLocalizations', app_info_localizations)

        return self

    def get(self) -> AppInfosResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppInfosResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppInfosResponse.parse_obj(json)

class AppStoreVersionsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appStoreVersions'

    def fields(self, *, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None) -> AppStoreVersionsOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_store_version_localization: the fields to include for returned resources of type appStoreVersionLocalizations
        :type app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionsOfAppEndpoint
        '''
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_store_version_localization: self._set_fields('appStoreVersionLocalizations',app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION_LOCALIZATIONS = 'appStoreVersionLocalizations'

    def filter(self, *, app_store_state: Union[AppStoreVersionState, list[AppStoreVersionState]]=None, platform: Union[Platform, list[Platform]]=None, version_string: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> AppStoreVersionsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param app_store_state: filter by attribute 'appStoreState'
        :type app_store_state: Union[AppStoreVersionState, list[AppStoreVersionState]] = None

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param version_string: filter by attribute 'versionString'
        :type version_string: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionsOfAppEndpoint
        '''
        if app_store_state: self._set_filter('appStoreState', app_store_state if type(app_store_state) is list else [app_store_state])
        
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if version_string: self._set_filter('versionString', version_string if type(version_string) is list else [version_string])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_store_version_localizations: int=None) -> AppStoreVersionsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_store_version_localizations: maximum number of related appStoreVersionLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if app_store_version_localizations and app_store_version_localizations > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_store_version_localizations: self._set_limit('appStoreVersionLocalizations', app_store_version_localizations)

        return self

    def get(self) -> AppStoreVersionsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppStoreVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionsResponse.parse_obj(json)

class AvailableTerritoriesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/availableTerritories'

    def fields(self, *, territory: Union[TerritoryField, list[TerritoryField]]=None) -> AvailableTerritoriesOfAppEndpoint:
        '''Fields to return for included related types.

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AvailableTerritoriesOfAppEndpoint
        '''
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    def limit(self, number: int=None) -> AvailableTerritoriesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AvailableTerritoriesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> TerritoriesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: TerritoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return TerritoriesResponse.parse_obj(json)

class BetaAppLocalizationsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/betaAppLocalizations'

    def fields(self, *, beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]]=None) -> BetaAppLocalizationsOfAppEndpoint:
        '''Fields to return for included related types.

        :param beta_app_localization: the fields to include for returned resources of type betaAppLocalizations
        :type beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationsOfAppEndpoint
        '''
        if beta_app_localization: self._set_fields('betaAppLocalizations',beta_app_localization if type(beta_app_localization) is list else [beta_app_localization])
        return self
        
    def limit(self, number: int=None) -> BetaAppLocalizationsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaAppLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BetaAppLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppLocalizationsResponse.parse_obj(json)

class BetaAppReviewDetailOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/betaAppReviewDetail'

    def fields(self, *, beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]]=None) -> BetaAppReviewDetailOfAppEndpoint:
        '''Fields to return for included related types.

        :param beta_app_review_detail: the fields to include for returned resources of type betaAppReviewDetails
        :type beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewDetailOfAppEndpoint
        '''
        if beta_app_review_detail: self._set_fields('betaAppReviewDetails',beta_app_review_detail if type(beta_app_review_detail) is list else [beta_app_review_detail])
        return self
        
    def get(self) -> BetaAppReviewDetailResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: BetaAppReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppReviewDetailResponse.parse_obj(json)

class BetaGroupsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/betaGroups'

    def fields(self, *, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None) -> BetaGroupsOfAppEndpoint:
        '''Fields to return for included related types.

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsOfAppEndpoint
        '''
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        return self
        
    def limit(self, number: int=None) -> BetaGroupsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaGroupsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BetaGroupsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupsResponse.parse_obj(json)

class BetaLicenseAgreementOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/betaLicenseAgreement'

    def fields(self, *, beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]]=None) -> BetaLicenseAgreementOfAppEndpoint:
        '''Fields to return for included related types.

        :param beta_license_agreement: the fields to include for returned resources of type betaLicenseAgreements
        :type beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaLicenseAgreementOfAppEndpoint
        '''
        if beta_license_agreement: self._set_fields('betaLicenseAgreements',beta_license_agreement if type(beta_license_agreement) is list else [beta_license_agreement])
        return self
        
    def get(self) -> BetaLicenseAgreementResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: BetaLicenseAgreementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaLicenseAgreementResponse.parse_obj(json)

class BetaTestersLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaTesters'

    def delete(self, request: AppBetaTestersLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: AppBetaTestersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class BuildsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/builds'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildsOfAppEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfAppEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    def limit(self, number: int=None) -> BuildsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BuildsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BuildsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildsResponse.parse_obj(json)

class CiProductOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/ciProduct'

    def fields(self, *, ci_product: Union[CiProductField, list[CiProductField]]=None, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> CiProductOfAppEndpoint:
        '''Fields to return for included related types.

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiProductOfAppEndpoint
        '''
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    class Include(StringEnum):
        PRIMARY_REPOSITORIES = 'primaryRepositories'

    def include(self, relationship: Union[Include, list[Include]]) -> CiProductOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiProductOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, primary_repositories: int=None) -> CiProductOfAppEndpoint:
        '''Number of included related resources to return.

        :param primary_repositories: maximum number of related primaryRepositories returned (when they are included). The maximum limit is 50
        :type primary_repositories: int = None

        :returns: self
        :rtype: applaud.endpoints.CiProductOfAppEndpoint
        '''
        if primary_repositories and primary_repositories > 50:
            raise ValueError(f'The maximum limit is 50')
        if primary_repositories: self._set_limit('primaryRepositories', primary_repositories)

        return self

    def get(self) -> CiProductResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: CiProductResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiProductResponse.parse_obj(json)

class EndUserLicenseAgreementOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/endUserLicenseAgreement'

    def fields(self, *, end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]]=None) -> EndUserLicenseAgreementOfAppEndpoint:
        '''Fields to return for included related types.

        :param end_user_license_agreement: the fields to include for returned resources of type endUserLicenseAgreements
        :type end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]] = None

        :returns: self
        :rtype: applaud.endpoints.EndUserLicenseAgreementOfAppEndpoint
        '''
        if end_user_license_agreement: self._set_fields('endUserLicenseAgreements',end_user_license_agreement if type(end_user_license_agreement) is list else [end_user_license_agreement])
        return self
        
    def get(self) -> EndUserLicenseAgreementResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: EndUserLicenseAgreementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return EndUserLicenseAgreementResponse.parse_obj(json)

class GameCenterEnabledVersionsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/gameCenterEnabledVersions'

    def fields(self, *, game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]]=None) -> GameCenterEnabledVersionsOfAppEndpoint:
        '''Fields to return for included related types.

        :param game_center_enabled_version: the fields to include for returned resources of type gameCenterEnabledVersions
        :type game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsOfAppEndpoint
        '''
        if game_center_enabled_version: self._set_fields('gameCenterEnabledVersions',game_center_enabled_version if type(game_center_enabled_version) is list else [game_center_enabled_version])
        return self
        
    class Include(StringEnum):
        COMPATIBLE_VERSIONS = 'compatibleVersions'

    def filter(self, *, platform: Union[Platform, list[Platform]]=None, version_string: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterEnabledVersionsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param version_string: filter by attribute 'versionString'
        :type version_string: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsOfAppEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if version_string: self._set_filter('versionString', version_string if type(version_string) is list else [version_string])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterEnabledVersionsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, version_string: SortOrder=None) -> GameCenterEnabledVersionsOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsOfAppEndpoint
        '''
        if version_string: self.sort_expressions.append('versionString' if version_string == SortOrder.ASC else '-versionString')
        return self
        
    def limit(self, number: int=None, *, compatible_versions: int=None) -> GameCenterEnabledVersionsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param compatible_versions: maximum number of related compatibleVersions returned (when they are included). The maximum limit is 50
        :type compatible_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if compatible_versions and compatible_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if compatible_versions: self._set_limit('compatibleVersions', compatible_versions)

        return self

    def get(self) -> GameCenterEnabledVersionsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: GameCenterEnabledVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterEnabledVersionsResponse.parse_obj(json)

class InAppPurchasesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/inAppPurchases'

    def fields(self, *, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, app: Union[AppField, list[AppField]]=None) -> InAppPurchasesOfAppEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesOfAppEndpoint
        '''
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APPS = 'apps'

    def filter(self, *, in_app_purchase_type: Union[InAppPurchaseType, list[InAppPurchaseType]]=None, can_be_submitted: Union[str, list[str]]=None) -> InAppPurchasesOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param in_app_purchase_type: filter by attribute 'inAppPurchaseType'
        :type in_app_purchase_type: Union[InAppPurchaseType, list[InAppPurchaseType]] = None

        :param can_be_submitted: filter by canBeSubmitted
        :type can_be_submitted: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesOfAppEndpoint
        '''
        if in_app_purchase_type: self._set_filter('inAppPurchaseType', in_app_purchase_type if type(in_app_purchase_type) is list else [in_app_purchase_type])
        
        if can_be_submitted: self._set_filter('canBeSubmitted', can_be_submitted if type(can_be_submitted) is list else [can_be_submitted])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchasesOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, in_app_purchase_type: SortOrder=None, product_id: SortOrder=None, reference_name: SortOrder=None) -> InAppPurchasesOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesOfAppEndpoint
        '''
        if in_app_purchase_type: self.sort_expressions.append('inAppPurchaseType' if in_app_purchase_type == SortOrder.ASC else '-inAppPurchaseType')
        if product_id: self.sort_expressions.append('productId' if product_id == SortOrder.ASC else '-productId')
        if reference_name: self.sort_expressions.append('referenceName' if reference_name == SortOrder.ASC else '-referenceName')
        return self
        
    def limit(self, number: int=None, *, apps: int=None) -> InAppPurchasesOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param apps: maximum number of related apps returned (when they are included). The maximum limit is 50
        :type apps: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if apps and apps > 50:
            raise ValueError(f'The maximum limit is 50')
        if apps: self._set_limit('apps', apps)

        return self

    def get(self) -> InAppPurchasesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: InAppPurchasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasesResponse.parse_obj(json)

class PerfPowerMetricsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/perfPowerMetrics'

    def filter(self, *, device_type: Union[str, list[str]]=None, metric_type: Union[PerfPowerMetricType, list[PerfPowerMetricType]]=None, platform: Union[PerfPowerMetricPlatform, list[PerfPowerMetricPlatform]]=None) -> PerfPowerMetricsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param device_type: filter by attribute 'deviceType'
        :type device_type: Union[str, list[str]] = None

        :param metric_type: filter by attribute 'metricType'
        :type metric_type: Union[PerfPowerMetricType, list[PerfPowerMetricType]] = None

        :param platform: filter by attribute 'platform'
        :type platform: Union[PerfPowerMetricPlatform, list[PerfPowerMetricPlatform]] = None

        :returns: self
        :rtype: applaud.endpoints.PerfPowerMetricsOfAppEndpoint
        '''
        if device_type: self._set_filter('deviceType', device_type if type(device_type) is list else [device_type])
        
        if metric_type: self._set_filter('metricType', metric_type if type(metric_type) is list else [metric_type])
        
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        return self
        
    def get(self) -> PerfPowerMetricsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: PerfPowerMetricsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PerfPowerMetricsResponse.parse_obj(json)

class PreOrderOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/preOrder'

    def fields(self, *, app_pre_order: Union[AppPreOrderField, list[AppPreOrderField]]=None) -> PreOrderOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_pre_order: the fields to include for returned resources of type appPreOrders
        :type app_pre_order: Union[AppPreOrderField, list[AppPreOrderField]] = None

        :returns: self
        :rtype: applaud.endpoints.PreOrderOfAppEndpoint
        '''
        if app_pre_order: self._set_fields('appPreOrders',app_pre_order if type(app_pre_order) is list else [app_pre_order])
        return self
        
    def get(self) -> AppPreOrderResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppPreOrderResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPreOrderResponse.parse_obj(json)

class PreReleaseVersionsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/preReleaseVersions'

    def fields(self, *, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None) -> PreReleaseVersionsOfAppEndpoint:
        '''Fields to return for included related types.

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionsOfAppEndpoint
        '''
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        return self
        
    def limit(self, number: int=None) -> PreReleaseVersionsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> PreReleaseVersionsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: PreReleaseVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PreReleaseVersionsResponse.parse_obj(json)

class PricesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/prices'

    def fields(self, *, app_price: Union[AppPriceField, list[AppPriceField]]=None) -> PricesOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_price: the fields to include for returned resources of type appPrices
        :type app_price: Union[AppPriceField, list[AppPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfAppEndpoint
        '''
        if app_price: self._set_fields('appPrices',app_price if type(app_price) is list else [app_price])
        return self
        
    def limit(self, number: int=None) -> PricesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> AppPricesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppPricesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPricesResponse.parse_obj(json)

