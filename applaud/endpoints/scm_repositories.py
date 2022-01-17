from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class ScmRepositoriesEndpoint(Endpoint):
    path = '/v1/scmRepositories'

    def fields(self, *, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None, scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]]=None, scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]]=None) -> ScmRepositoriesEndpoint:
        '''Fields to return for included related types.

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :param scm_git_reference: the fields to include for returned resources of type scmGitReferences
        :type scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]] = None

        :param scm_pull_request: the fields to include for returned resources of type scmPullRequests
        :type scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]] = None

        :returns: self
        :rtype: applaud.endpoints.ScmRepositoriesEndpoint
        '''
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        if scm_git_reference: self._set_fields('scmGitReferences',scm_git_reference if type(scm_git_reference) is list else [scm_git_reference])
        if scm_pull_request: self._set_fields('scmPullRequests',scm_pull_request if type(scm_pull_request) is list else [scm_pull_request])
        return self
        
    class Include(StringEnum):
        DEFAULT_BRANCH = 'defaultBranch'
        SCM_PROVIDER = 'scmProvider'

    def filter(self, *, id: Union[str, list[str]]=None) -> ScmRepositoriesEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.ScmRepositoriesEndpoint
        '''
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> ScmRepositoriesEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ScmRepositoriesEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ScmRepositoriesEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ScmRepositoriesEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ScmRepositoriesResponse:
        '''Get one or more resources.

        :returns: List of ScmRepositories
        :rtype: ScmRepositoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmRepositoriesResponse.parse_obj(json)

class ScmRepositoryEndpoint(IDEndpoint):
    path = '/v1/scmRepositories/{id}'

    @endpoint('/v1/scmRepositories/{id}/gitReferences')
    def git_references(self) -> GitReferencesOfScmRepositoryEndpoint:
        return GitReferencesOfScmRepositoryEndpoint(self.id, self.session)
        
    @endpoint('/v1/scmRepositories/{id}/pullRequests')
    def pull_requests(self) -> PullRequestsOfScmRepositoryEndpoint:
        return PullRequestsOfScmRepositoryEndpoint(self.id, self.session)
        
    def fields(self, *, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None, scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]]=None, scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]]=None) -> ScmRepositoryEndpoint:
        '''Fields to return for included related types.

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :param scm_git_reference: the fields to include for returned resources of type scmGitReferences
        :type scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]] = None

        :param scm_pull_request: the fields to include for returned resources of type scmPullRequests
        :type scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]] = None

        :returns: self
        :rtype: applaud.endpoints.ScmRepositoryEndpoint
        '''
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        if scm_git_reference: self._set_fields('scmGitReferences',scm_git_reference if type(scm_git_reference) is list else [scm_git_reference])
        if scm_pull_request: self._set_fields('scmPullRequests',scm_pull_request if type(scm_pull_request) is list else [scm_pull_request])
        return self
        
    class Include(StringEnum):
        DEFAULT_BRANCH = 'defaultBranch'
        SCM_PROVIDER = 'scmProvider'

    def include(self, relationship: Union[Include, list[Include]]) -> ScmRepositoryEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ScmRepositoryEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> ScmRepositoryResponse:
        '''Get the resource.

        :returns: Single ScmRepository
        :rtype: ScmRepositoryResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmRepositoryResponse.parse_obj(json)

class GitReferencesOfScmRepositoryEndpoint(IDEndpoint):
    path = '/v1/scmRepositories/{id}/gitReferences'

    def fields(self, *, scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]]=None) -> GitReferencesOfScmRepositoryEndpoint:
        '''Fields to return for included related types.

        :param scm_git_reference: the fields to include for returned resources of type scmGitReferences
        :type scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]] = None

        :returns: self
        :rtype: applaud.endpoints.GitReferencesOfScmRepositoryEndpoint
        '''
        if scm_git_reference: self._set_fields('scmGitReferences',scm_git_reference if type(scm_git_reference) is list else [scm_git_reference])
        return self
        
    def limit(self, number: int=None) -> GitReferencesOfScmRepositoryEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GitReferencesOfScmRepositoryEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ScmGitReferencesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: ScmGitReferencesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmGitReferencesResponse.parse_obj(json)

class PullRequestsOfScmRepositoryEndpoint(IDEndpoint):
    path = '/v1/scmRepositories/{id}/pullRequests'

    def fields(self, *, scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]]=None) -> PullRequestsOfScmRepositoryEndpoint:
        '''Fields to return for included related types.

        :param scm_pull_request: the fields to include for returned resources of type scmPullRequests
        :type scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]] = None

        :returns: self
        :rtype: applaud.endpoints.PullRequestsOfScmRepositoryEndpoint
        '''
        if scm_pull_request: self._set_fields('scmPullRequests',scm_pull_request if type(scm_pull_request) is list else [scm_pull_request])
        return self
        
    def limit(self, number: int=None) -> PullRequestsOfScmRepositoryEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PullRequestsOfScmRepositoryEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ScmPullRequestsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: ScmPullRequestsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmPullRequestsResponse.parse_obj(json)

