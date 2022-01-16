from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BundleIdCapabilitiesEndpoint(Endpoint):
    path = '/v1/bundleIdCapabilities'

    def create(self, request: BundleIdCapabilityCreateRequest) -> BundleIdCapabilityResponse:
        '''Create the resource.

        :param request: BundleIdCapability representation
        :type request: BundleIdCapabilityCreateRequest

        :returns: Single BundleIdCapability
        :rtype: BundleIdCapabilityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BundleIdCapabilityResponse.parse_obj(json)

class BundleIdCapabilityEndpoint(IDEndpoint):
    path = '/v1/bundleIdCapabilities/{id}'

    def update(self, request: BundleIdCapabilityUpdateRequest) -> BundleIdCapabilityResponse:
        '''Modify the resource.

        :param request: BundleIdCapability representation
        :type request: BundleIdCapabilityUpdateRequest

        :returns: Single BundleIdCapability
        :rtype: BundleIdCapabilityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BundleIdCapabilityResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

