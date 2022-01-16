from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppPreviewsEndpoint(Endpoint):
    path = '/v1/appPreviews'

    def create(self, request: AppPreviewCreateRequest) -> AppPreviewResponse:
        '''Create the resource.

        :param request: AppPreview representation
        :type request: AppPreviewCreateRequest

        :returns: Single AppPreview
        :rtype: AppPreviewResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppPreviewResponse.parse_obj(json)

class AppPreviewEndpoint(IDEndpoint):
    path = '/v1/appPreviews/{id}'

    def fields(self, *, app_preview: Union[AppPreviewField, list[AppPreviewField]]=None) -> AppPreviewEndpoint:
        '''Fields to return for included related types.

        :param app_preview: the fields to include for returned resources of type appPreviews
        :type app_preview: Union[AppPreviewField, list[AppPreviewField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewEndpoint
        '''
        if app_preview: self._set_fields('appPreviews',app_preview if type(app_preview) is list else [app_preview])
        return self
        
    class Include(StringEnum):
        APP_PREVIEW_SET = 'appPreviewSet'

    def include(self, relationship: Union[Include, list[Include]]) -> AppPreviewEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPreviewEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppPreviewResponse:
        '''Get the resource.

        :returns: Single AppPreview
        :rtype: AppPreviewResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPreviewResponse.parse_obj(json)

    def update(self, request: AppPreviewUpdateRequest) -> AppPreviewResponse:
        '''Modify the resource.

        :param request: AppPreview representation
        :type request: AppPreviewUpdateRequest

        :returns: Single AppPreview
        :rtype: AppPreviewResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppPreviewResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

