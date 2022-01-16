from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiXcodeVersionsEndpoint(Endpoint):
    path = '/v1/ciXcodeVersions'

    def fields(self, *, ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]]=None, ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]]=None) -> CiXcodeVersionsEndpoint:
        '''Fields to return for included related types.

        :param ci_xcode_version: the fields to include for returned resources of type ciXcodeVersions
        :type ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]] = None

        :param ci_mac_os_version: the fields to include for returned resources of type ciMacOsVersions
        :type ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiXcodeVersionsEndpoint
        '''
        if ci_xcode_version: self._set_fields('ciXcodeVersions',ci_xcode_version if type(ci_xcode_version) is list else [ci_xcode_version])
        if ci_mac_os_version: self._set_fields('ciMacOsVersions',ci_mac_os_version if type(ci_mac_os_version) is list else [ci_mac_os_version])
        return self
        
    class Include(StringEnum):
        MAC_OS_VERSIONS = 'macOsVersions'

    def include(self, relationship: Union[Include, list[Include]]) -> CiXcodeVersionsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiXcodeVersionsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, mac_os_versions: int=None) -> CiXcodeVersionsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param mac_os_versions: maximum number of related macOsVersions returned (when they are included). The maximum limit is 50
        :type mac_os_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.CiXcodeVersionsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if mac_os_versions and mac_os_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if mac_os_versions: self._set_limit('macOsVersions', mac_os_versions)

        return self

    def get(self) -> CiXcodeVersionsResponse:
        '''Get one or more resources.

        :returns: List of CiXcodeVersions
        :rtype: CiXcodeVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiXcodeVersionsResponse.parse_obj(json)

class CiXcodeVersionEndpoint(IDEndpoint):
    path = '/v1/ciXcodeVersions/{id}'

    @endpoint('/v1/ciXcodeVersions/{id}/macOsVersions')
    def mac_os_versions(self) -> MacOsVersionsOfCiXcodeVersionEndpoint:
        return MacOsVersionsOfCiXcodeVersionEndpoint(self.id, self.session)
        
    def fields(self, *, ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]]=None, ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]]=None) -> CiXcodeVersionEndpoint:
        '''Fields to return for included related types.

        :param ci_xcode_version: the fields to include for returned resources of type ciXcodeVersions
        :type ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]] = None

        :param ci_mac_os_version: the fields to include for returned resources of type ciMacOsVersions
        :type ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiXcodeVersionEndpoint
        '''
        if ci_xcode_version: self._set_fields('ciXcodeVersions',ci_xcode_version if type(ci_xcode_version) is list else [ci_xcode_version])
        if ci_mac_os_version: self._set_fields('ciMacOsVersions',ci_mac_os_version if type(ci_mac_os_version) is list else [ci_mac_os_version])
        return self
        
    class Include(StringEnum):
        MAC_OS_VERSIONS = 'macOsVersions'

    def include(self, relationship: Union[Include, list[Include]]) -> CiXcodeVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiXcodeVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, mac_os_versions: int=None) -> CiXcodeVersionEndpoint:
        '''Number of included related resources to return.

        :param mac_os_versions: maximum number of related macOsVersions returned (when they are included). The maximum limit is 50
        :type mac_os_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.CiXcodeVersionEndpoint
        '''
        if mac_os_versions and mac_os_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if mac_os_versions: self._set_limit('macOsVersions', mac_os_versions)

        return self

    def get(self) -> CiXcodeVersionResponse:
        '''Get the resource.

        :returns: Single CiXcodeVersion
        :rtype: CiXcodeVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiXcodeVersionResponse.parse_obj(json)

class MacOsVersionsOfCiXcodeVersionEndpoint(IDEndpoint):
    path = '/v1/ciXcodeVersions/{id}/macOsVersions'

    def fields(self, *, ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]]=None, ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]]=None) -> MacOsVersionsOfCiXcodeVersionEndpoint:
        '''Fields to return for included related types.

        :param ci_xcode_version: the fields to include for returned resources of type ciXcodeVersions
        :type ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]] = None

        :param ci_mac_os_version: the fields to include for returned resources of type ciMacOsVersions
        :type ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.MacOsVersionsOfCiXcodeVersionEndpoint
        '''
        if ci_xcode_version: self._set_fields('ciXcodeVersions',ci_xcode_version if type(ci_xcode_version) is list else [ci_xcode_version])
        if ci_mac_os_version: self._set_fields('ciMacOsVersions',ci_mac_os_version if type(ci_mac_os_version) is list else [ci_mac_os_version])
        return self
        
    class Include(StringEnum):
        XCODE_VERSIONS = 'xcodeVersions'

    def include(self, relationship: Union[Include, list[Include]]) -> MacOsVersionsOfCiXcodeVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.MacOsVersionsOfCiXcodeVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, xcode_versions: int=None) -> MacOsVersionsOfCiXcodeVersionEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param xcode_versions: maximum number of related xcodeVersions returned (when they are included). The maximum limit is 50
        :type xcode_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.MacOsVersionsOfCiXcodeVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if xcode_versions and xcode_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if xcode_versions: self._set_limit('xcodeVersions', xcode_versions)

        return self

    def get(self) -> CiMacOsVersionsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: CiMacOsVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiMacOsVersionsResponse.parse_obj(json)

