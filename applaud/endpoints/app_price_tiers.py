from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppPriceTiersEndpoint(Endpoint):
    path = '/v1/appPriceTiers'

    def fields(self, *, app_price_tier: Union[AppPriceTierField, list[AppPriceTierField]]=None, app_price_point: Union[AppPricePointField, list[AppPricePointField]]=None) -> AppPriceTiersEndpoint:
        '''Fields to return for included related types.

        :param app_price_tier: the fields to include for returned resources of type appPriceTiers
        :type app_price_tier: Union[AppPriceTierField, list[AppPriceTierField]] = None

        :param app_price_point: the fields to include for returned resources of type appPricePoints
        :type app_price_point: Union[AppPricePointField, list[AppPricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPriceTiersEndpoint
        '''
        if app_price_tier: self._set_fields('appPriceTiers',app_price_tier if type(app_price_tier) is list else [app_price_tier])
        if app_price_point: self._set_fields('appPricePoints',app_price_point if type(app_price_point) is list else [app_price_point])
        return self
        
    class Include(StringEnum):
        PRICE_POINTS = 'pricePoints'

    def filter(self, *, id: Union[str, list[str]]=None) -> AppPriceTiersEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPriceTiersEndpoint
        '''
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppPriceTiersEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPriceTiersEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, price_points: int=None) -> AppPriceTiersEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param price_points: maximum number of related pricePoints returned (when they are included). The maximum limit is 50
        :type price_points: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPriceTiersEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if price_points and price_points > 50:
            raise ValueError(f'The maximum limit is 50')
        if price_points: self._set_limit('pricePoints', price_points)

        return self

    def get(self) -> AppPriceTiersResponse:
        '''Get one or more resources.

        :returns: List of AppPriceTiers
        :rtype: AppPriceTiersResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPriceTiersResponse.parse_obj(json)

class AppPriceTierEndpoint(IDEndpoint):
    path = '/v1/appPriceTiers/{id}'

    @endpoint('/v1/appPriceTiers/{id}/pricePoints')
    def price_points(self) -> PricePointsOfAppPriceTierEndpoint:
        return PricePointsOfAppPriceTierEndpoint(self.id, self.session)
        
    def fields(self, *, app_price_tier: Union[AppPriceTierField, list[AppPriceTierField]]=None, app_price_point: Union[AppPricePointField, list[AppPricePointField]]=None) -> AppPriceTierEndpoint:
        '''Fields to return for included related types.

        :param app_price_tier: the fields to include for returned resources of type appPriceTiers
        :type app_price_tier: Union[AppPriceTierField, list[AppPriceTierField]] = None

        :param app_price_point: the fields to include for returned resources of type appPricePoints
        :type app_price_point: Union[AppPricePointField, list[AppPricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPriceTierEndpoint
        '''
        if app_price_tier: self._set_fields('appPriceTiers',app_price_tier if type(app_price_tier) is list else [app_price_tier])
        if app_price_point: self._set_fields('appPricePoints',app_price_point if type(app_price_point) is list else [app_price_point])
        return self
        
    class Include(StringEnum):
        PRICE_POINTS = 'pricePoints'

    def include(self, relationship: Union[Include, list[Include]]) -> AppPriceTierEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPriceTierEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, price_points: int=None) -> AppPriceTierEndpoint:
        '''Number of included related resources to return.

        :param price_points: maximum number of related pricePoints returned (when they are included). The maximum limit is 50
        :type price_points: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPriceTierEndpoint
        '''
        if price_points and price_points > 50:
            raise ValueError(f'The maximum limit is 50')
        if price_points: self._set_limit('pricePoints', price_points)

        return self

    def get(self) -> AppPriceTierResponse:
        '''Get the resource.

        :returns: Single AppPriceTier
        :rtype: AppPriceTierResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPriceTierResponse.parse_obj(json)

class PricePointsOfAppPriceTierEndpoint(IDEndpoint):
    path = '/v1/appPriceTiers/{id}/pricePoints'

    def fields(self, *, app_price_point: Union[AppPricePointField, list[AppPricePointField]]=None) -> PricePointsOfAppPriceTierEndpoint:
        '''Fields to return for included related types.

        :param app_price_point: the fields to include for returned resources of type appPricePoints
        :type app_price_point: Union[AppPricePointField, list[AppPricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.PricePointsOfAppPriceTierEndpoint
        '''
        if app_price_point: self._set_fields('appPricePoints',app_price_point if type(app_price_point) is list else [app_price_point])
        return self
        
    def limit(self, number: int=None) -> PricePointsOfAppPriceTierEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricePointsOfAppPriceTierEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> AppPricePointsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppPricePointsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPricePointsResponse.parse_obj(json)

