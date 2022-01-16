from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppPriceEndpoint(IDEndpoint):
    path = '/v1/appPrices/{id}'

    def fields(self, *, app_price: Union[AppPriceField, list[AppPriceField]]=None) -> AppPriceEndpoint:
        '''Fields to return for included related types.

        :param app_price: the fields to include for returned resources of type appPrices
        :type app_price: Union[AppPriceField, list[AppPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPriceEndpoint
        '''
        if app_price: self._set_fields('appPrices',app_price if type(app_price) is list else [app_price])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        PRICE_TIER = 'priceTier'

    def include(self, relationship: Union[Include, list[Include]]) -> AppPriceEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPriceEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppPriceResponse:
        '''Get the resource.

        :returns: Single AppPrice
        :rtype: AppPriceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPriceResponse.parse_obj(json)

