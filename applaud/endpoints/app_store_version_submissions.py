from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionSubmissionsEndpoint(Endpoint):
    path = '/v1/appStoreVersionSubmissions'

    def create(self, request: AppStoreVersionSubmissionCreateRequest) -> AppStoreVersionSubmissionResponse:
        '''Create the resource.

        :param request: AppStoreVersionSubmission representation
        :type request: AppStoreVersionSubmissionCreateRequest

        :returns: Single AppStoreVersionSubmission
        :rtype: AppStoreVersionSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreVersionSubmissionResponse.parse_obj(json)

class AppStoreVersionSubmissionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionSubmissions/{id}'

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

