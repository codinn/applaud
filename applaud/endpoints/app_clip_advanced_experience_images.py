from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppClipAdvancedExperienceImagesEndpoint(Endpoint):
    path = '/v1/appClipAdvancedExperienceImages'

    def create(self, request: AppClipAdvancedExperienceImageCreateRequest) -> AppClipAdvancedExperienceImageResponse:
        '''Create the resource.

        :param request: AppClipAdvancedExperienceImage representation
        :type request: AppClipAdvancedExperienceImageCreateRequest

        :returns: Single AppClipAdvancedExperienceImage
        :rtype: AppClipAdvancedExperienceImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppClipAdvancedExperienceImageResponse.parse_obj(json)

class AppClipAdvancedExperienceImageEndpoint(IDEndpoint):
    path = '/v1/appClipAdvancedExperienceImages/{id}'

    def fields(self, *, app_clip_advanced_experience_image: Union[AppClipAdvancedExperienceImageField, list[AppClipAdvancedExperienceImageField]]=None) -> AppClipAdvancedExperienceImageEndpoint:
        '''Fields to return for included related types.

        :param app_clip_advanced_experience_image: the fields to include for returned resources of type appClipAdvancedExperienceImages
        :type app_clip_advanced_experience_image: Union[AppClipAdvancedExperienceImageField, list[AppClipAdvancedExperienceImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipAdvancedExperienceImageEndpoint
        '''
        if app_clip_advanced_experience_image: self._set_fields('appClipAdvancedExperienceImages',app_clip_advanced_experience_image if type(app_clip_advanced_experience_image) is list else [app_clip_advanced_experience_image])
        return self
        
    def get(self) -> AppClipAdvancedExperienceImageResponse:
        '''Get the resource.

        :returns: Single AppClipAdvancedExperienceImage
        :rtype: AppClipAdvancedExperienceImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipAdvancedExperienceImageResponse.parse_obj(json)

    def update(self, request: AppClipAdvancedExperienceImageUpdateRequest) -> AppClipAdvancedExperienceImageResponse:
        '''Modify the resource.

        :param request: AppClipAdvancedExperienceImage representation
        :type request: AppClipAdvancedExperienceImageUpdateRequest

        :returns: Single AppClipAdvancedExperienceImage
        :rtype: AppClipAdvancedExperienceImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppClipAdvancedExperienceImageResponse.parse_obj(json)

