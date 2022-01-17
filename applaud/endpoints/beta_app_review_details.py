from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaAppReviewDetailsEndpoint(Endpoint):
    path = '/v1/betaAppReviewDetails'

    def fields(self, *, beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]]=None, app: Union[AppField, list[AppField]]=None) -> BetaAppReviewDetailsEndpoint:
        '''Fields to return for included related types.

        :param beta_app_review_detail: the fields to include for returned resources of type betaAppReviewDetails
        :type beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewDetailsEndpoint
        '''
        if beta_app_review_detail: self._set_fields('betaAppReviewDetails',beta_app_review_detail if type(beta_app_review_detail) is list else [beta_app_review_detail])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def filter(self, *, app: Union[str, list[str]]) -> BetaAppReviewDetailsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]]

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewDetailsEndpoint
        '''
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BetaAppReviewDetailsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewDetailsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> BetaAppReviewDetailsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewDetailsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaAppReviewDetailsResponse:
        '''Get one or more resources.

        :returns: List of BetaAppReviewDetails
        :rtype: BetaAppReviewDetailsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppReviewDetailsResponse.parse_obj(json)

class BetaAppReviewDetailEndpoint(IDEndpoint):
    path = '/v1/betaAppReviewDetails/{id}'

    @endpoint('/v1/betaAppReviewDetails/{id}/app')
    def app(self) -> AppOfBetaAppReviewDetailEndpoint:
        return AppOfBetaAppReviewDetailEndpoint(self.id, self.session)
        
    def fields(self, *, beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]]=None, app: Union[AppField, list[AppField]]=None) -> BetaAppReviewDetailEndpoint:
        '''Fields to return for included related types.

        :param beta_app_review_detail: the fields to include for returned resources of type betaAppReviewDetails
        :type beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewDetailEndpoint
        '''
        if beta_app_review_detail: self._set_fields('betaAppReviewDetails',beta_app_review_detail if type(beta_app_review_detail) is list else [beta_app_review_detail])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaAppReviewDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BetaAppReviewDetailResponse:
        '''Get the resource.

        :returns: Single BetaAppReviewDetail
        :rtype: BetaAppReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppReviewDetailResponse.parse_obj(json)

    def update(self, request: BetaAppReviewDetailUpdateRequest) -> BetaAppReviewDetailResponse:
        '''Modify the resource.

        :param request: BetaAppReviewDetail representation
        :type request: BetaAppReviewDetailUpdateRequest

        :returns: Single BetaAppReviewDetail
        :rtype: BetaAppReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BetaAppReviewDetailResponse.parse_obj(json)

class AppOfBetaAppReviewDetailEndpoint(IDEndpoint):
    path = '/v1/betaAppReviewDetails/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppOfBetaAppReviewDetailEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfBetaAppReviewDetailEndpoint
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

