from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionPhasedReleasesEndpoint(Endpoint):
    path = '/v1/appStoreVersionPhasedReleases'

    def create(self, request: AppStoreVersionPhasedReleaseCreateRequest) -> AppStoreVersionPhasedReleaseResponse:
        '''Create the resource.

        :param request: AppStoreVersionPhasedRelease representation
        :type request: AppStoreVersionPhasedReleaseCreateRequest

        :returns: Single AppStoreVersionPhasedRelease
        :rtype: AppStoreVersionPhasedReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreVersionPhasedReleaseResponse.parse_obj(json)

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
        json = super()._perform_patch(request)
        return AppStoreVersionPhasedReleaseResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

