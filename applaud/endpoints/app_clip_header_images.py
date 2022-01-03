from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppClipHeaderImageListEndpoint(Endpoint):
    path = '/v1/appClipHeaderImages'

    def create(self, request: AppClipHeaderImageCreateRequest) -> AppClipHeaderImageResponse:
        '''Create the resource.

        :param request: AppClipHeaderImage representation
        :type request: AppClipHeaderImageCreateRequest

        :returns: Single AppClipHeaderImage
        :rtype: AppClipHeaderImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_post(json)
        return AppClipHeaderImageResponse.parse_obj(response_json)

class AppClipHeaderImageEndpoint(IDEndpoint):
    path = '/v1/appClipHeaderImages/{id}'

    def fields(self, *, app_clip_header_image: Union[AppClipHeaderImageField, list[AppClipHeaderImageField]]=None) -> AppClipHeaderImageEndpoint:
        '''Fields to return for included related types.

        :param app_clip_header_image: the fields to include for returned resources of type appClipHeaderImages
        :type app_clip_header_image: Union[AppClipHeaderImageField, list[AppClipHeaderImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipHeaderImageEndpoint
        '''
        if app_clip_header_image: self._set_fields('appClipHeaderImages',app_clip_header_image if type(app_clip_header_image) is list else [app_clip_header_image])
        return self
        
    class Include(StringEnum):
        APP_CLIP_DEFAULT_EXPERIENCE_LOCALIZATION = 'appClipDefaultExperienceLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> AppClipHeaderImageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipHeaderImageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppClipHeaderImageResponse:
        '''Get the resource.

        :returns: Single AppClipHeaderImage
        :rtype: AppClipHeaderImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipHeaderImageResponse.parse_obj(json)

    def update(self, request: AppClipHeaderImageUpdateRequest) -> AppClipHeaderImageResponse:
        '''Modify the resource.

        :param request: AppClipHeaderImage representation
        :type request: AppClipHeaderImageUpdateRequest

        :returns: Single AppClipHeaderImage
        :rtype: AppClipHeaderImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_patch(json)
        return AppClipHeaderImageResponse.parse_obj(response_json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

