from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class ParentLinkageOfAppCategoryEndpoint(IDEndpoint):
    path = '/v1/appCategories/{id}/relationships/parent'

class SubcategoriesLinkagesOfAppCategoryEndpoint(IDEndpoint):
    path = '/v1/appCategories/{id}/relationships/subcategories'

class AppClipHeaderImageLinkageOfAppClipDefaultExperienceLocalizationEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperienceLocalizations/{id}/relationships/appClipHeaderImage'

class AppClipAppStoreReviewDetailLinkageOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/relationships/appClipAppStoreReviewDetail'

class AppClipDefaultExperienceLocalizationsLinkagesOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/relationships/appClipDefaultExperienceLocalizations'

class AppClipAdvancedExperiencesLinkagesOfAppClipEndpoint(IDEndpoint):
    path = '/v1/appClips/{id}/relationships/appClipAdvancedExperiences'

class AppClipDefaultExperiencesLinkagesOfAppClipEndpoint(IDEndpoint):
    path = '/v1/appClips/{id}/relationships/appClipDefaultExperiences'

class AppLinkageOfAppEncryptionDeclarationEndpoint(IDEndpoint):
    path = '/v1/appEncryptionDeclarations/{id}/relationships/app'

class AgeRatingDeclarationLinkageOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/relationships/ageRatingDeclaration'

class AppInfoLocalizationsLinkagesOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/relationships/appInfoLocalizations'

class PrimaryCategoryLinkageOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/relationships/primaryCategory'

class PrimarySubcategoryOneLinkageOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/relationships/primarySubcategoryOne'

class PrimarySubcategoryTwoLinkageOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/relationships/primarySubcategoryTwo'

class SecondaryCategoryLinkageOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/relationships/secondaryCategory'

class SecondarySubcategoryOneLinkageOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/relationships/secondarySubcategoryOne'

class SecondarySubcategoryTwoLinkageOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/relationships/secondarySubcategoryTwo'

class TerritoryLinkageOfAppPricePointEndpoint(IDEndpoint):
    path = '/v1/appPricePoints/{id}/relationships/territory'

class PricePointsLinkagesOfAppPriceTierEndpoint(IDEndpoint):
    path = '/v1/appPriceTiers/{id}/relationships/pricePoints'

class AppStoreReviewAttachmentsLinkagesOfAppStoreReviewDetailEndpoint(IDEndpoint):
    path = '/v1/appStoreReviewDetails/{id}/relationships/appStoreReviewAttachments'

class AppPreviewSetsLinkagesOfAppStoreVersionLocalizationEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionLocalizations/{id}/relationships/appPreviewSets'

class AppScreenshotSetsLinkagesOfAppStoreVersionLocalizationEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionLocalizations/{id}/relationships/appScreenshotSets'

class AgeRatingDeclarationLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/ageRatingDeclaration'

class AppStoreReviewDetailLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appStoreReviewDetail'

class AppStoreVersionLocalizationsLinkagesOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appStoreVersionLocalizations'

class AppStoreVersionPhasedReleaseLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appStoreVersionPhasedRelease'

class AppStoreVersionSubmissionLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appStoreVersionSubmission'

class IdfaDeclarationLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/idfaDeclaration'

class RoutingAppCoverageLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/routingAppCoverage'

class AppClipsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appClips'

class AppInfosLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appInfos'

class AppStoreVersionsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appStoreVersions'

class AvailableTerritoriesLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/availableTerritories'

class BetaAppLocalizationsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaAppLocalizations'

class BetaAppReviewDetailLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaAppReviewDetail'

class BetaGroupsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaGroups'

class BetaLicenseAgreementLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaLicenseAgreement'

class BuildsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/builds'

class CiProductLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/ciProduct'

class EndUserLicenseAgreementLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/endUserLicenseAgreement'

class GameCenterEnabledVersionsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/gameCenterEnabledVersions'

class InAppPurchasesLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/inAppPurchases'

class PerfPowerMetricsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/perfPowerMetrics'

class PreOrderLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/preOrder'

class PreReleaseVersionsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/preReleaseVersions'

class PricesLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/prices'

class AppLinkageOfBetaAppLocalizationEndpoint(IDEndpoint):
    path = '/v1/betaAppLocalizations/{id}/relationships/app'

class AppLinkageOfBetaAppReviewDetailEndpoint(IDEndpoint):
    path = '/v1/betaAppReviewDetails/{id}/relationships/app'

class BuildLinkageOfBetaAppReviewSubmissionEndpoint(IDEndpoint):
    path = '/v1/betaAppReviewSubmissions/{id}/relationships/build'

class BuildLinkageOfBetaBuildLocalizationEndpoint(IDEndpoint):
    path = '/v1/betaBuildLocalizations/{id}/relationships/build'

class AppLinkageOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/relationships/app'

class AppLinkageOfBetaLicenseAgreementEndpoint(IDEndpoint):
    path = '/v1/betaLicenseAgreements/{id}/relationships/app'

