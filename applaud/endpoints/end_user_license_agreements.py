from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class EndUserLicenseAgreementListEndpoint(Endpoint):
    path = '/v1/endUserLicenseAgreements'

    def create(self, request: EndUserLicenseAgreementCreateRequest) -> EndUserLicenseAgreementResponse:
        '''Create the resource.

        :param request: EndUserLicenseAgreement representation
        :type request: EndUserLicenseAgreementCreateRequest

        :returns: Single EndUserLicenseAgreement
        :rtype: EndUserLicenseAgreementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_post(json)
        return EndUserLicenseAgreementResponse.parse_obj(response_json)

class EndUserLicenseAgreementEndpoint(IDEndpoint):
    path = '/v1/endUserLicenseAgreements/{id}'

    def fields(self, *, end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> EndUserLicenseAgreementEndpoint:
        '''Fields to return for included related types.

        :param end_user_license_agreement: the fields to include for returned resources of type endUserLicenseAgreements
        :type end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.EndUserLicenseAgreementEndpoint
        '''
        if end_user_license_agreement: self._set_fields('endUserLicenseAgreements',end_user_license_agreement if type(end_user_license_agreement) is list else [end_user_license_agreement])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        TERRITORIES = 'territories'

    def include(self, relationship: Union[Include, list[Include]]) -> EndUserLicenseAgreementEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.EndUserLicenseAgreementEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, territories: int=None) -> EndUserLicenseAgreementEndpoint:
        '''Number of included related resources to return.

        :param territories: maximum number of related territories returned (when they are included). The maximum limit is 50
        :type territories: int = None

        :returns: self
        :rtype: applaud.endpoints.EndUserLicenseAgreementEndpoint
        '''
        if territories and territories > 50:
            raise ValueError(f'The maximum limit is 50')
        if territories: self._set_limit('territories', territories)

        return self

    def get(self) -> EndUserLicenseAgreementResponse:
        '''Get the resource.

        :returns: Single EndUserLicenseAgreement
        :rtype: EndUserLicenseAgreementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return EndUserLicenseAgreementResponse.parse_obj(json)

    def update(self, request: EndUserLicenseAgreementUpdateRequest) -> EndUserLicenseAgreementResponse:
        '''Modify the resource.

        :param request: EndUserLicenseAgreement representation
        :type request: EndUserLicenseAgreementUpdateRequest

        :returns: Single EndUserLicenseAgreement
        :rtype: EndUserLicenseAgreementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_patch(json)
        return EndUserLicenseAgreementResponse.parse_obj(response_json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class TerritoryListOfEndUserLicenseAgreementEndpoint(IDEndpoint):
    path = '/v1/endUserLicenseAgreements/{id}/territories'

    def fields(self, *, territory: Union[TerritoryField, list[TerritoryField]]=None) -> TerritoryListOfEndUserLicenseAgreementEndpoint:
        '''Fields to return for included related types.

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.TerritoryListOfEndUserLicenseAgreementEndpoint
        '''
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    def limit(self, number: int=None) -> TerritoryListOfEndUserLicenseAgreementEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TerritoryListOfEndUserLicenseAgreementEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> TerritoriesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: TerritoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return TerritoriesResponse.parse_obj(json)

