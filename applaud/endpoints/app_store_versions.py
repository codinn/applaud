from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionsEndpoint(Endpoint):
    path = '/v1/appStoreVersions'

    def create(self, request: AppStoreVersionCreateRequest) -> AppStoreVersionResponse:
        '''Create the resource.

        :param request: AppStoreVersion representation
        :type request: AppStoreVersionCreateRequest

        :returns: Single AppStoreVersion
        :rtype: AppStoreVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreVersionResponse.parse_obj(json)

class AppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}'

    @endpoint('/v1/appStoreVersions/{id}/ageRatingDeclaration')
    def age_rating_declaration(self) -> AgeRatingDeclarationOfAppStoreVersionEndpoint:
        return AgeRatingDeclarationOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appClipDefaultExperience')
    def app_clip_default_experience(self) -> AppClipDefaultExperienceOfAppStoreVersionEndpoint:
        return AppClipDefaultExperienceOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appStoreReviewDetail')
    def app_store_review_detail(self) -> AppStoreReviewDetailOfAppStoreVersionEndpoint:
        return AppStoreReviewDetailOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appStoreVersionLocalizations')
    def app_store_version_localizations(self) -> AppStoreVersionLocalizationsOfAppStoreVersionEndpoint:
        return AppStoreVersionLocalizationsOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appStoreVersionPhasedRelease')
    def app_store_version_phased_release(self) -> AppStoreVersionPhasedReleaseOfAppStoreVersionEndpoint:
        return AppStoreVersionPhasedReleaseOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appStoreVersionSubmission')
    def app_store_version_submission(self) -> AppStoreVersionSubmissionOfAppStoreVersionEndpoint:
        return AppStoreVersionSubmissionOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/build')
    def build(self) -> BuildOfAppStoreVersionEndpoint:
        return BuildOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/idfaDeclaration')
    def idfa_declaration(self) -> IdfaDeclarationOfAppStoreVersionEndpoint:
        return IdfaDeclarationOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/routingAppCoverage')
    def routing_app_coverage(self) -> RoutingAppCoverageOfAppStoreVersionEndpoint:
        return RoutingAppCoverageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/appClipDefaultExperience')
    def app_clip_default_experience_linkage(self) -> AppClipDefaultExperienceLinkageOfAppStoreVersionEndpoint:
        return AppClipDefaultExperienceLinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/build')
    def build_linkage(self) -> BuildLinkageOfAppStoreVersionEndpoint:
        return BuildLinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    def fields(self, *, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]]=None, age_rating_declaration: Union[AgeRatingDeclarationField, list[AgeRatingDeclarationField]]=None, app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]]=None, idfa_declaration: Union[IdfaDeclarationField, list[IdfaDeclarationField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]]=None, app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]]=None, build: Union[BuildField, list[BuildField]]=None, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None) -> AppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_store_version_submission: the fields to include for returned resources of type appStoreVersionSubmissions
        :type app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]] = None

        :param age_rating_declaration: the fields to include for returned resources of type ageRatingDeclarations
        :type age_rating_declaration: Union[AgeRatingDeclarationField, list[AgeRatingDeclarationField]] = None

        :param app_store_review_detail: the fields to include for returned resources of type appStoreReviewDetails
        :type app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]] = None

        :param idfa_declaration: the fields to include for returned resources of type idfaDeclarations
        :type idfa_declaration: Union[IdfaDeclarationField, list[IdfaDeclarationField]] = None

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :param routing_app_coverage: the fields to include for returned resources of type routingAppCoverages
        :type routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]] = None

        :param app_store_version_phased_release: the fields to include for returned resources of type appStoreVersionPhasedReleases
        :type app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param app_store_version_localization: the fields to include for returned resources of type appStoreVersionLocalizations
        :type app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionEndpoint
        '''
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_store_version_submission: self._set_fields('appStoreVersionSubmissions',app_store_version_submission if type(app_store_version_submission) is list else [app_store_version_submission])
        if age_rating_declaration: self._set_fields('ageRatingDeclarations',age_rating_declaration if type(age_rating_declaration) is list else [age_rating_declaration])
        if app_store_review_detail: self._set_fields('appStoreReviewDetails',app_store_review_detail if type(app_store_review_detail) is list else [app_store_review_detail])
        if idfa_declaration: self._set_fields('idfaDeclarations',idfa_declaration if type(idfa_declaration) is list else [idfa_declaration])
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        if routing_app_coverage: self._set_fields('routingAppCoverages',routing_app_coverage if type(routing_app_coverage) is list else [routing_app_coverage])
        if app_store_version_phased_release: self._set_fields('appStoreVersionPhasedReleases',app_store_version_phased_release if type(app_store_version_phased_release) is list else [app_store_version_phased_release])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if app_store_version_localization: self._set_fields('appStoreVersionLocalizations',app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        return self
        
    class Include(StringEnum):
        AGE_RATING_DECLARATION = 'ageRatingDeclaration'
        APP = 'app'
        APP_CLIP_DEFAULT_EXPERIENCE = 'appClipDefaultExperience'
        APP_STORE_REVIEW_DETAIL = 'appStoreReviewDetail'
        APP_STORE_VERSION_LOCALIZATIONS = 'appStoreVersionLocalizations'
        APP_STORE_VERSION_PHASED_RELEASE = 'appStoreVersionPhasedRelease'
        APP_STORE_VERSION_SUBMISSION = 'appStoreVersionSubmission'
        BUILD = 'build'
        IDFA_DECLARATION = 'idfaDeclaration'
        ROUTING_APP_COVERAGE = 'routingAppCoverage'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_version_localizations: int=None) -> AppStoreVersionEndpoint:
        '''Number of included related resources to return.

        :param app_store_version_localizations: maximum number of related appStoreVersionLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionEndpoint
        '''
        if app_store_version_localizations and app_store_version_localizations > 50:
            raise ValueError(f'The maximum limit of app_store_version_localizations is 50')
        if app_store_version_localizations: self._set_limit(app_store_version_localizations, 'appStoreVersionLocalizations')

        return self

    def get(self) -> AppStoreVersionResponse:
        '''Get the resource.

        :returns: Single AppStoreVersion
        :rtype: AppStoreVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionResponse.parse_obj(json)

    def update(self, request: AppStoreVersionUpdateRequest) -> AppStoreVersionResponse:
        '''Modify the resource.

        :param request: AppStoreVersion representation
        :type request: AppStoreVersionUpdateRequest

        :returns: Single AppStoreVersion
        :rtype: AppStoreVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppStoreVersionResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AgeRatingDeclarationOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/ageRatingDeclaration'

    def fields(self, *, age_rating_declaration: Union[AgeRatingDeclarationField, list[AgeRatingDeclarationField]]=None) -> AgeRatingDeclarationOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param age_rating_declaration: the fields to include for returned resources of type ageRatingDeclarations
        :type age_rating_declaration: Union[AgeRatingDeclarationField, list[AgeRatingDeclarationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AgeRatingDeclarationOfAppStoreVersionEndpoint
        '''
        if age_rating_declaration: self._set_fields('ageRatingDeclarations',age_rating_declaration if type(age_rating_declaration) is list else [age_rating_declaration])
        return self
        
    @deprecated
    def get(self) -> AgeRatingDeclarationResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AgeRatingDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AgeRatingDeclarationResponse.parse_obj(json)

class AppClipDefaultExperienceLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appClipDefaultExperience'

    def get(self) -> AppStoreVersionAppClipDefaultExperienceLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppStoreVersionAppClipDefaultExperienceLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionAppClipDefaultExperienceLinkageResponse.parse_obj(json)

    def update(self, request: AppStoreVersionAppClipDefaultExperienceLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: AppStoreVersionAppClipDefaultExperienceLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class AppClipDefaultExperienceOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appClipDefaultExperience'

    def fields(self, *, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]]=None) -> AppClipDefaultExperienceOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :param app_clip_default_experience_localization: the fields to include for returned resources of type appClipDefaultExperienceLocalizations
        :type app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceOfAppStoreVersionEndpoint
        '''
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        if app_clip_default_experience_localization: self._set_fields('appClipDefaultExperienceLocalizations',app_clip_default_experience_localization if type(app_clip_default_experience_localization) is list else [app_clip_default_experience_localization])
        return self
        
    class Include(StringEnum):
        APP_CLIP_DEFAULT_EXPERIENCE_LOCALIZATIONS = 'appClipDefaultExperienceLocalizations'

    def include(self, relationship: Union[Include, list[Include]]) -> AppClipDefaultExperienceOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_clip_default_experience_localizations: int=None) -> AppClipDefaultExperienceOfAppStoreVersionEndpoint:
        '''Number of included related resources to return.

        :param app_clip_default_experience_localizations: maximum number of related appClipDefaultExperienceLocalizations returned (when they are included). The maximum limit is 50
        :type app_clip_default_experience_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceOfAppStoreVersionEndpoint
        '''
        if app_clip_default_experience_localizations and app_clip_default_experience_localizations > 50:
            raise ValueError(f'The maximum limit of app_clip_default_experience_localizations is 50')
        if app_clip_default_experience_localizations: self._set_limit(app_clip_default_experience_localizations, 'appClipDefaultExperienceLocalizations')

        return self

    def get(self) -> AppClipDefaultExperienceResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppClipDefaultExperienceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperienceResponse.parse_obj(json)

class AppStoreReviewDetailOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appStoreReviewDetail'

    def fields(self, *, app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]]=None, app_store_review_attachment: Union[AppStoreReviewAttachmentField, list[AppStoreReviewAttachmentField]]=None) -> AppStoreReviewDetailOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_review_detail: the fields to include for returned resources of type appStoreReviewDetails
        :type app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]] = None

        :param app_store_review_attachment: the fields to include for returned resources of type appStoreReviewAttachments
        :type app_store_review_attachment: Union[AppStoreReviewAttachmentField, list[AppStoreReviewAttachmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewDetailOfAppStoreVersionEndpoint
        '''
        if app_store_review_detail: self._set_fields('appStoreReviewDetails',app_store_review_detail if type(app_store_review_detail) is list else [app_store_review_detail])
        if app_store_review_attachment: self._set_fields('appStoreReviewAttachments',app_store_review_attachment if type(app_store_review_attachment) is list else [app_store_review_attachment])
        return self
        
    class Include(StringEnum):
        APP_STORE_REVIEW_ATTACHMENTS = 'appStoreReviewAttachments'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreReviewDetailOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewDetailOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_review_attachments: int=None) -> AppStoreReviewDetailOfAppStoreVersionEndpoint:
        '''Number of included related resources to return.

        :param app_store_review_attachments: maximum number of related appStoreReviewAttachments returned (when they are included). The maximum limit is 50
        :type app_store_review_attachments: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewDetailOfAppStoreVersionEndpoint
        '''
        if app_store_review_attachments and app_store_review_attachments > 50:
            raise ValueError(f'The maximum limit of app_store_review_attachments is 50')
        if app_store_review_attachments: self._set_limit(app_store_review_attachments, 'appStoreReviewAttachments')

        return self

    def get(self) -> AppStoreReviewDetailResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppStoreReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreReviewDetailResponse.parse_obj(json)

class AppStoreVersionLocalizationsOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appStoreVersionLocalizations'

    def fields(self, *, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None) -> AppStoreVersionLocalizationsOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_localization: the fields to include for returned resources of type appStoreVersionLocalizations
        :type app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionLocalizationsOfAppStoreVersionEndpoint
        '''
        if app_store_version_localization: self._set_fields('appStoreVersionLocalizations',app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        return self
        
    def limit(self, number: int=None) -> AppStoreVersionLocalizationsOfAppStoreVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionLocalizationsOfAppStoreVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppStoreVersionLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppStoreVersionLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionLocalizationsResponse.parse_obj(json)

class AppStoreVersionPhasedReleaseOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appStoreVersionPhasedRelease'

    def fields(self, *, app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]]=None) -> AppStoreVersionPhasedReleaseOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_phased_release: the fields to include for returned resources of type appStoreVersionPhasedReleases
        :type app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionPhasedReleaseOfAppStoreVersionEndpoint
        '''
        if app_store_version_phased_release: self._set_fields('appStoreVersionPhasedReleases',app_store_version_phased_release if type(app_store_version_phased_release) is list else [app_store_version_phased_release])
        return self
        
    def get(self) -> AppStoreVersionPhasedReleaseResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppStoreVersionPhasedReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionPhasedReleaseResponse.parse_obj(json)

class AppStoreVersionSubmissionOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appStoreVersionSubmission'

    def fields(self, *, app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]]=None) -> AppStoreVersionSubmissionOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_submission: the fields to include for returned resources of type appStoreVersionSubmissions
        :type app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionSubmissionOfAppStoreVersionEndpoint
        '''
        if app_store_version_submission: self._set_fields('appStoreVersionSubmissions',app_store_version_submission if type(app_store_version_submission) is list else [app_store_version_submission])
        return self
        
    def get(self) -> AppStoreVersionSubmissionResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppStoreVersionSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionSubmissionResponse.parse_obj(json)

class BuildLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/build'

    def get(self) -> AppStoreVersionBuildLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppStoreVersionBuildLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionBuildLinkageResponse.parse_obj(json)

    def update(self, request: AppStoreVersionBuildLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: AppStoreVersionBuildLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class BuildOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/build'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildOfAppStoreVersionEndpoint
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

class IdfaDeclarationOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/idfaDeclaration'

    def fields(self, *, idfa_declaration: Union[IdfaDeclarationField, list[IdfaDeclarationField]]=None) -> IdfaDeclarationOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param idfa_declaration: the fields to include for returned resources of type idfaDeclarations
        :type idfa_declaration: Union[IdfaDeclarationField, list[IdfaDeclarationField]] = None

        :returns: self
        :rtype: applaud.endpoints.IdfaDeclarationOfAppStoreVersionEndpoint
        '''
        if idfa_declaration: self._set_fields('idfaDeclarations',idfa_declaration if type(idfa_declaration) is list else [idfa_declaration])
        return self
        
    @deprecated
    def get(self) -> IdfaDeclarationResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: IdfaDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return IdfaDeclarationResponse.parse_obj(json)

class RoutingAppCoverageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/routingAppCoverage'

    def fields(self, *, routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]]=None) -> RoutingAppCoverageOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param routing_app_coverage: the fields to include for returned resources of type routingAppCoverages
        :type routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]] = None

        :returns: self
        :rtype: applaud.endpoints.RoutingAppCoverageOfAppStoreVersionEndpoint
        '''
        if routing_app_coverage: self._set_fields('routingAppCoverages',routing_app_coverage if type(routing_app_coverage) is list else [routing_app_coverage])
        return self
        
    def get(self) -> RoutingAppCoverageResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: RoutingAppCoverageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return RoutingAppCoverageResponse.parse_obj(json)

