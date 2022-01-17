from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseEndpoint(IDEndpoint):
    path = '/v1/inAppPurchases/{id}'

    def fields(self, *, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None) -> InAppPurchaseEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseEndpoint
        '''
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        return self
        
    class Include(StringEnum):
        APPS = 'apps'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, apps: int=None) -> InAppPurchaseEndpoint:
        '''Number of included related resources to return.

        :param apps: maximum number of related apps returned (when they are included). The maximum limit is 50
        :type apps: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseEndpoint
        '''
        if apps and apps > 50:
            raise ValueError(f'The maximum limit of apps is 50')
        if apps: self._set_limit(apps, 'apps')

        return self

    def get(self) -> InAppPurchaseResponse:
        '''Get the resource.

        :returns: Single InAppPurchase
        :rtype: InAppPurchaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseResponse.parse_obj(json)

