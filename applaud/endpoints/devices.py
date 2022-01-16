from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class DevicesEndpoint(Endpoint):
    path = '/v1/devices'

    def fields(self, *, device: Union[DeviceField, list[DeviceField]]=None) -> DevicesEndpoint:
        '''Fields to return for included related types.

        :param device: the fields to include for returned resources of type devices
        :type device: Union[DeviceField, list[DeviceField]] = None

        :returns: self
        :rtype: applaud.endpoints.DevicesEndpoint
        '''
        if device: self._set_fields('devices',device if type(device) is list else [device])
        return self
        
    def filter(self, *, name: Union[str, list[str]]=None, platform: Union[BundleIdPlatform, list[BundleIdPlatform]]=None, status: Union[DeviceStatus, list[DeviceStatus]]=None, udid: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> DevicesEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param platform: filter by attribute 'platform'
        :type platform: Union[BundleIdPlatform, list[BundleIdPlatform]] = None

        :param status: filter by attribute 'status'
        :type status: Union[DeviceStatus, list[DeviceStatus]] = None

        :param udid: filter by attribute 'udid'
        :type udid: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.DevicesEndpoint
        '''
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if status: self._set_filter('status', status if type(status) is list else [status])
        
        if udid: self._set_filter('udid', udid if type(udid) is list else [udid])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def sort(self, *, id: SortOrder=None, name: SortOrder=None, platform: SortOrder=None, statu: SortOrder=None, udid: SortOrder=None) -> DevicesEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.DevicesEndpoint
        '''
        if id: self.sort_expressions.append('id' if id == SortOrder.ASC else '-id')
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if platform: self.sort_expressions.append('platform' if platform == SortOrder.ASC else '-platform')
        if statu: self.sort_expressions.append('status' if statu == SortOrder.ASC else '-status')
        if udid: self.sort_expressions.append('udid' if udid == SortOrder.ASC else '-udid')
        return self
        
    def limit(self, number: int=None) -> DevicesEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DevicesEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> DevicesResponse:
        '''Get one or more resources.

        :returns: List of Devices
        :rtype: DevicesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return DevicesResponse.parse_obj(json)

    def create(self, request: DeviceCreateRequest) -> DeviceResponse:
        '''Create the resource.

        :param request: Device representation
        :type request: DeviceCreateRequest

        :returns: Single Device
        :rtype: DeviceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return DeviceResponse.parse_obj(json)

class DeviceEndpoint(IDEndpoint):
    path = '/v1/devices/{id}'

    def fields(self, *, device: Union[DeviceField, list[DeviceField]]=None) -> DeviceEndpoint:
        '''Fields to return for included related types.

        :param device: the fields to include for returned resources of type devices
        :type device: Union[DeviceField, list[DeviceField]] = None

        :returns: self
        :rtype: applaud.endpoints.DeviceEndpoint
        '''
        if device: self._set_fields('devices',device if type(device) is list else [device])
        return self
        
    def get(self) -> DeviceResponse:
        '''Get the resource.

        :returns: Single Device
        :rtype: DeviceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return DeviceResponse.parse_obj(json)

    def update(self, request: DeviceUpdateRequest) -> DeviceResponse:
        '''Modify the resource.

        :param request: Device representation
        :type request: DeviceUpdateRequest

        :returns: Single Device
        :rtype: DeviceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return DeviceResponse.parse_obj(json)

