from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class ScmPullRequestEndpoint(IDEndpoint):
    path = '/v1/scmPullRequests/{id}'

    def fields(self, *, scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]]=None) -> ScmPullRequestEndpoint:
        '''Fields to return for included related types.

        :param scm_pull_request: the fields to include for returned resources of type scmPullRequests
        :type scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]] = None

        :returns: self
        :rtype: applaud.endpoints.ScmPullRequestEndpoint
        '''
        if scm_pull_request: self._set_fields('scmPullRequests',scm_pull_request if type(scm_pull_request) is list else [scm_pull_request])
        return self
        
    class Include(StringEnum):
        REPOSITORY = 'repository'

    def include(self, relationship: Union[Include, list[Include]]) -> ScmPullRequestEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ScmPullRequestEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> ScmPullRequestResponse:
        '''Get the resource.

        :returns: Single ScmPullRequest
        :rtype: ScmPullRequestResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmPullRequestResponse.parse_obj(json)

