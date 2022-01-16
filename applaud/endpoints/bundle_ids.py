from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BundleIdsEndpoint(Endpoint):
    path = '/v1/bundleIds'

    def fields(self, *, bundle_id: Union[BundleIdField, list[BundleIdField]]=None, bundle_id_capability: Union[BundleIdCapabilityField, list[BundleIdCapabilityField]]=None, profile: Union[ProfileField, list[ProfileField]]=None, app: Union[AppField, list[AppField]]=None) -> BundleIdsEndpoint:
        '''Fields to return for included related types.

        :param bundle_id: the fields to include for returned resources of type bundleIds
        :type bundle_id: Union[BundleIdField, list[BundleIdField]] = None

        :param bundle_id_capability: the fields to include for returned resources of type bundleIdCapabilities
        :type bundle_id_capability: Union[BundleIdCapabilityField, list[BundleIdCapabilityField]] = None

        :param profile: the fields to include for returned resources of type profiles
        :type profile: Union[ProfileField, list[ProfileField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.BundleIdsEndpoint
        '''
        if bundle_id: self._set_fields('bundleIds',bundle_id if type(bundle_id) is list else [bundle_id])
        if bundle_id_capability: self._set_fields('bundleIdCapabilities',bundle_id_capability if type(bundle_id_capability) is list else [bundle_id_capability])
        if profile: self._set_fields('profiles',profile if type(profile) is list else [profile])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BUNDLE_ID_CAPABILITIES = 'bundleIdCapabilities'
        PROFILES = 'profiles'

    def filter(self, *, identifier: Union[str, list[str]]=None, name: Union[str, list[str]]=None, platform: Union[BundleIdPlatform, list[BundleIdPlatform]]=None, seed_id: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> BundleIdsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param identifier: filter by attribute 'identifier'
        :type identifier: Union[str, list[str]] = None

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param platform: filter by attribute 'platform'
        :type platform: Union[BundleIdPlatform, list[BundleIdPlatform]] = None

        :param seed_id: filter by attribute 'seedId'
        :type seed_id: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BundleIdsEndpoint
        '''
        if identifier: self._set_filter('identifier', identifier if type(identifier) is list else [identifier])
        
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if seed_id: self._set_filter('seedId', seed_id if type(seed_id) is list else [seed_id])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BundleIdsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BundleIdsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, id: SortOrder=None, identifier: SortOrder=None, name: SortOrder=None, platform: SortOrder=None, seed_id: SortOrder=None) -> BundleIdsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BundleIdsEndpoint
        '''
        if id: self.sort_expressions.append('id' if id == SortOrder.ASC else '-id')
        if identifier: self.sort_expressions.append('identifier' if identifier == SortOrder.ASC else '-identifier')
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if platform: self.sort_expressions.append('platform' if platform == SortOrder.ASC else '-platform')
        if seed_id: self.sort_expressions.append('seedId' if seed_id == SortOrder.ASC else '-seedId')
        return self
        
    def limit(self, number: int=None, *, bundle_id_capabilities: int=None, profiles: int=None) -> BundleIdsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param bundle_id_capabilities: maximum number of related bundleIdCapabilities returned (when they are included). The maximum limit is 50
        :type bundle_id_capabilities: int = None

        :param profiles: maximum number of related profiles returned (when they are included). The maximum limit is 50
        :type profiles: int = None

        :returns: self
        :rtype: applaud.endpoints.BundleIdsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if bundle_id_capabilities and bundle_id_capabilities > 50:
            raise ValueError(f'The maximum limit is 50')
        if bundle_id_capabilities: self._set_limit('bundleIdCapabilities', bundle_id_capabilities)

        if profiles and profiles > 50:
            raise ValueError(f'The maximum limit is 50')
        if profiles: self._set_limit('profiles', profiles)

        return self

    def get(self) -> BundleIdsResponse:
        '''Get one or more resources.

        :returns: List of BundleIds
        :rtype: BundleIdsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BundleIdsResponse.parse_obj(json)

    def create(self, request: BundleIdCreateRequest) -> BundleIdResponse:
        '''Create the resource.

        :param request: BundleId representation
        :type request: BundleIdCreateRequest

        :returns: Single BundleId
        :rtype: BundleIdResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BundleIdResponse.parse_obj(json)

class BundleIdEndpoint(IDEndpoint):
    path = '/v1/bundleIds/{id}'

    @endpoint('/v1/bundleIds/{id}/app')
    def app(self) -> AppOfBundleIdEndpoint:
        return AppOfBundleIdEndpoint(self.id, self.session)
        
    @endpoint('/v1/bundleIds/{id}/bundleIdCapabilities')
    def bundle_id_capabilities(self) -> BundleIdCapabilitiesOfBundleIdEndpoint:
        return BundleIdCapabilitiesOfBundleIdEndpoint(self.id, self.session)
        
    @endpoint('/v1/bundleIds/{id}/profiles')
    def profiles(self) -> ProfilesOfBundleIdEndpoint:
        return ProfilesOfBundleIdEndpoint(self.id, self.session)
        
    def fields(self, *, bundle_id: Union[BundleIdField, list[BundleIdField]]=None, bundle_id_capability: Union[BundleIdCapabilityField, list[BundleIdCapabilityField]]=None, profile: Union[ProfileField, list[ProfileField]]=None, app: Union[AppField, list[AppField]]=None) -> BundleIdEndpoint:
        '''Fields to return for included related types.

        :param bundle_id: the fields to include for returned resources of type bundleIds
        :type bundle_id: Union[BundleIdField, list[BundleIdField]] = None

        :param bundle_id_capability: the fields to include for returned resources of type bundleIdCapabilities
        :type bundle_id_capability: Union[BundleIdCapabilityField, list[BundleIdCapabilityField]] = None

        :param profile: the fields to include for returned resources of type profiles
        :type profile: Union[ProfileField, list[ProfileField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.BundleIdEndpoint
        '''
        if bundle_id: self._set_fields('bundleIds',bundle_id if type(bundle_id) is list else [bundle_id])
        if bundle_id_capability: self._set_fields('bundleIdCapabilities',bundle_id_capability if type(bundle_id_capability) is list else [bundle_id_capability])
        if profile: self._set_fields('profiles',profile if type(profile) is list else [profile])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BUNDLE_ID_CAPABILITIES = 'bundleIdCapabilities'
        PROFILES = 'profiles'

    def include(self, relationship: Union[Include, list[Include]]) -> BundleIdEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BundleIdEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, bundle_id_capabilities: int=None, profiles: int=None) -> BundleIdEndpoint:
        '''Number of included related resources to return.

        :param bundle_id_capabilities: maximum number of related bundleIdCapabilities returned (when they are included). The maximum limit is 50
        :type bundle_id_capabilities: int = None

        :param profiles: maximum number of related profiles returned (when they are included). The maximum limit is 50
        :type profiles: int = None

        :returns: self
        :rtype: applaud.endpoints.BundleIdEndpoint
        '''
        if bundle_id_capabilities and bundle_id_capabilities > 50:
            raise ValueError(f'The maximum limit is 50')
        if bundle_id_capabilities: self._set_limit('bundleIdCapabilities', bundle_id_capabilities)

        if profiles and profiles > 50:
            raise ValueError(f'The maximum limit is 50')
        if profiles: self._set_limit('profiles', profiles)

        return self

    def get(self) -> BundleIdResponse:
        '''Get the resource.

        :returns: Single BundleId
        :rtype: BundleIdResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BundleIdResponse.parse_obj(json)

    def update(self, request: BundleIdUpdateRequest) -> BundleIdResponse:
        '''Modify the resource.

        :param request: BundleId representation
        :type request: BundleIdUpdateRequest

        :returns: Single BundleId
        :rtype: BundleIdResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BundleIdResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppOfBundleIdEndpoint(IDEndpoint):
    path = '/v1/bundleIds/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppOfBundleIdEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfBundleIdEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    def get(self) -> AppResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppResponse.parse_obj(json)

