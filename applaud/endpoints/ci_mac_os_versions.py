from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiMacOsVersionListEndpoint(Endpoint):
    path = '/v1/ciMacOsVersions'

    def fields(self, *, ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]]=None, ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]]=None) -> CiMacOsVersionListEndpoint:
        '''Fields to return for included related types.

        :param ci_mac_os_version: the fields to include for returned resources of type ciMacOsVersions
        :type ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]] = None

        :param ci_xcode_version: the fields to include for returned resources of type ciXcodeVersions
        :type ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiMacOsVersionListEndpoint
        '''
        if ci_mac_os_version: self._set_fields('ciMacOsVersions',ci_mac_os_version if type(ci_mac_os_version) is list else [ci_mac_os_version])
        if ci_xcode_version: self._set_fields('ciXcodeVersions',ci_xcode_version if type(ci_xcode_version) is list else [ci_xcode_version])
        return self
        
    class Include(StringEnum):
        XCODE_VERSIONS = 'xcodeVersions'

    def include(self, relationship: Union[Include, list[Include]]) -> CiMacOsVersionListEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiMacOsVersionListEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, xcode_versions: int=None) -> CiMacOsVersionListEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param xcode_versions: maximum number of related xcodeVersions returned (when they are included). The maximum limit is 50
        :type xcode_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.CiMacOsVersionListEndpoint
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

        :returns: List of CiMacOsVersions
        :rtype: CiMacOsVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiMacOsVersionsResponse.parse_obj(json)

class CiMacOsVersionEndpoint(IDEndpoint):
    path = '/v1/ciMacOsVersions/{id}'

    def fields(self, *, ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]]=None, ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]]=None) -> CiMacOsVersionEndpoint:
        '''Fields to return for included related types.

        :param ci_mac_os_version: the fields to include for returned resources of type ciMacOsVersions
        :type ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]] = None

        :param ci_xcode_version: the fields to include for returned resources of type ciXcodeVersions
        :type ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiMacOsVersionEndpoint
        '''
        if ci_mac_os_version: self._set_fields('ciMacOsVersions',ci_mac_os_version if type(ci_mac_os_version) is list else [ci_mac_os_version])
        if ci_xcode_version: self._set_fields('ciXcodeVersions',ci_xcode_version if type(ci_xcode_version) is list else [ci_xcode_version])
        return self
        
    class Include(StringEnum):
        XCODE_VERSIONS = 'xcodeVersions'

    def include(self, relationship: Union[Include, list[Include]]) -> CiMacOsVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiMacOsVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, xcode_versions: int=None) -> CiMacOsVersionEndpoint:
        '''Number of included related resources to return.

        :param xcode_versions: maximum number of related xcodeVersions returned (when they are included). The maximum limit is 50
        :type xcode_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.CiMacOsVersionEndpoint
        '''
        if xcode_versions and xcode_versions > 50:
            raise ValueError(f'The maximum limit is 50')
        if xcode_versions: self._set_limit('xcodeVersions', xcode_versions)

        return self

    def get(self) -> CiMacOsVersionResponse:
        '''Get the resource.

        :returns: Single CiMacOsVersion
        :rtype: CiMacOsVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiMacOsVersionResponse.parse_obj(json)

class XcodeVersionListOfCiMacOsVersionEndpoint(IDEndpoint):
    path = '/v1/ciMacOsVersions/{id}/xcodeVersions'

    def fields(self, *, ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]]=None, ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]]=None) -> XcodeVersionListOfCiMacOsVersionEndpoint:
        '''Fields to return for included related types.

        :param ci_xcode_version: the fields to include for returned resources of type ciXcodeVersions
        :type ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]] = None

        :param ci_mac_os_version: the fields to include for returned resources of type ciMacOsVersions
        :type ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.XcodeVersionListOfCiMacOsVersionEndpoint
        '''
        if ci_xcode_version: self._set_fields('ciXcodeVersions',ci_xcode_version if type(ci_xcode_version) is list else [ci_xcode_version])
        if ci_mac_os_version: self._set_fields('ciMacOsVersions',ci_mac_os_version if type(ci_mac_os_version) is list else [ci_mac_os_version])
        return self
        
    class Include(StringEnum):
        MAC_OS_VERSIONS = 'macOsVersions'

    def include(self, relationship: Union[Include, list[Include]]) -> XcodeVersionListOfCiMacOsVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.XcodeVersionListOfCiMacOsVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, mac_os_versions: int=None) -> XcodeVersionListOfCiMacOsVersionEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param mac_os_versions: maximum number of related macOsVersions returned (when they are included). The maximum limit is 50
        :type mac_os_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.XcodeVersionListOfCiMacOsVersionEndpoint
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

        :returns: List of related resources
        :rtype: CiXcodeVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiXcodeVersionsResponse.parse_obj(json)

