from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaLicenseAgreementsEndpoint(Endpoint):
    path = '/v1/betaLicenseAgreements'

    def fields(self, *, beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]]=None, app: Union[AppField, list[AppField]]=None) -> BetaLicenseAgreementsEndpoint:
        '''Fields to return for included related types.

        :param beta_license_agreement: the fields to include for returned resources of type betaLicenseAgreements
        :type beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaLicenseAgreementsEndpoint
        '''
        if beta_license_agreement: self._set_fields('betaLicenseAgreements',beta_license_agreement if type(beta_license_agreement) is list else [beta_license_agreement])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def filter(self, *, app: Union[str, list[str]]=None) -> BetaLicenseAgreementsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaLicenseAgreementsEndpoint
        '''
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BetaLicenseAgreementsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaLicenseAgreementsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> BetaLicenseAgreementsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaLicenseAgreementsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaLicenseAgreementsResponse:
        '''Get one or more resources.

        :returns: List of BetaLicenseAgreements
        :rtype: BetaLicenseAgreementsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaLicenseAgreementsResponse.parse_obj(json)

class BetaLicenseAgreementEndpoint(IDEndpoint):
    path = '/v1/betaLicenseAgreements/{id}'

    @endpoint('/v1/betaLicenseAgreements/{id}/app')
    def app(self) -> AppOfBetaLicenseAgreementEndpoint:
        return AppOfBetaLicenseAgreementEndpoint(self.id, self.session)
        
    def fields(self, *, beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]]=None, app: Union[AppField, list[AppField]]=None) -> BetaLicenseAgreementEndpoint:
        '''Fields to return for included related types.

        :param beta_license_agreement: the fields to include for returned resources of type betaLicenseAgreements
        :type beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaLicenseAgreementEndpoint
        '''
        if beta_license_agreement: self._set_fields('betaLicenseAgreements',beta_license_agreement if type(beta_license_agreement) is list else [beta_license_agreement])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaLicenseAgreementEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaLicenseAgreementEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BetaLicenseAgreementResponse:
        '''Get the resource.

        :returns: Single BetaLicenseAgreement
        :rtype: BetaLicenseAgreementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaLicenseAgreementResponse.parse_obj(json)

    def update(self, request: BetaLicenseAgreementUpdateRequest) -> BetaLicenseAgreementResponse:
        '''Modify the resource.

        :param request: BetaLicenseAgreement representation
        :type request: BetaLicenseAgreementUpdateRequest

        :returns: Single BetaLicenseAgreement
        :rtype: BetaLicenseAgreementResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BetaLicenseAgreementResponse.parse_obj(json)

class AppOfBetaLicenseAgreementEndpoint(IDEndpoint):
    path = '/v1/betaLicenseAgreements/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppOfBetaLicenseAgreementEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfBetaLicenseAgreementEndpoint
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

