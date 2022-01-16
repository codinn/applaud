from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class EndUserLicenseAgreementsEndpoint(Endpoint):
    path = '/v1/endUserLicenseAgreements'

    def create(self, request: EndUserLicenseAgreementCreateRequest) -> EndUserLicenseAgreementResponse:
        '''Create the resource.

        :param request: EndUserLicenseAgreement representation
        :type request: EndUserLicenseAgreementCreateRequest

        :returns: Single EndUserLicenseAgreement
        :rtype: EndUserLicenseAgreementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return EndUserLicenseAgreementResponse.parse_obj(json)

class EndUserLicenseAgreementEndpoint(IDEndpoint):
    path = '/v1/endUserLicenseAgreements/{id}'

    @endpoint('/v1/endUserLicenseAgreements/{id}/territories')
    def territories(self) -> TerritoriesOfEndUserLicenseAgreementEndpoint:
        return TerritoriesOfEndUserLicenseAgreementEndpoint(self.id, self.session)
        
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
        json = super()._perform_patch(request)
        return EndUserLicenseAgreementResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class TerritoriesOfEndUserLicenseAgreementEndpoint(IDEndpoint):
    path = '/v1/endUserLicenseAgreements/{id}/territories'

    def fields(self, *, territory: Union[TerritoryField, list[TerritoryField]]=None) -> TerritoriesOfEndUserLicenseAgreementEndpoint:
        '''Fields to return for included related types.

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.TerritoriesOfEndUserLicenseAgreementEndpoint
        '''
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    def limit(self, number: int=None) -> TerritoriesOfEndUserLicenseAgreementEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TerritoriesOfEndUserLicenseAgreementEndpoint
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

