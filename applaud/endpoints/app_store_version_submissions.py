from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionSubmissionListEndpoint(Endpoint):
    path = '/v1/appStoreVersionSubmissions'

    def create(self, request: AppStoreVersionSubmissionCreateRequest) -> AppStoreVersionSubmissionResponse:
        '''Create the resource.

        :param request: AppStoreVersionSubmission representation
        :type request: AppStoreVersionSubmissionCreateRequest

        :returns: Single AppStoreVersionSubmission
        :rtype: AppStoreVersionSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_post(json)
        return AppStoreVersionSubmissionResponse.parse_obj(response_json)

class AppStoreVersionSubmissionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionSubmissions/{id}'

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

