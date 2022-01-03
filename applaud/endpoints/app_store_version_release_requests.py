from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionReleaseRequestListEndpoint(Endpoint):
    path = '/v1/appStoreVersionReleaseRequests'

    def create(self, request: AppStoreVersionReleaseRequestCreateRequest) -> AppStoreVersionReleaseRequestResponse:
        '''Create the resource.

        :param request: AppStoreVersionReleaseRequest representation
        :type request: AppStoreVersionReleaseRequestCreateRequest

        :returns: Single AppStoreVersionReleaseRequest
        :rtype: AppStoreVersionReleaseRequestResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_post(json)
        return AppStoreVersionReleaseRequestResponse.parse_obj(response_json)

