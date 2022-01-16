from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreReviewDetailsEndpoint(Endpoint):
    path = '/v1/appStoreReviewDetails'

    def create(self, request: AppStoreReviewDetailCreateRequest) -> AppStoreReviewDetailResponse:
        '''Create the resource.

        :param request: AppStoreReviewDetail representation
        :type request: AppStoreReviewDetailCreateRequest

        :returns: Single AppStoreReviewDetail
        :rtype: AppStoreReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreReviewDetailResponse.parse_obj(json)

class AppStoreReviewDetailEndpoint(IDEndpoint):
    path = '/v1/appStoreReviewDetails/{id}'

    @endpoint('/v1/appStoreReviewDetails/{id}/appStoreReviewAttachments')
    def app_store_review_attachments(self) -> AppStoreReviewAttachmentsOfAppStoreReviewDetailEndpoint:
        return AppStoreReviewAttachmentsOfAppStoreReviewDetailEndpoint(self.id, self.session)
        
    def fields(self, *, app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]]=None, app_store_review_attachment: Union[AppStoreReviewAttachmentField, list[AppStoreReviewAttachmentField]]=None) -> AppStoreReviewDetailEndpoint:
        '''Fields to return for included related types.

        :param app_store_review_detail: the fields to include for returned resources of type appStoreReviewDetails
        :type app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]] = None

        :param app_store_review_attachment: the fields to include for returned resources of type appStoreReviewAttachments
        :type app_store_review_attachment: Union[AppStoreReviewAttachmentField, list[AppStoreReviewAttachmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewDetailEndpoint
        '''
        if app_store_review_detail: self._set_fields('appStoreReviewDetails',app_store_review_detail if type(app_store_review_detail) is list else [app_store_review_detail])
        if app_store_review_attachment: self._set_fields('appStoreReviewAttachments',app_store_review_attachment if type(app_store_review_attachment) is list else [app_store_review_attachment])
        return self
        
    class Include(StringEnum):
        APP_STORE_REVIEW_ATTACHMENTS = 'appStoreReviewAttachments'
        APP_STORE_VERSION = 'appStoreVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreReviewDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_review_attachments: int=None) -> AppStoreReviewDetailEndpoint:
        '''Number of included related resources to return.

        :param app_store_review_attachments: maximum number of related appStoreReviewAttachments returned (when they are included). The maximum limit is 50
        :type app_store_review_attachments: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewDetailEndpoint
        '''
        if app_store_review_attachments and app_store_review_attachments > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_store_review_attachments: self._set_limit('appStoreReviewAttachments', app_store_review_attachments)

        return self

    def get(self) -> AppStoreReviewDetailResponse:
        '''Get the resource.

        :returns: Single AppStoreReviewDetail
        :rtype: AppStoreReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreReviewDetailResponse.parse_obj(json)

    def update(self, request: AppStoreReviewDetailUpdateRequest) -> AppStoreReviewDetailResponse:
        '''Modify the resource.

        :param request: AppStoreReviewDetail representation
        :type request: AppStoreReviewDetailUpdateRequest

        :returns: Single AppStoreReviewDetail
        :rtype: AppStoreReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppStoreReviewDetailResponse.parse_obj(json)

class AppStoreReviewAttachmentsOfAppStoreReviewDetailEndpoint(IDEndpoint):
    path = '/v1/appStoreReviewDetails/{id}/appStoreReviewAttachments'

    def fields(self, *, app_store_review_attachment: Union[AppStoreReviewAttachmentField, list[AppStoreReviewAttachmentField]]=None) -> AppStoreReviewAttachmentsOfAppStoreReviewDetailEndpoint:
        '''Fields to return for included related types.

        :param app_store_review_attachment: the fields to include for returned resources of type appStoreReviewAttachments
        :type app_store_review_attachment: Union[AppStoreReviewAttachmentField, list[AppStoreReviewAttachmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewAttachmentsOfAppStoreReviewDetailEndpoint
        '''
        if app_store_review_attachment: self._set_fields('appStoreReviewAttachments',app_store_review_attachment if type(app_store_review_attachment) is list else [app_store_review_attachment])
        return self
        
    def limit(self, number: int=None) -> AppStoreReviewAttachmentsOfAppStoreReviewDetailEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewAttachmentsOfAppStoreReviewDetailEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> AppStoreReviewAttachmentsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppStoreReviewAttachmentsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreReviewAttachmentsResponse.parse_obj(json)

