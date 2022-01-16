from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaTesterInvitationsEndpoint(Endpoint):
    path = '/v1/betaTesterInvitations'

    def create(self, request: BetaTesterInvitationCreateRequest) -> BetaTesterInvitationResponse:
        '''Create the resource.

        :param request: BetaTesterInvitation representation
        :type request: BetaTesterInvitationCreateRequest

        :returns: Single BetaTesterInvitation
        :rtype: BetaTesterInvitationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BetaTesterInvitationResponse.parse_obj(json)

