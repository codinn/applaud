# This file is autogenerated by `applaudgen` from `app_store_connect_api.json`.
# Do not modify this file -- YOUR CHANGES WILL BE ERASED!

import datetime
from .endpoints import *
import requests
from authlib.jose import jwt

class Connection:
    """
    Connection to the App Store Connect.
    """

    base_url = 'https://api.appstoreconnect.apple.com'

    def __init__(self, issuer_id: str, key_id: str, private_key: str):
        self._s = requests.Session()
        self.key_id = key_id
        self.issuer_id = issuer_id
        self.private_key = private_key

        self.__gen_auth_header()

    def __gen_auth_header(self):
        # Creates a token that lives for 20 minutes
        self._auth_header_timestamp = datetime.datetime.utcnow()
        expiry = datetime.datetime.utcnow() + datetime.timedelta(minutes=20)

        token = jwt.encode(
            {
                "alg": "ES256",
                "kid": self.key_id,
                "typ": "JWT"
            },
            {
                "iss": self.issuer_id,
                "exp": expiry,
                "aud": "appstoreconnect-v1"
            },
            self.private_key
        )

        # Create an Authorization header value with bearer token (JWT).
        # The token is set to expire in 20 minutes, and is used for all App Store
        # Connect API calls.
        self._s.headers['Authorization'] = 'Bearer ' + token.decode()
    
    @property
    def session(self):
        expiring = self._auth_header_timestamp + datetime.timedelta(minutes=15) < datetime.datetime.utcnow()
        # generate a new token every 15 minutes
        if expiring or ('Authorization' not in self._s.headers):
            self.__gen_auth_header()

        return self._s

    def generic_endpoint(self, url: str) -> GenericEndpoint:
        return GenericEndpoint(self.session, url)

    # Shortcuts for root endpoints

    @endpoint('/v1/ageRatingDeclarations/{id}')
    def age_rating_declaration(self, id: str) -> AgeRatingDeclarationEndpoint:
        return AgeRatingDeclarationEndpoint(id, self.session)
    
    @endpoint('/v1/appCategories')
    def app_categories(self) -> AppCategoriesEndpoint:
        return AppCategoriesEndpoint(self.session)
    
    @endpoint('/v1/appCategories/{id}')
    def app_category(self, id: str) -> AppCategoryEndpoint:
        return AppCategoryEndpoint(id, self.session)
    
    @endpoint('/v1/appClipAdvancedExperienceImages')
    def app_clip_advanced_experience_images(self) -> AppClipAdvancedExperienceImagesEndpoint:
        return AppClipAdvancedExperienceImagesEndpoint(self.session)
    
    @endpoint('/v1/appClipAdvancedExperienceImages/{id}')
    def app_clip_advanced_experience_image(self, id: str) -> AppClipAdvancedExperienceImageEndpoint:
        return AppClipAdvancedExperienceImageEndpoint(id, self.session)
    
    @endpoint('/v1/appClipAdvancedExperiences')
    def app_clip_advanced_experiences(self) -> AppClipAdvancedExperiencesEndpoint:
        return AppClipAdvancedExperiencesEndpoint(self.session)
    
    @endpoint('/v1/appClipAdvancedExperiences/{id}')
    def app_clip_advanced_experience(self, id: str) -> AppClipAdvancedExperienceEndpoint:
        return AppClipAdvancedExperienceEndpoint(id, self.session)
    
    @endpoint('/v1/appClipAppStoreReviewDetails')
    def app_clip_app_store_review_details(self) -> AppClipAppStoreReviewDetailsEndpoint:
        return AppClipAppStoreReviewDetailsEndpoint(self.session)
    
    @endpoint('/v1/appClipAppStoreReviewDetails/{id}')
    def app_clip_app_store_review_detail(self, id: str) -> AppClipAppStoreReviewDetailEndpoint:
        return AppClipAppStoreReviewDetailEndpoint(id, self.session)
    
    @endpoint('/v1/appClipDefaultExperienceLocalizations')
    def app_clip_default_experience_localizations(self) -> AppClipDefaultExperienceLocalizationsEndpoint:
        return AppClipDefaultExperienceLocalizationsEndpoint(self.session)
    
    @endpoint('/v1/appClipDefaultExperienceLocalizations/{id}')
    def app_clip_default_experience_localization(self, id: str) -> AppClipDefaultExperienceLocalizationEndpoint:
        return AppClipDefaultExperienceLocalizationEndpoint(id, self.session)
    
    @endpoint('/v1/appClipDefaultExperiences')
    def app_clip_default_experiences(self) -> AppClipDefaultExperiencesEndpoint:
        return AppClipDefaultExperiencesEndpoint(self.session)
    
    @endpoint('/v1/appClipDefaultExperiences/{id}')
    def app_clip_default_experience(self, id: str) -> AppClipDefaultExperienceEndpoint:
        return AppClipDefaultExperienceEndpoint(id, self.session)
    
    @endpoint('/v1/appClipHeaderImages')
    def app_clip_header_images(self) -> AppClipHeaderImagesEndpoint:
        return AppClipHeaderImagesEndpoint(self.session)
    
    @endpoint('/v1/appClipHeaderImages/{id}')
    def app_clip_header_image(self, id: str) -> AppClipHeaderImageEndpoint:
        return AppClipHeaderImageEndpoint(id, self.session)
    
    @endpoint('/v1/appClips/{id}')
    def app_clip(self, id: str) -> AppClipEndpoint:
        return AppClipEndpoint(id, self.session)
    
    @endpoint('/v1/appEncryptionDeclarations')
    def app_encryption_declarations(self) -> AppEncryptionDeclarationsEndpoint:
        return AppEncryptionDeclarationsEndpoint(self.session)
    
    @endpoint('/v1/appEncryptionDeclarations/{id}')
    def app_encryption_declaration(self, id: str) -> AppEncryptionDeclarationEndpoint:
        return AppEncryptionDeclarationEndpoint(id, self.session)
    
    @endpoint('/v1/appInfoLocalizations')
    def app_info_localizations(self) -> AppInfoLocalizationsEndpoint:
        return AppInfoLocalizationsEndpoint(self.session)
    
    @endpoint('/v1/appInfoLocalizations/{id}')
    def app_info_localization(self, id: str) -> AppInfoLocalizationEndpoint:
        return AppInfoLocalizationEndpoint(id, self.session)
    
    @endpoint('/v1/appInfos/{id}')
    def app_info(self, id: str) -> AppInfoEndpoint:
        return AppInfoEndpoint(id, self.session)
    
    @endpoint('/v1/appPreOrders')
    def app_pre_orders(self) -> AppPreOrdersEndpoint:
        return AppPreOrdersEndpoint(self.session)
    
    @endpoint('/v1/appPreOrders/{id}')
    def app_pre_order(self, id: str) -> AppPreOrderEndpoint:
        return AppPreOrderEndpoint(id, self.session)
    
    @endpoint('/v1/appPreviewSets')
    def app_preview_sets(self) -> AppPreviewSetsEndpoint:
        return AppPreviewSetsEndpoint(self.session)
    
    @endpoint('/v1/appPreviewSets/{id}')
    def app_preview_set(self, id: str) -> AppPreviewSetEndpoint:
        return AppPreviewSetEndpoint(id, self.session)
    
    @endpoint('/v1/appPreviews')
    def app_previews(self) -> AppPreviewsEndpoint:
        return AppPreviewsEndpoint(self.session)
    
    @endpoint('/v1/appPreviews/{id}')
    def app_preview(self, id: str) -> AppPreviewEndpoint:
        return AppPreviewEndpoint(id, self.session)
    
    @endpoint('/v1/appPricePoints')
    def app_price_points(self) -> AppPricePointsEndpoint:
        return AppPricePointsEndpoint(self.session)
    
    @endpoint('/v1/appPricePoints/{id}')
    def app_price_point(self, id: str) -> AppPricePointEndpoint:
        return AppPricePointEndpoint(id, self.session)
    
    @endpoint('/v1/appPriceTiers')
    def app_price_tiers(self) -> AppPriceTiersEndpoint:
        return AppPriceTiersEndpoint(self.session)
    
    @endpoint('/v1/appPriceTiers/{id}')
    def app_price_tier(self, id: str) -> AppPriceTierEndpoint:
        return AppPriceTierEndpoint(id, self.session)
    
    @endpoint('/v1/appPrices/{id}')
    def app_price(self, id: str) -> AppPriceEndpoint:
        return AppPriceEndpoint(id, self.session)
    
    @endpoint('/v1/appScreenshotSets')
    def app_screenshot_sets(self) -> AppScreenshotSetsEndpoint:
        return AppScreenshotSetsEndpoint(self.session)
    
    @endpoint('/v1/appScreenshotSets/{id}')
    def app_screenshot_set(self, id: str) -> AppScreenshotSetEndpoint:
        return AppScreenshotSetEndpoint(id, self.session)
    
    @endpoint('/v1/appScreenshots')
    def app_screenshots(self) -> AppScreenshotsEndpoint:
        return AppScreenshotsEndpoint(self.session)
    
    @endpoint('/v1/appScreenshots/{id}')
    def app_screenshot(self, id: str) -> AppScreenshotEndpoint:
        return AppScreenshotEndpoint(id, self.session)
    
    @endpoint('/v1/appStoreReviewAttachments')
    def app_store_review_attachments(self) -> AppStoreReviewAttachmentsEndpoint:
        return AppStoreReviewAttachmentsEndpoint(self.session)
    
    @endpoint('/v1/appStoreReviewAttachments/{id}')
    def app_store_review_attachment(self, id: str) -> AppStoreReviewAttachmentEndpoint:
        return AppStoreReviewAttachmentEndpoint(id, self.session)
    
    @endpoint('/v1/appStoreReviewDetails')
    def app_store_review_details(self) -> AppStoreReviewDetailsEndpoint:
        return AppStoreReviewDetailsEndpoint(self.session)
    
    @endpoint('/v1/appStoreReviewDetails/{id}')
    def app_store_review_detail(self, id: str) -> AppStoreReviewDetailEndpoint:
        return AppStoreReviewDetailEndpoint(id, self.session)
    
    @endpoint('/v1/appStoreVersionLocalizations')
    def app_store_version_localizations(self) -> AppStoreVersionLocalizationsEndpoint:
        return AppStoreVersionLocalizationsEndpoint(self.session)
    
    @endpoint('/v1/appStoreVersionLocalizations/{id}')
    def app_store_version_localization(self, id: str) -> AppStoreVersionLocalizationEndpoint:
        return AppStoreVersionLocalizationEndpoint(id, self.session)
    
    @endpoint('/v1/appStoreVersionPhasedReleases')
    def app_store_version_phased_releases(self) -> AppStoreVersionPhasedReleasesEndpoint:
        return AppStoreVersionPhasedReleasesEndpoint(self.session)
    
    @endpoint('/v1/appStoreVersionPhasedReleases/{id}')
    def app_store_version_phased_release(self, id: str) -> AppStoreVersionPhasedReleaseEndpoint:
        return AppStoreVersionPhasedReleaseEndpoint(id, self.session)
    
    @endpoint('/v1/appStoreVersionReleaseRequests')
    def app_store_version_release_requests(self) -> AppStoreVersionReleaseRequestsEndpoint:
        return AppStoreVersionReleaseRequestsEndpoint(self.session)
    
    @endpoint('/v1/appStoreVersionSubmissions')
    def app_store_version_submissions(self) -> AppStoreVersionSubmissionsEndpoint:
        return AppStoreVersionSubmissionsEndpoint(self.session)
    
    @endpoint('/v1/appStoreVersionSubmissions/{id}')
    def app_store_version_submission(self, id: str) -> AppStoreVersionSubmissionEndpoint:
        return AppStoreVersionSubmissionEndpoint(id, self.session)
    
    @endpoint('/v1/appStoreVersions')
    def app_store_versions(self) -> AppStoreVersionsEndpoint:
        return AppStoreVersionsEndpoint(self.session)
    
    @endpoint('/v1/appStoreVersions/{id}')
    def app_store_version(self, id: str) -> AppStoreVersionEndpoint:
        return AppStoreVersionEndpoint(id, self.session)
    
    @endpoint('/v1/apps')
    def apps(self) -> AppsEndpoint:
        return AppsEndpoint(self.session)
    
    @endpoint('/v1/apps/{id}')
    def app(self, id: str) -> AppEndpoint:
        return AppEndpoint(id, self.session)
    
    @endpoint('/v1/betaAppClipInvocationLocalizations')
    def beta_app_clip_invocation_localizations(self) -> BetaAppClipInvocationLocalizationsEndpoint:
        return BetaAppClipInvocationLocalizationsEndpoint(self.session)
    
    @endpoint('/v1/betaAppClipInvocationLocalizations/{id}')
    def beta_app_clip_invocation_localization(self, id: str) -> BetaAppClipInvocationLocalizationEndpoint:
        return BetaAppClipInvocationLocalizationEndpoint(id, self.session)
    
    @endpoint('/v1/betaAppClipInvocations')
    def beta_app_clip_invocations(self) -> BetaAppClipInvocationsEndpoint:
        return BetaAppClipInvocationsEndpoint(self.session)
    
    @endpoint('/v1/betaAppClipInvocations/{id}')
    def beta_app_clip_invocation(self, id: str) -> BetaAppClipInvocationEndpoint:
        return BetaAppClipInvocationEndpoint(id, self.session)
    
    @endpoint('/v1/betaAppLocalizations')
    def beta_app_localizations(self) -> BetaAppLocalizationsEndpoint:
        return BetaAppLocalizationsEndpoint(self.session)
    
    @endpoint('/v1/betaAppLocalizations/{id}')
    def beta_app_localization(self, id: str) -> BetaAppLocalizationEndpoint:
        return BetaAppLocalizationEndpoint(id, self.session)
    
    @endpoint('/v1/betaAppReviewDetails')
    def beta_app_review_details(self) -> BetaAppReviewDetailsEndpoint:
        return BetaAppReviewDetailsEndpoint(self.session)
    
    @endpoint('/v1/betaAppReviewDetails/{id}')
    def beta_app_review_detail(self, id: str) -> BetaAppReviewDetailEndpoint:
        return BetaAppReviewDetailEndpoint(id, self.session)
    
    @endpoint('/v1/betaAppReviewSubmissions')
    def beta_app_review_submissions(self) -> BetaAppReviewSubmissionsEndpoint:
        return BetaAppReviewSubmissionsEndpoint(self.session)
    
    @endpoint('/v1/betaAppReviewSubmissions/{id}')
    def beta_app_review_submission(self, id: str) -> BetaAppReviewSubmissionEndpoint:
        return BetaAppReviewSubmissionEndpoint(id, self.session)
    
    @endpoint('/v1/betaBuildLocalizations')
    def beta_build_localizations(self) -> BetaBuildLocalizationsEndpoint:
        return BetaBuildLocalizationsEndpoint(self.session)
    
    @endpoint('/v1/betaBuildLocalizations/{id}')
    def beta_build_localization(self, id: str) -> BetaBuildLocalizationEndpoint:
        return BetaBuildLocalizationEndpoint(id, self.session)
    
    @endpoint('/v1/betaGroups')
    def beta_groups(self) -> BetaGroupsEndpoint:
        return BetaGroupsEndpoint(self.session)
    
    @endpoint('/v1/betaGroups/{id}')
    def beta_group(self, id: str) -> BetaGroupEndpoint:
        return BetaGroupEndpoint(id, self.session)
    
    @endpoint('/v1/betaLicenseAgreements')
    def beta_license_agreements(self) -> BetaLicenseAgreementsEndpoint:
        return BetaLicenseAgreementsEndpoint(self.session)
    
    @endpoint('/v1/betaLicenseAgreements/{id}')
    def beta_license_agreement(self, id: str) -> BetaLicenseAgreementEndpoint:
        return BetaLicenseAgreementEndpoint(id, self.session)
    
    @endpoint('/v1/betaTesterInvitations')
    def beta_tester_invitations(self) -> BetaTesterInvitationsEndpoint:
        return BetaTesterInvitationsEndpoint(self.session)
    
    @endpoint('/v1/betaTesters')
    def beta_testers(self) -> BetaTestersEndpoint:
        return BetaTestersEndpoint(self.session)
    
    @endpoint('/v1/betaTesters/{id}')
    def beta_tester(self, id: str) -> BetaTesterEndpoint:
        return BetaTesterEndpoint(id, self.session)
    
    @endpoint('/v1/buildBetaDetails')
    def build_beta_details(self) -> BuildBetaDetailsEndpoint:
        return BuildBetaDetailsEndpoint(self.session)
    
    @endpoint('/v1/buildBetaDetails/{id}')
    def build_beta_detail(self, id: str) -> BuildBetaDetailEndpoint:
        return BuildBetaDetailEndpoint(id, self.session)
    
    @endpoint('/v1/buildBetaNotifications')
    def build_beta_notifications(self) -> BuildBetaNotificationsEndpoint:
        return BuildBetaNotificationsEndpoint(self.session)
    
    @endpoint('/v1/builds')
    def builds(self) -> BuildsEndpoint:
        return BuildsEndpoint(self.session)
    
    @endpoint('/v1/builds/{id}')
    def build(self, id: str) -> BuildEndpoint:
        return BuildEndpoint(id, self.session)
    
    @endpoint('/v1/bundleIdCapabilities')
    def bundle_id_capabilities(self) -> BundleIdCapabilitiesEndpoint:
        return BundleIdCapabilitiesEndpoint(self.session)
    
    @endpoint('/v1/bundleIdCapabilities/{id}')
    def bundle_id_capability(self, id: str) -> BundleIdCapabilityEndpoint:
        return BundleIdCapabilityEndpoint(id, self.session)
    
    @endpoint('/v1/bundleIds')
    def bundle_ids(self) -> BundleIdsEndpoint:
        return BundleIdsEndpoint(self.session)
    
    @endpoint('/v1/bundleIds/{id}')
    def bundle_id(self, id: str) -> BundleIdEndpoint:
        return BundleIdEndpoint(id, self.session)
    
    @endpoint('/v1/certificates')
    def certificates(self) -> CertificatesEndpoint:
        return CertificatesEndpoint(self.session)
    
    @endpoint('/v1/certificates/{id}')
    def certificate(self, id: str) -> CertificateEndpoint:
        return CertificateEndpoint(id, self.session)
    
    @endpoint('/v1/ciArtifacts/{id}')
    def ci_artifact(self, id: str) -> CiArtifactEndpoint:
        return CiArtifactEndpoint(id, self.session)
    
    @endpoint('/v1/ciBuildActions/{id}')
    def ci_build_action(self, id: str) -> CiBuildActionEndpoint:
        return CiBuildActionEndpoint(id, self.session)
    
    @endpoint('/v1/ciBuildRuns')
    def ci_build_runs(self) -> CiBuildRunsEndpoint:
        return CiBuildRunsEndpoint(self.session)
    
    @endpoint('/v1/ciBuildRuns/{id}')
    def ci_build_run(self, id: str) -> CiBuildRunEndpoint:
        return CiBuildRunEndpoint(id, self.session)
    
    @endpoint('/v1/ciIssues/{id}')
    def ci_issue(self, id: str) -> CiIssueEndpoint:
        return CiIssueEndpoint(id, self.session)
    
    @endpoint('/v1/ciMacOsVersions')
    def ci_mac_os_versions(self) -> CiMacOsVersionsEndpoint:
        return CiMacOsVersionsEndpoint(self.session)
    
    @endpoint('/v1/ciMacOsVersions/{id}')
    def ci_mac_os_version(self, id: str) -> CiMacOsVersionEndpoint:
        return CiMacOsVersionEndpoint(id, self.session)
    
    @endpoint('/v1/ciProducts')
    def ci_products(self) -> CiProductsEndpoint:
        return CiProductsEndpoint(self.session)
    
    @endpoint('/v1/ciProducts/{id}')
    def ci_product(self, id: str) -> CiProductEndpoint:
        return CiProductEndpoint(id, self.session)
    
    @endpoint('/v1/ciTestResults/{id}')
    def ci_test_result(self, id: str) -> CiTestResultEndpoint:
        return CiTestResultEndpoint(id, self.session)
    
    @endpoint('/v1/ciWorkflows')
    def ci_workflows(self) -> CiWorkflowsEndpoint:
        return CiWorkflowsEndpoint(self.session)
    
    @endpoint('/v1/ciWorkflows/{id}')
    def ci_workflow(self, id: str) -> CiWorkflowEndpoint:
        return CiWorkflowEndpoint(id, self.session)
    
    @endpoint('/v1/ciXcodeVersions')
    def ci_xcode_versions(self) -> CiXcodeVersionsEndpoint:
        return CiXcodeVersionsEndpoint(self.session)
    
    @endpoint('/v1/ciXcodeVersions/{id}')
    def ci_xcode_version(self, id: str) -> CiXcodeVersionEndpoint:
        return CiXcodeVersionEndpoint(id, self.session)
    
    @endpoint('/v1/devices')
    def devices(self) -> DevicesEndpoint:
        return DevicesEndpoint(self.session)
    
    @endpoint('/v1/devices/{id}')
    def device(self, id: str) -> DeviceEndpoint:
        return DeviceEndpoint(id, self.session)
    
    @endpoint('/v1/endUserLicenseAgreements')
    def end_user_license_agreements(self) -> EndUserLicenseAgreementsEndpoint:
        return EndUserLicenseAgreementsEndpoint(self.session)
    
    @endpoint('/v1/endUserLicenseAgreements/{id}')
    def end_user_license_agreement(self, id: str) -> EndUserLicenseAgreementEndpoint:
        return EndUserLicenseAgreementEndpoint(id, self.session)
    
    @endpoint('/v1/financeReports')
    def finance_reports(self) -> FinanceReportsEndpoint:
        return FinanceReportsEndpoint(self.session)
    
    @endpoint('/v1/idfaDeclarations')
    def idfa_declarations(self) -> IdfaDeclarationsEndpoint:
        return IdfaDeclarationsEndpoint(self.session)
    
    @endpoint('/v1/idfaDeclarations/{id}')
    def idfa_declaration(self, id: str) -> IdfaDeclarationEndpoint:
        return IdfaDeclarationEndpoint(id, self.session)
    
    @endpoint('/v1/inAppPurchases/{id}')
    def in_app_purchase(self, id: str) -> InAppPurchaseEndpoint:
        return InAppPurchaseEndpoint(id, self.session)
    
    @endpoint('/v1/preReleaseVersions')
    def pre_release_versions(self) -> PreReleaseVersionsEndpoint:
        return PreReleaseVersionsEndpoint(self.session)
    
    @endpoint('/v1/preReleaseVersions/{id}')
    def pre_release_version(self, id: str) -> PreReleaseVersionEndpoint:
        return PreReleaseVersionEndpoint(id, self.session)
    
    @endpoint('/v1/profiles')
    def profiles(self) -> ProfilesEndpoint:
        return ProfilesEndpoint(self.session)
    
    @endpoint('/v1/profiles/{id}')
    def profile(self, id: str) -> ProfileEndpoint:
        return ProfileEndpoint(id, self.session)
    
    @endpoint('/v1/routingAppCoverages')
    def routing_app_coverages(self) -> RoutingAppCoveragesEndpoint:
        return RoutingAppCoveragesEndpoint(self.session)
    
    @endpoint('/v1/routingAppCoverages/{id}')
    def routing_app_coverage(self, id: str) -> RoutingAppCoverageEndpoint:
        return RoutingAppCoverageEndpoint(id, self.session)
    
    @endpoint('/v1/salesReports')
    def sales_reports(self) -> SalesReportsEndpoint:
        return SalesReportsEndpoint(self.session)
    
    @endpoint('/v1/scmGitReferences/{id}')
    def scm_git_reference(self, id: str) -> ScmGitReferenceEndpoint:
        return ScmGitReferenceEndpoint(id, self.session)
    
    @endpoint('/v1/scmProviders')
    def scm_providers(self) -> ScmProvidersEndpoint:
        return ScmProvidersEndpoint(self.session)
    
    @endpoint('/v1/scmProviders/{id}')
    def scm_provider(self, id: str) -> ScmProviderEndpoint:
        return ScmProviderEndpoint(id, self.session)
    
    @endpoint('/v1/scmPullRequests/{id}')
    def scm_pull_request(self, id: str) -> ScmPullRequestEndpoint:
        return ScmPullRequestEndpoint(id, self.session)
    
    @endpoint('/v1/scmRepositories')
    def scm_repositories(self) -> ScmRepositoriesEndpoint:
        return ScmRepositoriesEndpoint(self.session)
    
    @endpoint('/v1/scmRepositories/{id}')
    def scm_repository(self, id: str) -> ScmRepositoryEndpoint:
        return ScmRepositoryEndpoint(id, self.session)
    
    @endpoint('/v1/territories')
    def territories(self) -> TerritoriesEndpoint:
        return TerritoriesEndpoint(self.session)
    
    @endpoint('/v1/userInvitations')
    def user_invitations(self) -> UserInvitationsEndpoint:
        return UserInvitationsEndpoint(self.session)
    
    @endpoint('/v1/userInvitations/{id}')
    def user_invitation(self, id: str) -> UserInvitationEndpoint:
        return UserInvitationEndpoint(id, self.session)
    
    @endpoint('/v1/users')
    def users(self) -> UsersEndpoint:
        return UsersEndpoint(self.session)
    
    @endpoint('/v1/users/{id}')
    def user(self, id: str) -> UserEndpoint:
        return UserEndpoint(id, self.session)
    
    @endpoint('/v1/buildBundles/{id}')
    def build_bundle(self, id: str) -> BuildBundleEndpoint:
        return BuildBundleEndpoint(id, self.session)
    
    @endpoint('/v1/diagnosticSignatures/{id}')
    def diagnostic_signature(self, id: str) -> DiagnosticSignatureEndpoint:
        return DiagnosticSignatureEndpoint(id, self.session)
    
    @endpoint('/v1/gameCenterEnabledVersions/{id}')
    def game_center_enabled_version(self, id: str) -> GameCenterEnabledVersionEndpoint:
        return GameCenterEnabledVersionEndpoint(id, self.session)
    
