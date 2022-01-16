from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppPreOrdersEndpoint(Endpoint):
    path = '/v1/appPreOrders'

    def create(self, request: AppPreOrderCreateRequest) -> AppPreOrderResponse:
        '''Create the resource.

        :param request: AppPreOrder representation
        :type request: AppPreOrderCreateRequest

        :returns: Single AppPreOrder
        :rtype: AppPreOrderResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppPreOrderResponse.parse_obj(json)

class AppPreOrderEndpoint(IDEndpoint):
    path = '/v1/appPreOrders/{id}'

    def fields(self, *, app_pre_order: Union[AppPreOrderField, list[AppPreOrderField]]=None) -> AppPreOrderEndpoint:
        '''Fields to return for included related types.

        :param app_pre_order: the fields to include for returned resources of type appPreOrders
        :type app_pre_order: Union[AppPreOrderField, list[AppPreOrderField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPreOrderEndpoint
        '''
        if app_pre_order: self._set_fields('appPreOrders',app_pre_order if type(app_pre_order) is list else [app_pre_order])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def include(self, relationship: Union[Include, list[Include]]) -> AppPreOrderEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPreOrderEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppPreOrderResponse:
        '''Get the resource.

        :returns: Single AppPreOrder
        :rtype: AppPreOrderResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPreOrderResponse.parse_obj(json)

    def update(self, request: AppPreOrderUpdateRequest) -> AppPreOrderResponse:
        '''Modify the resource.

        :param request: AppPreOrder representation
        :type request: AppPreOrderUpdateRequest

        :returns: Single AppPreOrder
        :rtype: AppPreOrderResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppPreOrderResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

