from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BuildBetaNotificationsEndpoint(Endpoint):
    path = '/v1/buildBetaNotifications'

    def create(self, request: BuildBetaNotificationCreateRequest) -> BuildBetaNotificationResponse:
        '''Create the resource.

        :param request: BuildBetaNotification representation
        :type request: BuildBetaNotificationCreateRequest

        :returns: Single BuildBetaNotification
        :rtype: BuildBetaNotificationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BuildBetaNotificationResponse.parse_obj(json)

