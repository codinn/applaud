from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppClipDefaultExperiencesEndpoint(Endpoint):
    path = '/v1/appClipDefaultExperiences'

    def create(self, request: AppClipDefaultExperienceCreateRequest) -> AppClipDefaultExperienceResponse:
        '''Create the resource.

        :param request: AppClipDefaultExperience representation
        :type request: AppClipDefaultExperienceCreateRequest

        :returns: Single AppClipDefaultExperience
        :rtype: AppClipDefaultExperienceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppClipDefaultExperienceResponse.parse_obj(json)

class AppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}'

    @endpoint('/v1/appClipDefaultExperiences/{id}/appClipAppStoreReviewDetail')
    def app_clip_app_store_review_detail(self) -> AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint:
        return AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint(self.id, self.session)
        
    @endpoint('/v1/appClipDefaultExperiences/{id}/appClipDefaultExperienceLocalizations')
    def app_clip_default_experience_localizations(self) -> AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint:
        return AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint(self.id, self.session)
        
    @endpoint('/v1/appClipDefaultExperiences/{id}/releaseWithAppStoreVersion')
    def release_with_app_store_version(self) -> ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint:
        return ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint(self.id, self.session)
        
    @endpoint('/v1/appClipDefaultExperiences/{id}/relationships/releaseWithAppStoreVersion')
    def release_with_app_store_version_linkage(self) -> ReleaseWithAppStoreVersionLinkageOfAppClipDefaultExperienceEndpoint:
        return ReleaseWithAppStoreVersionLinkageOfAppClipDefaultExperienceEndpoint(self.id, self.session)
        
    def fields(self, *, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]]=None) -> AppClipDefaultExperienceEndpoint:
        '''Fields to return for included related types.

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :param app_clip_app_store_review_detail: the fields to include for returned resources of type appClipAppStoreReviewDetails
        :type app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_clip_default_experience_localization: the fields to include for returned resources of type appClipDefaultExperienceLocalizations
        :type app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceEndpoint
        '''
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        if app_clip_app_store_review_detail: self._set_fields('appClipAppStoreReviewDetails',app_clip_app_store_review_detail if type(app_clip_app_store_review_detail) is list else [app_clip_app_store_review_detail])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_clip_default_experience_localization: self._set_fields('appClipDefaultExperienceLocalizations',app_clip_default_experience_localization if type(app_clip_default_experience_localization) is list else [app_clip_default_experience_localization])
        return self
        
    class Include(StringEnum):
        APP_CLIP = 'appClip'
        APP_CLIP_APP_STORE_REVIEW_DETAIL = 'appClipAppStoreReviewDetail'
        APP_CLIP_DEFAULT_EXPERIENCE_LOCALIZATIONS = 'appClipDefaultExperienceLocalizations'
        RELEASE_WITH_APP_STORE_VERSION = 'releaseWithAppStoreVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> AppClipDefaultExperienceEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_clip_default_experience_localizations: int=None) -> AppClipDefaultExperienceEndpoint:
        '''Number of included related resources to return.

        :param app_clip_default_experience_localizations: maximum number of related appClipDefaultExperienceLocalizations returned (when they are included). The maximum limit is 50
        :type app_clip_default_experience_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceEndpoint
        '''
        if app_clip_default_experience_localizations and app_clip_default_experience_localizations > 50:
            raise ValueError(f'The maximum limit of app_clip_default_experience_localizations is 50')
        if app_clip_default_experience_localizations: self._set_limit(app_clip_default_experience_localizations, 'appClipDefaultExperienceLocalizations')

        return self

    def get(self) -> AppClipDefaultExperienceResponse:
        '''Get the resource.

        :returns: Single AppClipDefaultExperience
        :rtype: AppClipDefaultExperienceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperienceResponse.parse_obj(json)

    def update(self, request: AppClipDefaultExperienceUpdateRequest) -> AppClipDefaultExperienceResponse:
        '''Modify the resource.

        :param request: AppClipDefaultExperience representation
        :type request: AppClipDefaultExperienceUpdateRequest

        :returns: Single AppClipDefaultExperience
        :rtype: AppClipDefaultExperienceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppClipDefaultExperienceResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/appClipAppStoreReviewDetail'

    def fields(self, *, app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]]=None) -> AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint:
        '''Fields to return for included related types.

        :param app_clip_app_store_review_detail: the fields to include for returned resources of type appClipAppStoreReviewDetails
        :type app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint
        '''
        if app_clip_app_store_review_detail: self._set_fields('appClipAppStoreReviewDetails',app_clip_app_store_review_detail if type(app_clip_app_store_review_detail) is list else [app_clip_app_store_review_detail])
        return self
        
    def get(self) -> AppClipAppStoreReviewDetailResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppClipAppStoreReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipAppStoreReviewDetailResponse.parse_obj(json)

class AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/appClipDefaultExperienceLocalizations'

    def fields(self, *, app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]]=None) -> AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint:
        '''Fields to return for included related types.

        :param app_clip_default_experience_localization: the fields to include for returned resources of type appClipDefaultExperienceLocalizations
        :type app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint
        '''
        if app_clip_default_experience_localization: self._set_fields('appClipDefaultExperienceLocalizations',app_clip_default_experience_localization if type(app_clip_default_experience_localization) is list else [app_clip_default_experience_localization])
        return self
        
    def filter(self, *, locale: Union[str, list[str]]=None) -> AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param locale: filter by attribute 'locale'
        :type locale: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint
        '''
        if locale: self._set_filter('locale', locale if type(locale) is list else [locale])
        
        return self
        
    def limit(self, number: int=None) -> AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppClipDefaultExperienceLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppClipDefaultExperienceLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperienceLocalizationsResponse.parse_obj(json)

class ReleaseWithAppStoreVersionLinkageOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/relationships/releaseWithAppStoreVersion'

    def get(self) -> AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageResponse.parse_obj(json)

    def update(self, request: AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/releaseWithAppStoreVersion'

    def fields(self, *, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None) -> ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint:
        '''Fields to return for included related types.

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_store_version_localization: the fields to include for returned resources of type appStoreVersionLocalizations
        :type app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint
        '''
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_store_version_localization: self._set_fields('appStoreVersionLocalizations',app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION_LOCALIZATIONS = 'appStoreVersionLocalizations'

    def include(self, relationship: Union[Include, list[Include]]) -> ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_version_localizations: int=None) -> ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint:
        '''Number of included related resources to return.

        :param app_store_version_localizations: maximum number of related appStoreVersionLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint
        '''
        if app_store_version_localizations and app_store_version_localizations > 50:
            raise ValueError(f'The maximum limit of app_store_version_localizations is 50')
        if app_store_version_localizations: self._set_limit(app_store_version_localizations, 'appStoreVersionLocalizations')

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