class BundleIdCapabilitiesOfBundleIdEndpoint(IDEndpoint):
    path = '/v1/bundleIds/{id}/bundleIdCapabilities'

    def fields(self, *, bundle_id_capability: Union[BundleIdCapabilityField, list[BundleIdCapabilityField]]=None) -> BundleIdCapabilitiesOfBundleIdEndpoint:
        '''Fields to return for included related types.

        :param bundle_id_capability: the fields to include for returned resources of type bundleIdCapabilities
        :type bundle_id_capability: Union[BundleIdCapabilityField, list[BundleIdCapabilityField]] = None

        :returns: self
        :rtype: applaud.endpoints.BundleIdCapabilitiesOfBundleIdEndpoint
        '''
        if bundle_id_capability: self._set_fields('bundleIdCapabilities',bundle_id_capability if type(bundle_id_capability) is list else [bundle_id_capability])
        return self
        
    def limit(self, number: int=None) -> BundleIdCapabilitiesOfBundleIdEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BundleIdCapabilitiesOfBundleIdEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BundleIdCapabilitiesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BundleIdCapabilitiesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BundleIdCapabilitiesResponse.parse_obj(json)

class ProfilesOfBundleIdEndpoint(IDEndpoint):
    path = '/v1/bundleIds/{id}/profiles'

    def fields(self, *, profile: Union[ProfileField, list[ProfileField]]=None) -> ProfilesOfBundleIdEndpoint:
        '''Fields to return for included related types.

        :param profile: the fields to include for returned resources of type profiles
        :type profile: Union[ProfileField, list[ProfileField]] = None

        :returns: self
        :rtype: applaud.endpoints.ProfilesOfBundleIdEndpoint
        '''
        if profile: self._set_fields('profiles',profile if type(profile) is list else [profile])
        return self
        
    def limit(self, number: int=None) -> ProfilesOfBundleIdEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ProfilesOfBundleIdEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> ProfilesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: ProfilesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ProfilesResponse.parse_obj(json)

