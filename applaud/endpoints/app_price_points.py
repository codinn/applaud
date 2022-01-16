from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppPricePointsEndpoint(Endpoint):
    path = '/v1/appPricePoints'

    def fields(self, *, app_price_point: Union[AppPricePointField, list[AppPricePointField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> AppPricePointsEndpoint:
        '''Fields to return for included related types.

        :param app_price_point: the fields to include for returned resources of type appPricePoints
        :type app_price_point: Union[AppPricePointField, list[AppPricePointField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPricePointsEndpoint
        '''
        if app_price_point: self._set_fields('appPricePoints',app_price_point if type(app_price_point) is list else [app_price_point])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        PRICE_TIER = 'priceTier'
        TERRITORY = 'territory'

    def filter(self, *, price_tier: Union[str, list[str]]=None, territory: Union[str, list[str]]=None) -> AppPricePointsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param price_tier: filter by id(s) of related 'priceTier'
        :type price_tier: Union[str, list[str]] = None

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPricePointsEndpoint
        '''
        if price_tier: self._set_filter('priceTier', price_tier if type(price_tier) is list else [price_tier])
        
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppPricePointsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPricePointsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> AppPricePointsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPricePointsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> AppPricePointsResponse:
        '''Get one or more resources.

        :returns: List of AppPricePoints
        :rtype: AppPricePointsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPricePointsResponse.parse_obj(json)

class AppPricePointEndpoint(IDEndpoint):
    path = '/v1/appPricePoints/{id}'

    @endpoint('/v1/appPricePoints/{id}/territory')
    def territory(self) -> TerritoryOfAppPricePointEndpoint:
        return TerritoryOfAppPricePointEndpoint(self.id, self.session)
        
    def fields(self, *, app_price_point: Union[AppPricePointField, list[AppPricePointField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> AppPricePointEndpoint:
        '''Fields to return for included related types.

        :param app_price_point: the fields to include for returned resources of type appPricePoints
        :type app_price_point: Union[AppPricePointField, list[AppPricePointField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPricePointEndpoint
        '''
        if app_price_point: self._set_fields('appPricePoints',app_price_point if type(app_price_point) is list else [app_price_point])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        PRICE_TIER = 'priceTier'
        TERRITORY = 'territory'

    def include(self, relationship: Union[Include, list[Include]]) -> AppPricePointEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPricePointEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppPricePointResponse:
        '''Get the resource.

        :returns: Single AppPricePoint
        :rtype: AppPricePointResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPricePointResponse.parse_obj(json)

class TerritoryOfAppPricePointEndpoint(IDEndpoint):
    path = '/v1/appPricePoints/{id}/territory'

    def fields(self, *, territory: Union[TerritoryField, list[TerritoryField]]=None) -> TerritoryOfAppPricePointEndpoint:
        '''Fields to return for included related types.

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.TerritoryOfAppPricePointEndpoint
        '''
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    def get(self) -> TerritoryResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: TerritoryResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return TerritoryResponse.parse_obj(json)

