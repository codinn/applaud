from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class RoutingAppCoveragesEndpoint(Endpoint):
    path = '/v1/routingAppCoverages'

    def create(self, request: RoutingAppCoverageCreateRequest) -> RoutingAppCoverageResponse:
        '''Create the resource.

        :param request: RoutingAppCoverage representation
        :type request: RoutingAppCoverageCreateRequest

        :returns: Single RoutingAppCoverage
        :rtype: RoutingAppCoverageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return RoutingAppCoverageResponse.parse_obj(json)

class RoutingAppCoverageEndpoint(IDEndpoint):
    path = '/v1/routingAppCoverages/{id}'

    def fields(self, *, routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]]=None) -> RoutingAppCoverageEndpoint:
        '''Fields to return for included related types.

        :param routing_app_coverage: the fields to include for returned resources of type routingAppCoverages
        :type routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]] = None

        :returns: self
        :rtype: applaud.endpoints.RoutingAppCoverageEndpoint
        '''
        if routing_app_coverage: self._set_fields('routingAppCoverages',routing_app_coverage if type(routing_app_coverage) is list else [routing_app_coverage])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION = 'appStoreVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> RoutingAppCoverageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.RoutingAppCoverageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> RoutingAppCoverageResponse:
        '''Get the resource.

        :returns: Single RoutingAppCoverage
        :rtype: RoutingAppCoverageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return RoutingAppCoverageResponse.parse_obj(json)

    def update(self, request: RoutingAppCoverageUpdateRequest) -> RoutingAppCoverageResponse:
        '''Modify the resource.

        :param request: RoutingAppCoverage representation
        :type request: RoutingAppCoverageUpdateRequest

        :returns: Single RoutingAppCoverage
        :rtype: RoutingAppCoverageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return RoutingAppCoverageResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

