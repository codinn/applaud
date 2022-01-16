from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionReleaseRequestsEndpoint(Endpoint):
    path = '/v1/appStoreVersionReleaseRequests'

    def create(self, request: AppStoreVersionReleaseRequestCreateRequest) -> AppStoreVersionReleaseRequestResponse:
        '''Create the resource.

        :param request: AppStoreVersionReleaseRequest representation
        :type request: AppStoreVersionReleaseRequestCreateRequest

        :returns: Single AppStoreVersionReleaseRequest
        :rtype: AppStoreVersionReleaseRequestResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreVersionReleaseRequestResponse.parse_obj(json)

