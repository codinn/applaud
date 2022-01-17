from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CertificatesEndpoint(Endpoint):
    path = '/v1/certificates'

    def fields(self, *, certificate: Union[CertificateField, list[CertificateField]]=None) -> CertificatesEndpoint:
        '''Fields to return for included related types.

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesEndpoint
        '''
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    def filter(self, *, certificate_type: Union[CertificateType, list[CertificateType]]=None, display_name: Union[str, list[str]]=None, serial_number: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> CertificatesEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param certificate_type: filter by attribute 'certificateType'
        :type certificate_type: Union[CertificateType, list[CertificateType]] = None

        :param display_name: filter by attribute 'displayName'
        :type display_name: Union[str, list[str]] = None

        :param serial_number: filter by attribute 'serialNumber'
        :type serial_number: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesEndpoint
        '''
        if certificate_type: self._set_filter('certificateType', certificate_type if type(certificate_type) is list else [certificate_type])
        
        if display_name: self._set_filter('displayName', display_name if type(display_name) is list else [display_name])
        
        if serial_number: self._set_filter('serialNumber', serial_number if type(serial_number) is list else [serial_number])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def sort(self, *, certificate_type: SortOrder=None, display_name: SortOrder=None, id: SortOrder=None, serial_number: SortOrder=None) -> CertificatesEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.CertificatesEndpoint
        '''
        if certificate_type: self.sort_expressions.append('certificateType' if certificate_type == SortOrder.ASC else '-certificateType')
        if display_name: self.sort_expressions.append('displayName' if display_name == SortOrder.ASC else '-displayName')
        if id: self.sort_expressions.append('id' if id == SortOrder.ASC else '-id')
        if serial_number: self.sort_expressions.append('serialNumber' if serial_number == SortOrder.ASC else '-serialNumber')
        return self
        
    def limit(self, number: int=None) -> CertificatesEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CertificatesEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CertificatesResponse:
        '''Get one or more resources.

        :returns: List of Certificates
        :rtype: CertificatesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CertificatesResponse.parse_obj(json)

    def create(self, request: CertificateCreateRequest) -> CertificateResponse:
        '''Create the resource.

        :param request: Certificate representation
        :type request: CertificateCreateRequest

        :returns: Single Certificate
        :rtype: CertificateResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return CertificateResponse.parse_obj(json)

class CertificateEndpoint(IDEndpoint):
    path = '/v1/certificates/{id}'

    def fields(self, *, certificate: Union[CertificateField, list[CertificateField]]=None) -> CertificateEndpoint:
        '''Fields to return for included related types.

        :param certificate: the fields to include for returned resources of type certificates
        :type certificate: Union[CertificateField, list[CertificateField]] = None

        :returns: self
        :rtype: applaud.endpoints.CertificateEndpoint
        '''
        if certificate: self._set_fields('certificates',certificate if type(certificate) is list else [certificate])
        return self
        
    def get(self) -> CertificateResponse:
        '''Get the resource.

        :returns: Single Certificate
        :rtype: CertificateResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CertificateResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

