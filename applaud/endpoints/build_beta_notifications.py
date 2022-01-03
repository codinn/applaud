from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BuildBetaNotificationListEndpoint(Endpoint):
    path = '/v1/buildBetaNotifications'

    def create(self, request: BuildBetaNotificationCreateRequest) -> BuildBetaNotificationResponse:
        '''Create the resource.

        :param request: BuildBetaNotification representation
        :type request: BuildBetaNotificationCreateRequest

        :returns: Single BuildBetaNotification
        :rtype: BuildBetaNotificationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_post(json)
        return BuildBetaNotificationResponse.parse_obj(response_json)