class BuildLinkageOfBuildBetaDetailEndpoint(IDEndpoint):
    path = '/v1/buildBetaDetails/{id}/relationships/build'

class AppClipDomainCacheStatusLinkagesOfBuildBundleEndpoint(IDEndpoint):
    path = '/v1/buildBundles/{id}/relationships/appClipDomainCacheStatus'

class AppClipDomainDebugStatusLinkagesOfBuildBundleEndpoint(IDEndpoint):
    path = '/v1/buildBundles/{id}/relationships/appClipDomainDebugStatus'

class BetaAppClipInvocationsLinkagesOfBuildBundleEndpoint(IDEndpoint):
    path = '/v1/buildBundles/{id}/relationships/betaAppClipInvocations'

class BuildBundleFileSizesLinkagesOfBuildBundleEndpoint(IDEndpoint):
    path = '/v1/buildBundles/{id}/relationships/buildBundleFileSizes'

class AppLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/app'

class AppStoreVersionLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/appStoreVersion'

class BetaAppReviewSubmissionLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/betaAppReviewSubmission'

class BetaBuildLocalizationsLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/betaBuildLocalizations'

class BuildBetaDetailLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/buildBetaDetail'

class DiagnosticSignaturesLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/diagnosticSignatures'

class IconsLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/icons'

class PerfPowerMetricsLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/perfPowerMetrics'

class PreReleaseVersionLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/preReleaseVersion'

class AppLinkageOfBundleIdEndpoint(IDEndpoint):
    path = '/v1/bundleIds/{id}/relationships/app'

class BundleIdCapabilitiesLinkagesOfBundleIdEndpoint(IDEndpoint):
    path = '/v1/bundleIds/{id}/relationships/bundleIdCapabilities'

class ProfilesLinkagesOfBundleIdEndpoint(IDEndpoint):
    path = '/v1/bundleIds/{id}/relationships/profiles'

class ArtifactsLinkagesOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/relationships/artifacts'

class BuildRunLinkageOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/relationships/buildRun'

class IssuesLinkagesOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/relationships/issues'

class TestResultsLinkagesOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/relationships/testResults'

class ActionsLinkagesOfCiBuildRunEndpoint(IDEndpoint):
    path = '/v1/ciBuildRuns/{id}/relationships/actions'

class BuildsLinkagesOfCiBuildRunEndpoint(IDEndpoint):
    path = '/v1/ciBuildRuns/{id}/relationships/builds'

class XcodeVersionsLinkagesOfCiMacOsVersionEndpoint(IDEndpoint):
    path = '/v1/ciMacOsVersions/{id}/relationships/xcodeVersions'

class AdditionalRepositoriesLinkagesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/relationships/additionalRepositories'

class AppLinkageOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/relationships/app'

class BuildRunsLinkagesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/relationships/buildRuns'

class PrimaryRepositoriesLinkagesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/relationships/primaryRepositories'

class WorkflowsLinkagesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/relationships/workflows'

class BuildRunsLinkagesOfCiWorkflowEndpoint(IDEndpoint):
    path = '/v1/ciWorkflows/{id}/relationships/buildRuns'

class RepositoryLinkageOfCiWorkflowEndpoint(IDEndpoint):
    path = '/v1/ciWorkflows/{id}/relationships/repository'

class MacOsVersionsLinkagesOfCiXcodeVersionEndpoint(IDEndpoint):
    path = '/v1/ciXcodeVersions/{id}/relationships/macOsVersions'

class LogsLinkagesOfDiagnosticSignatureEndpoint(IDEndpoint):
    path = '/v1/diagnosticSignatures/{id}/relationships/logs'

class TerritoriesLinkagesOfEndUserLicenseAgreementEndpoint(IDEndpoint):
    path = '/v1/endUserLicenseAgreements/{id}/relationships/territories'

class AppLinkageOfPreReleaseVersionEndpoint(IDEndpoint):
    path = '/v1/preReleaseVersions/{id}/relationships/app'

class BuildsLinkagesOfPreReleaseVersionEndpoint(IDEndpoint):
    path = '/v1/preReleaseVersions/{id}/relationships/builds'

class BundleIdLinkageOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/relationships/bundleId'

class CertificatesLinkagesOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/relationships/certificates'

class DevicesLinkagesOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/relationships/devices'

class RepositoriesLinkagesOfScmProviderEndpoint(IDEndpoint):
    path = '/v1/scmProviders/{id}/relationships/repositories'

class GitReferencesLinkagesOfScmRepositoryEndpoint(IDEndpoint):
    path = '/v1/scmRepositories/{id}/relationships/gitReferences'

class PullRequestsLinkagesOfScmRepositoryEndpoint(IDEndpoint):
    path = '/v1/scmRepositories/{id}/relationships/pullRequests'

class VisibleAppsLinkagesOfUserInvitationEndpoint(IDEndpoint):
    path = '/v1/userInvitations/{id}/relationships/visibleApps'

