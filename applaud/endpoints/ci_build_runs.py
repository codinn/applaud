from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiBuildRunsEndpoint(Endpoint):
    path = '/v1/ciBuildRuns'

    def create(self, request: CiBuildRunCreateRequest) -> CiBuildRunResponse:
        '''Create the resource.

        :param request: CiBuildRun representation
        :type request: CiBuildRunCreateRequest

        :returns: Single CiBuildRun
        :rtype: CiBuildRunResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return CiBuildRunResponse.parse_obj(json)

class CiBuildRunEndpoint(IDEndpoint):
    path = '/v1/ciBuildRuns/{id}'

    @endpoint('/v1/ciBuildRuns/{id}/actions')
    def actions(self) -> ActionsOfCiBuildRunEndpoint:
        return ActionsOfCiBuildRunEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildRuns/{id}/builds')
    def builds(self) -> BuildsOfCiBuildRunEndpoint:
        return BuildsOfCiBuildRunEndpoint(self.id, self.session)
        
    def fields(self, *, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None, ci_build_action: Union[CiBuildActionField, list[CiBuildActionField]]=None, build: Union[BuildField, list[BuildField]]=None) -> CiBuildRunEndpoint:
        '''Fields to return for included related types.

        :param ci_build_run: the fields to include for returned resources of type ciBuildRuns
        :type ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]] = None

        :param ci_build_action: the fields to include for returned resources of type ciBuildActions
        :type ci_build_action: Union[CiBuildActionField, list[CiBuildActionField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiBuildRunEndpoint
        '''
        if ci_build_run: self._set_fields('ciBuildRuns',ci_build_run if type(ci_build_run) is list else [ci_build_run])
        if ci_build_action: self._set_fields('ciBuildActions',ci_build_action if type(ci_build_action) is list else [ci_build_action])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILDS = 'builds'
        DESTINATION_BRANCH = 'destinationBranch'
        PRODUCT = 'product'
        PULL_REQUEST = 'pullRequest'
        SOURCE_BRANCH_OR_TAG = 'sourceBranchOrTag'
        WORKFLOW = 'workflow'

    def include(self, relationship: Union[Include, list[Include]]) -> CiBuildRunEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiBuildRunEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, builds: int=None) -> CiBuildRunEndpoint:
        '''Number of included related resources to return.

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.CiBuildRunEndpoint
        '''
        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        return self

    def get(self) -> CiBuildRunResponse:
        '''Get the resource.

        :returns: Single CiBuildRun
        :rtype: CiBuildRunResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildRunResponse.parse_obj(json)

class ActionsOfCiBuildRunEndpoint(IDEndpoint):
    path = '/v1/ciBuildRuns/{id}/actions'

    def fields(self, *, ci_build_action: Union[CiBuildActionField, list[CiBuildActionField]]=None) -> ActionsOfCiBuildRunEndpoint:
        '''Fields to return for included related types.

        :param ci_build_action: the fields to include for returned resources of type ciBuildActions
        :type ci_build_action: Union[CiBuildActionField, list[CiBuildActionField]] = None

        :returns: self
        :rtype: applaud.endpoints.ActionsOfCiBuildRunEndpoint
        '''
        if ci_build_action: self._set_fields('ciBuildActions',ci_build_action if type(ci_build_action) is list else [ci_build_action])
        return self
        
    def limit(self, number: int=None) -> ActionsOfCiBuildRunEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ActionsOfCiBuildRunEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiBuildActionsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: CiBuildActionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildActionsResponse.parse_obj(json)

class BuildsOfCiBuildRunEndpoint(IDEndpoint):
    path = '/v1/ciBuildRuns/{id}/builds'

    def fields(self, *, build_bundle: Union[BuildBundleField, list[BuildBundleField]]=None, build_icon: Union[BuildIconField, list[BuildIconField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BuildsOfCiBuildRunEndpoint:
        '''Fields to return for included related types.

        :param build_bundle: the fields to include for returned resources of type buildBundles
        :type build_bundle: Union[BuildBundleField, list[BuildBundleField]] = None

        :param build_icon: the fields to include for returned resources of type buildIcons
        :type build_icon: Union[BuildIconField, list[BuildIconField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :param beta_build_localization: the fields to include for returned resources of type betaBuildLocalizations
        :type beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
        '''
        if build_bundle: self._set_fields('buildBundles',build_bundle if type(build_bundle) is list else [build_bundle])
        if build_icon: self._set_fields('buildIcons',build_icon if type(build_icon) is list else [build_icon])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if beta_build_localization: self._set_fields('betaBuildLocalizations',beta_build_localization if type(beta_build_localization) is list else [beta_build_localization])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BETA_BUILD_LOCALIZATIONS = 'betaBuildLocalizations'
        BUILD_BUNDLES = 'buildBundles'
        ICONS = 'icons'
        INDIVIDUAL_TESTERS = 'individualTesters'

    def filter(self, *, beta_app_review_submission_beta_review_state: Union[BetaReviewState, list[BetaReviewState]]=None, build_audience_type: Union[BuildAudienceType, list[BuildAudienceType]]=None, expired: Union[str, list[str]]=None, pre_release_version_platform: Union[Platform, list[Platform]]=None, pre_release_version_version: Union[str, list[str]]=None, processing_state: Union[BuildProcessingState, list[BuildProcessingState]]=None, uses_non_exempt_encryption: Union[str, list[str]]=None, version: Union[str, list[str]]=None, app: Union[str, list[str]]=None, app_store_version: Union[str, list[str]]=None, beta_groups: Union[str, list[str]]=None, pre_release_version: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> BuildsOfCiBuildRunEndpoint:
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
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
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
        
    def include(self, relationship: Union[Include, list[Include]]) -> BuildsOfCiBuildRunEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, pre_release_version: SortOrder=None, uploaded_date: SortOrder=None, version: SortOrder=None) -> BuildsOfCiBuildRunEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
        '''
        if pre_release_version: self.sort_expressions.append('preReleaseVersion' if pre_release_version == SortOrder.ASC else '-preReleaseVersion')
        if uploaded_date: self.sort_expressions.append('uploadedDate' if uploaded_date == SortOrder.ASC else '-uploadedDate')
        if version: self.sort_expressions.append('version' if version == SortOrder.ASC else '-version')
        return self
        
    def limit(self, number: int=None, *, individual_testers: int=None, beta_build_localizations: int=None, icons: int=None, build_bundles: int=None) -> BuildsOfCiBuildRunEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param individual_testers: maximum number of related individualTesters returned (when they are included). The maximum limit is 50
        :type individual_testers: int = None

        :param beta_build_localizations: maximum number of related betaBuildLocalizations returned (when they are included). The maximum limit is 50
        :type beta_build_localizations: int = None

        :param icons: maximum number of related icons returned (when they are included). The maximum limit is 50
        :type icons: int = None

        :param build_bundles: maximum number of related buildBundles returned (when they are included). The maximum limit is 50
        :type build_bundles: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if individual_testers and individual_testers > 50:
            raise ValueError(f'The maximum limit of individual_testers is 50')
        if individual_testers: self._set_limit(individual_testers, 'individualTesters')

        if beta_build_localizations and beta_build_localizations > 50:
            raise ValueError(f'The maximum limit of beta_build_localizations is 50')
        if beta_build_localizations: self._set_limit(beta_build_localizations, 'betaBuildLocalizations')

        if icons and icons > 50:
            raise ValueError(f'The maximum limit of icons is 50')
        if icons: self._set_limit(icons, 'icons')

        if build_bundles and build_bundles > 50:
            raise ValueError(f'The maximum limit of build_bundles is 50')
        if build_bundles: self._set_limit(build_bundles, 'buildBundles')

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

