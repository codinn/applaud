from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppClipAppStoreReviewDetailsEndpoint(Endpoint):
    path = '/v1/appClipAppStoreReviewDetails'

    def create(self, request: AppClipAppStoreReviewDetailCreateRequest) -> AppClipAppStoreReviewDetailResponse:
        '''Create the resource.

        :param request: AppClipAppStoreReviewDetail representation
        :type request: AppClipAppStoreReviewDetailCreateRequest

        :returns: Single AppClipAppStoreReviewDetail
        :rtype: AppClipAppStoreReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppClipAppStoreReviewDetailResponse.parse_obj(json)

class AppClipAppStoreReviewDetailEndpoint(IDEndpoint):
    path = '/v1/appClipAppStoreReviewDetails/{id}'

    def fields(self, *, app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]]=None) -> AppClipAppStoreReviewDetailEndpoint:
        '''Fields to return for included related types.

        :param app_clip_app_store_review_detail: the fields to include for returned resources of type appClipAppStoreReviewDetails
        :type app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipAppStoreReviewDetailEndpoint
        '''
        if app_clip_app_store_review_detail: self._set_fields('appClipAppStoreReviewDetails',app_clip_app_store_review_detail if type(app_clip_app_store_review_detail) is list else [app_clip_app_store_review_detail])
        return self
        
    class Include(StringEnum):
        APP_CLIP_DEFAULT_EXPERIENCE = 'appClipDefaultExperience'

    def include(self, relationship: Union[Include, list[Include]]) -> AppClipAppStoreReviewDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipAppStoreReviewDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppClipAppStoreReviewDetailResponse:
        '''Get the resource.

        :returns: Single AppClipAppStoreReviewDetail
        :rtype: AppClipAppStoreReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipAppStoreReviewDetailResponse.parse_obj(json)

    def update(self, request: AppClipAppStoreReviewDetailUpdateRequest) -> AppClipAppStoreReviewDetailResponse:
        '''Modify the resource.

        :param request: AppClipAppStoreReviewDetail representation
        :type request: AppClipAppStoreReviewDetailUpdateRequest

        :returns: Single AppClipAppStoreReviewDetail
        :rtype: AppClipAppStoreReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppClipAppStoreReviewDetailResponse.parse_obj(json)

