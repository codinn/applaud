from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BuildsEndpoint(Endpoint):
    path = '/v1/builds'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None, diagnostic_signature: Union[DiagnosticSignatureField, list[DiagnosticSignatureField]]=None, build_icon: Union[BuildIconField, list[BuildIconField]]=None, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, app: Union[AppField, list[AppField]]=None, perf_power_metric: Union[PerfPowerMetricField, list[PerfPowerMetricField]]=None) -> BuildsEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param diagnostic_signature: the fields to include for returned resources of type diagnosticSignatures
        :type diagnostic_signature: Union[DiagnosticSignatureField, list[DiagnosticSignatureField]] = None

        :param build_icon: the fields to include for returned resources of type buildIcons
        :type build_icon: Union[BuildIconField, list[BuildIconField]] = None

        :param build_beta_detail: the fields to include for returned resources of type buildBetaDetails
        :type build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]] = None

        :param beta_app_review_submission: the fields to include for returned resources of type betaAppReviewSubmissions
        :type beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param beta_build_localization: the fields to include for returned resources of type betaBuildLocalizations
        :type beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]] = None

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param perf_power_metric: the fields to include for returned resources of type perfPowerMetrics
        :type perf_power_metric: Union[PerfPowerMetricField, list[PerfPowerMetricField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if diagnostic_signature: self._set_fields('diagnosticSignatures',diagnostic_signature if type(diagnostic_signature) is list else [diagnostic_signature])
        if build_icon: self._set_fields('buildIcons',build_icon if type(build_icon) is list else [build_icon])
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        if beta_app_review_submission: self._set_fields('betaAppReviewSubmissions',beta_app_review_submission if type(beta_app_review_submission) is list else [beta_app_review_submission])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if beta_build_localization: self._set_fields('betaBuildLocalizations',beta_build_localization if type(beta_build_localization) is list else [beta_build_localization])
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if perf_power_metric: self._set_fields('perfPowerMetrics',perf_power_metric if type(perf_power_metric) is list else [perf_power_metric])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        APP_ENCRYPTION_DECLARATION = 'appEncryptionDeclaration'
        APP_STORE_VERSION = 'appStoreVersion'
        BETA_APP_REVIEW_SUBMISSION = 'betaAppReviewSubmission'
        BETA_BUILD_LOCALIZATIONS = 'betaBuildLocalizations'
        BUILD_BETA_DETAIL = 'buildBetaDetail'
        BUILD_BUNDLES = 'buildBundles'
        ICONS = 'icons'
        INDIVIDUAL_TESTERS = 'individualTesters'
        PRE_RELEASE_VERSION = 'preReleaseVersion'

    def filter(self, *, beta_app_review_submission_beta_review_state: Union[BetaReviewState, list[BetaReviewState]]=None, build_audience_type: Union[BuildAudienceType, list[BuildAudienceType]]=None, expired: Union[str, list[str]]=None, pre_release_version_platform: Union[Platform, list[Platform]]=None, pre_release_version_version: Union[str, list[str]]=None, processing_state: Union[BuildProcessingState, list[BuildProcessingState]]=None, uses_non_exempt_encryption: Union[str, list[str]]=None, version: Union[str, list[str]]=None, app: Union[str, list[str]]=None, app_store_version: Union[str, list[str]]=None, beta_groups: Union[str, list[str]]=None, pre_release_version: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> BuildsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param beta_app_review_submission_beta_review_state: filter by attribute 'betaAppReviewSubmission.betaReviewState'
        :type beta_app_review_submission_beta_review_state: Union[BetaReviewState, list[BetaReviewState]] = None

        :param build_audience_type: filter by attribute 'buildAudienceType'
        :type build_audience_type: Union[BuildAudienceType, list[BuildAudienceType]] = None

        :param expired: filter by attribute 'expired'
        :type expired: Union[str, list[str]] = None

        :param pre_release_version_platform: filter by attribute 'preReleaseVersion.platform'
        :type pre_release_version_platform: Union[Platform, list[Platform]] = None

        :param pre_release_version_version: filter by attribute 'preReleaseVersion.version'
        :type pre_release_version_version: Union[str, list[str]] = None

        :param processing_state: filter by attribute 'processingState'
        :type processing_state: Union[BuildProcessingState, list[BuildProcessingState]] = None

        :param uses_non_exempt_encryption: filter by attribute 'usesNonExemptEncryption'
        :type uses_non_exempt_encryption: Union[str, list[str]] = None

        :param version: filter by attribute 'version'
        :type version: Union[str, list[str]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :param app_store_version: filter by id(s) of related 'appStoreVersion'
        :type app_store_version: Union[str, list[str]] = None

        :param beta_groups: filter by id(s) of related 'betaGroups'
        :type beta_groups: Union[str, list[str]] = None

        :param pre_release_version: filter by id(s) of related 'preReleaseVersion'
        :type pre_release_version: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if beta_app_review_submission_beta_review_state: self._set_filter('betaAppReviewSubmission.betaReviewState', beta_app_review_submission_beta_review_state if type(beta_app_review_submission_beta_review_state) is list else [beta_app_review_submission_beta_review_state])
        
        if build_audience_type: self._set_filter('buildAudienceType', build_audience_type if type(build_audience_type) is list else [build_audience_type])
        
        if expired: self._set_filter('expired', expired if type(expired) is list else [expired])
        
        if pre_release_version_platform: self._set_filter('preReleaseVersion.platform', pre_release_version_platform if type(pre_release_version_platform) is list else [pre_release_version_platform])
        
        if pre_release_version_version: self._set_filter('preReleaseVersion.version', pre_release_version_version if type(pre_release_version_version) is list else [pre_release_version_version])
        
        if processing_state: self._set_filter('processingState', processing_state if type(processing_state) is list else [processing_state])
        
        if uses_non_exempt_encryption: self._set_filter('usesNonExemptEncryption', uses_non_exempt_encryption if type(uses_non_exempt_encryption) is list else [uses_non_exempt_encryption])
        
        if version: self._set_filter('version', version if type(version) is list else [version])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        if app_store_version: self._set_filter('appStoreVersion', app_store_version if type(app_store_version) is list else [app_store_version])
        
        if beta_groups: self._set_filter('betaGroups', beta_groups if type(beta_groups) is list else [beta_groups])
        
        if pre_release_version: self._set_filter('preReleaseVersion', pre_release_version if type(pre_release_version) is list else [pre_release_version])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BuildsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, pre_release_version: SortOrder=None, uploaded_date: SortOrder=None, version: SortOrder=None) -> BuildsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if pre_release_version: self.sort_expressions.append('preReleaseVersion' if pre_release_version == SortOrder.ASC else '-preReleaseVersion')
        if uploaded_date: self.sort_expressions.append('uploadedDate' if uploaded_date == SortOrder.ASC else '-uploadedDate')
        if version: self.sort_expressions.append('version' if version == SortOrder.ASC else '-version')
        return self
        
    def limit(self, number: int=None, *, beta_build_localizations: int=None, build_bundles: int=None, icons: int=None, individual_testers: int=None) -> BuildsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param beta_build_localizations: maximum number of related betaBuildLocalizations returned (when they are included). The maximum limit is 50
        :type beta_build_localizations: int = None

        :param build_bundles: maximum number of related buildBundles returned (when they are included). The maximum limit is 50
        :type build_bundles: int = None

        :param icons: maximum number of related icons returned (when they are included). The maximum limit is 50
        :type icons: int = None

        :param individual_testers: maximum number of related individualTesters returned (when they are included). The maximum limit is 50
        :type individual_testers: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if beta_build_localizations and beta_build_localizations > 50:
            raise ValueError(f'The maximum limit of beta_build_localizations is 50')
        if beta_build_localizations: self._set_limit(beta_build_localizations, 'betaBuildLocalizations')

        if build_bundles and build_bundles > 50:
            raise ValueError(f'The maximum limit of build_bundles is 50')
        if build_bundles: self._set_limit(build_bundles, 'buildBundles')

        if icons and icons > 50:
            raise ValueError(f'The maximum limit of icons is 50')
        if icons: self._set_limit(icons, 'icons')

        if individual_testers and individual_testers > 50:
            raise ValueError(f'The maximum limit of individual_testers is 50')
        if individual_testers: self._set_limit(individual_testers, 'individualTesters')

        return self

    def get(self) -> BuildsResponse:
        '''Get one or more resources.

        :returns: List of Builds
        :rtype: BuildsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildsResponse.parse_obj(json)

class BuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}'

    @endpoint('/v1/builds/{id}/app')
    def app(self) -> AppOfBuildEndpoint:
        return AppOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/appEncryptionDeclaration')
    def app_encryption_declaration(self) -> AppEncryptionDeclarationOfBuildEndpoint:
        return AppEncryptionDeclarationOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/appStoreVersion')
    def app_store_version(self) -> AppStoreVersionOfBuildEndpoint:
        return AppStoreVersionOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/betaAppReviewSubmission')
    def beta_app_review_submission(self) -> BetaAppReviewSubmissionOfBuildEndpoint:
        return BetaAppReviewSubmissionOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/betaBuildLocalizations')
    def beta_build_localizations(self) -> BetaBuildLocalizationsOfBuildEndpoint:
        return BetaBuildLocalizationsOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/buildBetaDetail')
    def build_beta_detail(self) -> BuildBetaDetailOfBuildEndpoint:
        return BuildBetaDetailOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/diagnosticSignatures')
    def diagnostic_signatures(self) -> DiagnosticSignaturesOfBuildEndpoint:
        return DiagnosticSignaturesOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/icons')
    def icons(self) -> IconsOfBuildEndpoint:
        return IconsOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/individualTesters')
    def individual_testers(self) -> IndividualTestersOfBuildEndpoint:
        return IndividualTestersOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/perfPowerMetrics')
    def perf_power_metrics(self) -> PerfPowerMetricsOfBuildEndpoint:
        return PerfPowerMetricsOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/preReleaseVersion')
    def pre_release_version(self) -> PreReleaseVersionOfBuildEndpoint:
        return PreReleaseVersionOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/appEncryptionDeclaration')
    def app_encryption_declaration_linkage(self) -> AppEncryptionDeclarationLinkageOfBuildEndpoint:
        return AppEncryptionDeclarationLinkageOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/betaGroups')
    def beta_groups_linkages(self) -> BetaGroupsLinkagesOfBuildEndpoint:
        return BetaGroupsLinkagesOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/individualTesters')
    def individual_testers_linkages(self) -> IndividualTestersLinkagesOfBuildEndpoint:
        return IndividualTestersLinkagesOfBuildEndpoint(self.id, self.session)
        
    def fields(self, *, build: Union[BuildField, list[BuildField]]=None, diagnostic_signature: Union[DiagnosticSignatureField, list[DiagnosticSignatureField]]=None, build_icon: Union[BuildIconField, list[BuildIconField]]=None, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, app: Union[AppField, list[AppField]]=None, perf_power_metric: Union[PerfPowerMetricField, list[PerfPowerMetricField]]=None) -> BuildEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param diagnostic_signature: the fields to include for returned resources of type diagnosticSignatures
        :type diagnostic_signature: Union[DiagnosticSignatureField, list[DiagnosticSignatureField]] = None

        :param build_icon: the fields to include for returned resources of type buildIcons
        :type build_icon: Union[BuildIconField, list[BuildIconField]] = None

        :param build_beta_detail: the fields to include for returned resources of type buildBetaDetails
        :type build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]] = None

        :param beta_app_review_submission: the fields to include for returned resources of type betaAppReviewSubmissions
        :type beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param beta_build_localization: the fields to include for returned resources of type betaBuildLocalizations
        :type beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]] = None

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param perf_power_metric: the fields to include for returned resources of type perfPowerMetrics
        :type perf_power_metric: Union[PerfPowerMetricField, list[PerfPowerMetricField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if diagnostic_signature: self._set_fields('diagnosticSignatures',diagnostic_signature if type(diagnostic_signature) is list else [diagnostic_signature])
        if build_icon: self._set_fields('buildIcons',build_icon if type(build_icon) is list else [build_icon])
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        if beta_app_review_submission: self._set_fields('betaAppReviewSubmissions',beta_app_review_submission if type(beta_app_review_submission) is list else [beta_app_review_submission])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if beta_build_localization: self._set_fields('betaBuildLocalizations',beta_build_localization if type(beta_build_localization) is list else [beta_build_localization])
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if perf_power_metric: self._set_fields('perfPowerMetrics',perf_power_metric if type(perf_power_metric) is list else [perf_power_metric])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        APP_ENCRYPTION_DECLARATION = 'appEncryptionDeclaration'
        APP_STORE_VERSION = 'appStoreVersion'
        BETA_APP_REVIEW_SUBMISSION = 'betaAppReviewSubmission'
        BETA_BUILD_LOCALIZATIONS = 'betaBuildLocalizations'
        BUILD_BETA_DETAIL = 'buildBetaDetail'
        BUILD_BUNDLES = 'buildBundles'
        ICONS = 'icons'
        INDIVIDUAL_TESTERS = 'individualTesters'
        PRE_RELEASE_VERSION = 'preReleaseVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> BuildEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, beta_build_localizations: int=None, build_bundles: int=None, icons: int=None, individual_testers: int=None) -> BuildEndpoint:
        '''Number of included related resources to return.

        :param beta_build_localizations: maximum number of related betaBuildLocalizations returned (when they are included). The maximum limit is 50
        :type beta_build_localizations: int = None

        :param build_bundles: maximum number of related buildBundles returned (when they are included). The maximum limit is 50
        :type build_bundles: int = None

        :param icons: maximum number of related icons returned (when they are included). The maximum limit is 50
        :type icons: int = None

        :param individual_testers: maximum number of related individualTesters returned (when they are included). The maximum limit is 50
        :type individual_testers: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildEndpoint
        '''
        if beta_build_localizations and beta_build_localizations > 50:
            raise ValueError(f'The maximum limit of beta_build_localizations is 50')
        if beta_build_localizations: self._set_limit(beta_build_localizations, 'betaBuildLocalizations')

        if build_bundles and build_bundles > 50:
            raise ValueError(f'The maximum limit of build_bundles is 50')
        if build_bundles: self._set_limit(build_bundles, 'buildBundles')

        if icons and icons > 50:
            raise ValueError(f'The maximum limit of icons is 50')
        if icons: self._set_limit(icons, 'icons')

        if individual_testers and individual_testers > 50:
            raise ValueError(f'The maximum limit of individual_testers is 50')
        if individual_testers: self._set_limit(individual_testers, 'individualTesters')

        return self

    def get(self) -> BuildResponse:
        '''Get the resource.

        :returns: Single Build
        :rtype: BuildResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildResponse.parse_obj(json)

    def update(self, request: BuildUpdateRequest) -> BuildResponse:
        '''Modify the resource.

        :param request: Build representation
        :type request: BuildUpdateRequest

        :returns: Single Build
        :rtype: BuildResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BuildResponse.parse_obj(json)

class AppOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppOfBuildEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfBuildEndpoint
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

class AppEncryptionDeclarationLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/appEncryptionDeclaration'

    def get(self) -> BuildAppEncryptionDeclarationLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BuildAppEncryptionDeclarationLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildAppEncryptionDeclarationLinkageResponse.parse_obj(json)

    def update(self, request: BuildAppEncryptionDeclarationLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: BuildAppEncryptionDeclarationLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class AppEncryptionDeclarationOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/appEncryptionDeclaration'

    def fields(self, *, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None) -> AppEncryptionDeclarationOfBuildEndpoint:
        '''Fields to return for included related types.

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationOfBuildEndpoint
        '''
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        return self
        
    def get(self) -> AppEncryptionDeclarationResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppEncryptionDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEncryptionDeclarationResponse.parse_obj(json)

class AppStoreVersionOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/appStoreVersion'

    def fields(self, *, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None) -> AppStoreVersionOfBuildEndpoint:
        '''Fields to return for included related types.

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionOfBuildEndpoint
        '''
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        return self
        
    def get(self) -> AppStoreVersionResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppStoreVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionResponse.parse_obj(json)

class BetaAppReviewSubmissionOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/betaAppReviewSubmission'

    def fields(self, *, beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]]=None) -> BetaAppReviewSubmissionOfBuildEndpoint:
        '''Fields to return for included related types.

        :param beta_app_review_submission: the fields to include for returned resources of type betaAppReviewSubmissions
        :type beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewSubmissionOfBuildEndpoint
        '''
        if beta_app_review_submission: self._set_fields('betaAppReviewSubmissions',beta_app_review_submission if type(beta_app_review_submission) is list else [beta_app_review_submission])
        return self
        
    def get(self) -> BetaAppReviewSubmissionResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: BetaAppReviewSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppReviewSubmissionResponse.parse_obj(json)

class BetaBuildLocalizationsOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/betaBuildLocalizations'

    def fields(self, *, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None) -> BetaBuildLocalizationsOfBuildEndpoint:
        '''Fields to return for included related types.

        :param beta_build_localization: the fields to include for returned resources of type betaBuildLocalizations
        :type beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationsOfBuildEndpoint
        '''
        if beta_build_localization: self._set_fields('betaBuildLocalizations',beta_build_localization if type(beta_build_localization) is list else [beta_build_localization])
        return self
        
    def limit(self, number: int=None) -> BetaBuildLocalizationsOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationsOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaBuildLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BetaBuildLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaBuildLocalizationsResponse.parse_obj(json)

class BetaGroupsLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/betaGroups'

    def create(self, request: BuildBetaGroupsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: BuildBetaGroupsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: BuildBetaGroupsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BuildBetaGroupsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class BuildBetaDetailOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/buildBetaDetail'

    def fields(self, *, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None) -> BuildBetaDetailOfBuildEndpoint:
        '''Fields to return for included related types.

        :param build_beta_detail: the fields to include for returned resources of type buildBetaDetails
        :type build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailOfBuildEndpoint
        '''
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        return self
        
    def get(self) -> BuildBetaDetailResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: BuildBetaDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildBetaDetailResponse.parse_obj(json)

class DiagnosticSignaturesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/diagnosticSignatures'

    def fields(self, *, diagnostic_signature: Union[DiagnosticSignatureField, list[DiagnosticSignatureField]]=None) -> DiagnosticSignaturesOfBuildEndpoint:
        '''Fields to return for included related types.

        :param diagnostic_signature: the fields to include for returned resources of type diagnosticSignatures
        :type diagnostic_signature: Union[DiagnosticSignatureField, list[DiagnosticSignatureField]] = None

        :returns: self
        :rtype: applaud.endpoints.DiagnosticSignaturesOfBuildEndpoint
        '''
        if diagnostic_signature: self._set_fields('diagnosticSignatures',diagnostic_signature if type(diagnostic_signature) is list else [diagnostic_signature])
        return self
        
    def filter(self, *, diagnostic_type: Union[DiagnosticType, list[DiagnosticType]]=None) -> DiagnosticSignaturesOfBuildEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param diagnostic_type: filter by attribute 'diagnosticType'
        :type diagnostic_type: Union[DiagnosticType, list[DiagnosticType]] = None

        :returns: self
        :rtype: applaud.endpoints.DiagnosticSignaturesOfBuildEndpoint
        '''
        if diagnostic_type: self._set_filter('diagnosticType', diagnostic_type if type(diagnostic_type) is list else [diagnostic_type])
        
        return self
        
    def limit(self, number: int=None) -> DiagnosticSignaturesOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DiagnosticSignaturesOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> DiagnosticSignaturesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: DiagnosticSignaturesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return DiagnosticSignaturesResponse.parse_obj(json)

class IconsOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/icons'

    def fields(self, *, build_icon: Union[BuildIconField, list[BuildIconField]]=None) -> IconsOfBuildEndpoint:
        '''Fields to return for included related types.

        :param build_icon: the fields to include for returned resources of type buildIcons
        :type build_icon: Union[BuildIconField, list[BuildIconField]] = None

        :returns: self
        :rtype: applaud.endpoints.IconsOfBuildEndpoint
        '''
        if build_icon: self._set_fields('buildIcons',build_icon if type(build_icon) is list else [build_icon])
        return self
        
    def limit(self, number: int=None) -> IconsOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IconsOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildIconsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BuildIconsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildIconsResponse.parse_obj(json)

class IndividualTestersLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/individualTesters'

    def limit(self, number: int=None) -> IndividualTestersLinkagesOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IndividualTestersLinkagesOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildIndividualTestersLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BuildIndividualTestersLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildIndividualTestersLinkagesResponse.parse_obj(json)

    def create(self, request: BuildIndividualTestersLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: BuildIndividualTestersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: BuildIndividualTestersLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BuildIndividualTestersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class IndividualTestersOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/individualTesters'

    def fields(self, *, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None) -> IndividualTestersOfBuildEndpoint:
        '''Fields to return for included related types.

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :returns: self
        :rtype: applaud.endpoints.IndividualTestersOfBuildEndpoint
        '''
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        return self
        
    def limit(self, number: int=None) -> IndividualTestersOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IndividualTestersOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaTestersResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BetaTestersResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaTestersResponse.parse_obj(json)

class PerfPowerMetricsOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/perfPowerMetrics'

    def filter(self, *, device_type: Union[str, list[str]]=None, metric_type: Union[PerfPowerMetricType, list[PerfPowerMetricType]]=None, platform: Union[PerfPowerMetricPlatform, list[PerfPowerMetricPlatform]]=None) -> PerfPowerMetricsOfBuildEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param device_type: filter by attribute 'deviceType'
        :type device_type: Union[str, list[str]] = None

        :param metric_type: filter by attribute 'metricType'
        :type metric_type: Union[PerfPowerMetricType, list[PerfPowerMetricType]] = None

        :param platform: filter by attribute 'platform'
        :type platform: Union[PerfPowerMetricPlatform, list[PerfPowerMetricPlatform]] = None

        :returns: self
        :rtype: applaud.endpoints.PerfPowerMetricsOfBuildEndpoint
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

class PreReleaseVersionOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/preReleaseVersion'

    def fields(self, *, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None) -> PreReleaseVersionOfBuildEndpoint:
        '''Fields to return for included related types.

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionOfBuildEndpoint
        '''
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        return self
        
    def get(self) -> PrereleaseVersionResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: PrereleaseVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PrereleaseVersionResponse.parse_obj(json)

