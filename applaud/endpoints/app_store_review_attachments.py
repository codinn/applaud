from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreReviewAttachmentsEndpoint(Endpoint):
    path = '/v1/appStoreReviewAttachments'

    def create(self, request: AppStoreReviewAttachmentCreateRequest) -> AppStoreReviewAttachmentResponse:
        '''Create the resource.

        :param request: AppStoreReviewAttachment representation
        :type request: AppStoreReviewAttachmentCreateRequest

        :returns: Single AppStoreReviewAttachment
        :rtype: AppStoreReviewAttachmentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreReviewAttachmentResponse.parse_obj(json)

class AppStoreReviewAttachmentEndpoint(IDEndpoint):
    path = '/v1/appStoreReviewAttachments/{id}'

    def fields(self, *, app_store_review_attachment: Union[AppStoreReviewAttachmentField, list[AppStoreReviewAttachmentField]]=None) -> AppStoreReviewAttachmentEndpoint:
        '''Fields to return for included related types.

        :param app_store_review_attachment: the fields to include for returned resources of type appStoreReviewAttachments
        :type app_store_review_attachment: Union[AppStoreReviewAttachmentField, list[AppStoreReviewAttachmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewAttachmentEndpoint
        '''
        if app_store_review_attachment: self._set_fields('appStoreReviewAttachments',app_store_review_attachment if type(app_store_review_attachment) is list else [app_store_review_attachment])
        return self
        
    class Include(StringEnum):
        APP_STORE_REVIEW_DETAIL = 'appStoreReviewDetail'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreReviewAttachmentEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewAttachmentEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppStoreReviewAttachmentResponse:
        '''Get the resource.

        :returns: Single AppStoreReviewAttachment
        :rtype: AppStoreReviewAttachmentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreReviewAttachmentResponse.parse_obj(json)

    def update(self, request: AppStoreReviewAttachmentUpdateRequest) -> AppStoreReviewAttachmentResponse:
        '''Modify the resource.

        :param request: AppStoreReviewAttachment representation
        :type request: AppStoreReviewAttachmentUpdateRequest

        :returns: Single AppStoreReviewAttachment
        :rtype: AppStoreReviewAttachmentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppStoreReviewAttachmentResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

