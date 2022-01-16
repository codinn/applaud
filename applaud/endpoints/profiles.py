from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class ProfilesEndpoint(Endpoint):
    path = '/v1/profiles'

    def fields(self, *, profile: Union[ProfileField, list[ProfileField]]=None, certificate: Union[CertificateField, list[CertificateField]]=None, device: Union[DeviceField, list[DeviceField]]=None, bundle_id: Union[BundleIdField, list[BundleIdField]]=None) -> ProfilesEndpoint:
        '''Fields to return for included related types.

        :param profile: the fields to include for returned resources of type profiles
        :type profile: Union[ProfileField, list[ProfileField]] = None

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :param device: the fields to include for returned resources of type devices
        :type device: Union[DeviceField, list[DeviceField]] = None

        :param bundle_id: the fields to include for returned resources of type bundleIds
        :type bundle_id: Union[BundleIdField, list[BundleIdField]] = None

        :returns: self
        :rtype: applaud.endpoints.ProfilesEndpoint
        '''
        if profile: self._set_fields('profiles',profile if type(profile) is list else [profile])
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        if device: self._set_fields('devices',device if type(device) is list else [device])
        if bundle_id: self._set_fields('bundleIds',bundle_id if type(bundle_id) is list else [bundle_id])
        return self
        
    class Include(StringEnum):
        BUNDLE_ID = 'bundleId'
        CERTIFICATES = 'certificates'
        DEVICES = 'devices'

    def filter(self, *, name: Union[str, list[str]]=None, profile_state: Union[ProfileState, list[ProfileState]]=None, profile_type: Union[ProfileType, list[ProfileType]]=None, id: Union[str, list[str]]=None) -> ProfilesEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param profile_state: filter by attribute 'profileState'
        :type profile_state: Union[ProfileState, list[ProfileState]] = None

        :param profile_type: filter by attribute 'profileType'
        :type profile_type: Union[ProfileType, list[ProfileType]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.ProfilesEndpoint
        '''
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if profile_state: self._set_filter('profileState', profile_state if type(profile_state) is list else [profile_state])
        
        if profile_type: self._set_filter('profileType', profile_type if type(profile_type) is list else [profile_type])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> ProfilesEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ProfilesEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, id: SortOrder=None, name: SortOrder=None, profile_state: SortOrder=None, profile_type: SortOrder=None) -> ProfilesEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.ProfilesEndpoint
        '''
        if id: self.sort_expressions.append('id' if id == SortOrder.ASC else '-id')
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if profile_state: self.sort_expressions.append('profileState' if profile_state == SortOrder.ASC else '-profileState')
        if profile_type: self.sort_expressions.append('profileType' if profile_type == SortOrder.ASC else '-profileType')
        return self
        
    def limit(self, number: int=None, *, certificates: int=None, devices: int=None) -> ProfilesEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param certificates: maximum number of related certificates returned (when they are included). The maximum limit is 50
        :type certificates: int = None

        :param devices: maximum number of related devices returned (when they are included). The maximum limit is 50
        :type devices: int = None

        :returns: self
        :rtype: applaud.endpoints.ProfilesEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if certificates and certificates > 50:
            raise ValueError(f'The maximum limit is 50')
        if certificates: self._set_limit('certificates', certificates)

        if devices and devices > 50:
            raise ValueError(f'The maximum limit is 50')
        if devices: self._set_limit('devices', devices)

        return self

    def get(self) -> ProfilesResponse:
        '''Get one or more resources.

        :returns: List of Profiles
        :rtype: ProfilesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ProfilesResponse.parse_obj(json)

    def create(self, request: ProfileCreateRequest) -> ProfileResponse:
        '''Create the resource.

        :param request: Profile representation
        :type request: ProfileCreateRequest

        :returns: Single Profile
        :rtype: ProfileResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return ProfileResponse.parse_obj(json)

class ProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}'

    @endpoint('/v1/profiles/{id}/bundleId')
    def bundle_id(self) -> BundleIdOfProfileEndpoint:
        return BundleIdOfProfileEndpoint(self.id, self.session)
        
    @endpoint('/v1/profiles/{id}/certificates')
    def certificates(self) -> CertificatesOfProfileEndpoint:
        return CertificatesOfProfileEndpoint(self.id, self.session)
        
    @endpoint('/v1/profiles/{id}/devices')
    def devices(self) -> DevicesOfProfileEndpoint:
        return DevicesOfProfileEndpoint(self.id, self.session)
        
    def fields(self, *, profile: Union[ProfileField, list[ProfileField]]=None, certificate: Union[CertificateField, list[CertificateField]]=None, device: Union[DeviceField, list[DeviceField]]=None, bundle_id: Union[BundleIdField, list[BundleIdField]]=None) -> ProfileEndpoint:
        '''Fields to return for included related types.

        :param profile: the fields to include for returned resources of type profiles
        :type profile: Union[ProfileField, list[ProfileField]] = None

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :param device: the fields to include for returned resources of type devices
        :type device: Union[DeviceField, list[DeviceField]] = None

        :param bundle_id: the fields to include for returned resources of type bundleIds
        :type bundle_id: Union[BundleIdField, list[BundleIdField]] = None

        :returns: self
        :rtype: applaud.endpoints.ProfileEndpoint
        '''
        if profile: self._set_fields('profiles',profile if type(profile) is list else [profile])
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        if device: self._set_fields('devices',device if type(device) is list else [device])
        if bundle_id: self._set_fields('bundleIds',bundle_id if type(bundle_id) is list else [bundle_id])
        return self
        
    class Include(StringEnum):
        BUNDLE_ID = 'bundleId'
        CERTIFICATES = 'certificates'
        DEVICES = 'devices'

    def include(self, relationship: Union[Include, list[Include]]) -> ProfileEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ProfileEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, certificates: int=None, devices: int=None) -> ProfileEndpoint:
        '''Number of included related resources to return.

        :param certificates: maximum number of related certificates returned (when they are included). The maximum limit is 50
        :type certificates: int = None

        :param devices: maximum number of related devices returned (when they are included). The maximum limit is 50
        :type devices: int = None

        :returns: self
        :rtype: applaud.endpoints.ProfileEndpoint
        '''
        if certificates and certificates > 50:
            raise ValueError(f'The maximum limit is 50')
        if certificates: self._set_limit('certificates', certificates)

        if devices and devices > 50:
            raise ValueError(f'The maximum limit is 50')
        if devices: self._set_limit('devices', devices)

        return self

    def get(self) -> ProfileResponse:
        '''Get the resource.

        :returns: Single Profile
        :rtype: ProfileResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ProfileResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class BundleIdOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/bundleId'

    def fields(self, *, bundle_id: Union[BundleIdField, list[BundleIdField]]=None) -> BundleIdOfProfileEndpoint:
        '''Fields to return for included related types.

        :param bundle_id: the fields to include for returned resources of type bundleIds
        :type bundle_id: Union[BundleIdField, list[BundleIdField]] = None

        :returns: self
        :rtype: applaud.endpoints.BundleIdOfProfileEndpoint
        '''
        if bundle_id: self._set_fields('bundleIds',bundle_id if type(bundle_id) is list else [bundle_id])
        return self
        
    def get(self) -> BundleIdResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: BundleIdResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BundleIdResponse.parse_obj(json)

class CertificatesOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/certificates'

    def fields(self, *, certificate: Union[CertificateField, list[CertificateField]]=None) -> CertificatesOfProfileEndpoint:
        '''Fields to return for included related types.

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfProfileEndpoint
        '''
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    def limit(self, number: int=None) -> CertificatesOfProfileEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesOfProfileEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> CertificatesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: CertificatesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CertificatesResponse.parse_obj(json)

class DevicesOfProfileEndpoint(IDEndpoint):
    path = '/v1/profiles/{id}/devices'

    def fields(self, *, device: Union[DeviceField, list[DeviceField]]=None) -> DevicesOfProfileEndpoint:
        '''Fields to return for included related types.

        :param device: the fields to include for returned resources of type devices
        :type device: Union[DeviceField, list[DeviceField]] = None

        :returns: self
        :rtype: applaud.endpoints.DevicesOfProfileEndpoint
        '''
        if device: self._set_fields('devices',device if type(device) is list else [device])
        return self
        
    def limit(self, number: int=None) -> DevicesOfProfileEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DevicesOfProfileEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> DevicesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: DevicesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return DevicesResponse.parse_obj(json)

