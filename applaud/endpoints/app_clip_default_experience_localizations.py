from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppClipDefaultExperienceLocalizationsEndpoint(Endpoint):
    path = '/v1/appClipDefaultExperienceLocalizations'

    def create(self, request: AppClipDefaultExperienceLocalizationCreateRequest) -> AppClipDefaultExperienceLocalizationResponse:
        '''Create the resource.

        :param request: AppClipDefaultExperienceLocalization representation
        :type request: AppClipDefaultExperienceLocalizationCreateRequest

        :returns: Single AppClipDefaultExperienceLocalization
        :rtype: AppClipDefaultExperienceLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppClipDefaultExperienceLocalizationResponse.parse_obj(json)

class AppClipDefaultExperienceLocalizationEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperienceLocalizations/{id}'

    @endpoint('/v1/appClipDefaultExperienceLocalizations/{id}/appClipHeaderImage')
    def app_clip_header_image(self) -> AppClipHeaderImageOfAppClipDefaultExperienceLocalizationEndpoint:
        return AppClipHeaderImageOfAppClipDefaultExperienceLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]]=None, app_clip_header_image: Union[AppClipHeaderImageField, list[AppClipHeaderImageField]]=None) -> AppClipDefaultExperienceLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_clip_default_experience_localization: the fields to include for returned resources of type appClipDefaultExperienceLocalizations
        :type app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]] = None

        :param app_clip_header_image: the fields to include for returned resources of type appClipHeaderImages
        :type app_clip_header_image: Union[AppClipHeaderImageField, list[AppClipHeaderImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceLocalizationEndpoint
        '''
        if app_clip_default_experience_localization: self._set_fields('appClipDefaultExperienceLocalizations',app_clip_default_experience_localization if type(app_clip_default_experience_localization) is list else [app_clip_default_experience_localization])
        if app_clip_header_image: self._set_fields('appClipHeaderImages',app_clip_header_image if type(app_clip_header_image) is list else [app_clip_header_image])
        return self
        
    class Include(StringEnum):
        APP_CLIP_DEFAULT_EXPERIENCE = 'appClipDefaultExperience'
        APP_CLIP_HEADER_IMAGE = 'appClipHeaderImage'

    def include(self, relationship: Union[Include, list[Include]]) -> AppClipDefaultExperienceLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppClipDefaultExperienceLocalizationResponse:
        '''Get the resource.

        :returns: Single AppClipDefaultExperienceLocalization
        :rtype: AppClipDefaultExperienceLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperienceLocalizationResponse.parse_obj(json)

    def update(self, request: AppClipDefaultExperienceLocalizationUpdateRequest) -> AppClipDefaultExperienceLocalizationResponse:
        '''Modify the resource.

        :param request: AppClipDefaultExperienceLocalization representation
        :type request: AppClipDefaultExperienceLocalizationUpdateRequest

        :returns: Single AppClipDefaultExperienceLocalization
        :rtype: AppClipDefaultExperienceLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppClipDefaultExperienceLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppClipHeaderImageOfAppClipDefaultExperienceLocalizationEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperienceLocalizations/{id}/appClipHeaderImage'

    def fields(self, *, app_clip_header_image: Union[AppClipHeaderImageField, list[AppClipHeaderImageField]]=None) -> AppClipHeaderImageOfAppClipDefaultExperienceLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_clip_header_image: the fields to include for returned resources of type appClipHeaderImages
        :type app_clip_header_image: Union[AppClipHeaderImageField, list[AppClipHeaderImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipHeaderImageOfAppClipDefaultExperienceLocalizationEndpoint
        '''
        if app_clip_header_image: self._set_fields('appClipHeaderImages',app_clip_header_image if type(app_clip_header_image) is list else [app_clip_header_image])
        return self
        
    def get(self) -> AppClipHeaderImageResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppClipHeaderImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipHeaderImageResponse.parse_obj(json)

