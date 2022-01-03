from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaAppClipInvocationLocalizationListEndpoint(Endpoint):
    path = '/v1/betaAppClipInvocationLocalizations'

    def create(self, request: BetaAppClipInvocationLocalizationCreateRequest) -> BetaAppClipInvocationLocalizationResponse:
        '''Create the resource.

        :param request: BetaAppClipInvocationLocalization representation
        :type request: BetaAppClipInvocationLocalizationCreateRequest

        :returns: Single BetaAppClipInvocationLocalization
        :rtype: BetaAppClipInvocationLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_post(json)
        return BetaAppClipInvocationLocalizationResponse.parse_obj(response_json)

class BetaAppClipInvocationLocalizationEndpoint(IDEndpoint):
    path = '/v1/betaAppClipInvocationLocalizations/{id}'

    def update(self, request: BetaAppClipInvocationLocalizationUpdateRequest) -> BetaAppClipInvocationLocalizationResponse:
        '''Modify the resource.

        :param request: BetaAppClipInvocationLocalization representation
        :type request: BetaAppClipInvocationLocalizationUpdateRequest

        :returns: Single BetaAppClipInvocationLocalization
        :rtype: BetaAppClipInvocationLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_patch(json)
        return BetaAppClipInvocationLocalizationResponse.parse_obj(response_json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

