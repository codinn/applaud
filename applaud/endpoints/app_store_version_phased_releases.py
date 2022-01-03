from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionPhasedReleaseListEndpoint(Endpoint):
    path = '/v1/appStoreVersionPhasedReleases'

    def create(self, request: AppStoreVersionPhasedReleaseCreateRequest) -> AppStoreVersionPhasedReleaseResponse:
        '''Create the resource.

        :param request: AppStoreVersionPhasedRelease representation
        :type request: AppStoreVersionPhasedReleaseCreateRequest

        :returns: Single AppStoreVersionPhasedRelease
        :rtype: AppStoreVersionPhasedReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_post(json)
        return AppStoreVersionPhasedReleaseResponse.parse_obj(response_json)

class AppStoreVersionPhasedReleaseEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionPhasedReleases/{id}'

    def update(self, request: AppStoreVersionPhasedReleaseUpdateRequest) -> AppStoreVersionPhasedReleaseResponse:
        '''Modify the resource.

        :param request: AppStoreVersionPhasedRelease representation
        :type request: AppStoreVersionPhasedReleaseUpdateRequest

        :returns: Single AppStoreVersionPhasedRelease
        :rtype: AppStoreVersionPhasedReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_patch(json)
        return AppStoreVersionPhasedReleaseResponse.parse_obj(response_json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

