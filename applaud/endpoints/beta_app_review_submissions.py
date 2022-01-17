from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaAppReviewSubmissionsEndpoint(Endpoint):
    path = '/v1/betaAppReviewSubmissions'

    def fields(self, *, beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BetaAppReviewSubmissionsEndpoint:
        '''Fields to return for included related types.

        :param beta_app_review_submission: the fields to include for returned resources of type betaAppReviewSubmissions
        :type beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewSubmissionsEndpoint
        '''
        if beta_app_review_submission: self._set_fields('betaAppReviewSubmissions',beta_app_review_submission if type(beta_app_review_submission) is list else [beta_app_review_submission])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'

    def filter(self, *, beta_review_state: Union[BetaReviewState, list[BetaReviewState]]=None, build: Union[str, list[str]]) -> BetaAppReviewSubmissionsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param beta_review_state: filter by attribute 'betaReviewState'
        :type beta_review_state: Union[BetaReviewState, list[BetaReviewState]] = None

        :param build: filter by id(s) of related 'build'
        :type build: Union[str, list[str]]

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewSubmissionsEndpoint
        '''
        if beta_review_state: self._set_filter('betaReviewState', beta_review_state if type(beta_review_state) is list else [beta_review_state])
        
        if build: self._set_filter('build', build if type(build) is list else [build])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BetaAppReviewSubmissionsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewSubmissionsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> BetaAppReviewSubmissionsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewSubmissionsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaAppReviewSubmissionsResponse:
        '''Get one or more resources.

        :returns: List of BetaAppReviewSubmissions
        :rtype: BetaAppReviewSubmissionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppReviewSubmissionsResponse.parse_obj(json)

    def create(self, request: BetaAppReviewSubmissionCreateRequest) -> BetaAppReviewSubmissionResponse:
        '''Create the resource.

        :param request: BetaAppReviewSubmission representation
        :type request: BetaAppReviewSubmissionCreateRequest

        :returns: Single BetaAppReviewSubmission
        :rtype: BetaAppReviewSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BetaAppReviewSubmissionResponse.parse_obj(json)

class BetaAppReviewSubmissionEndpoint(IDEndpoint):
    path = '/v1/betaAppReviewSubmissions/{id}'

    @endpoint('/v1/betaAppReviewSubmissions/{id}/build')
    def build(self) -> BuildOfBetaAppReviewSubmissionEndpoint:
        return BuildOfBetaAppReviewSubmissionEndpoint(self.id, self.session)
        
    def fields(self, *, beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BetaAppReviewSubmissionEndpoint:
        '''Fields to return for included related types.

        :param beta_app_review_submission: the fields to include for returned resources of type betaAppReviewSubmissions
        :type beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewSubmissionEndpoint
        '''
        if beta_app_review_submission: self._set_fields('betaAppReviewSubmissions',beta_app_review_submission if type(beta_app_review_submission) is list else [beta_app_review_submission])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaAppReviewSubmissionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewSubmissionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BetaAppReviewSubmissionResponse:
        '''Get the resource.

        :returns: Single BetaAppReviewSubmission
        :rtype: BetaAppReviewSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppReviewSubmissionResponse.parse_obj(json)

class BuildOfBetaAppReviewSubmissionEndpoint(IDEndpoint):
    path = '/v1/betaAppReviewSubmissions/{id}/build'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildOfBetaAppReviewSubmissionEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildOfBetaAppReviewSubmissionEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    def get(self) -> BuildResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: BuildResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildResponse.parse_obj(json)

