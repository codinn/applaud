from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}'

    @endpoint('/v1/ciBuildActions/{id}/artifacts')
    def artifacts(self) -> ArtifactsOfCiBuildActionEndpoint:
        return ArtifactsOfCiBuildActionEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildActions/{id}/buildRun')
    def build_run(self) -> BuildRunOfCiBuildActionEndpoint:
        return BuildRunOfCiBuildActionEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildActions/{id}/issues')
    def issues(self) -> IssuesOfCiBuildActionEndpoint:
        return IssuesOfCiBuildActionEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildActions/{id}/testResults')
    def test_results(self) -> TestResultsOfCiBuildActionEndpoint:
        return TestResultsOfCiBuildActionEndpoint(self.id, self.session)
        
    def fields(self, *, ci_build_action: Union[CiBuildActionField, list[CiBuildActionField]]=None, ci_issue: Union[CiIssueField, list[CiIssueField]]=None, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None, ci_test_result: Union[CiTestResultField, list[CiTestResultField]]=None, ci_artifact: Union[CiArtifactField, list[CiArtifactField]]=None) -> CiBuildActionEndpoint:
        '''Fields to return for included related types.

        :param ci_build_action: the fields to include for returned resources of type ciBuildActions
        :type ci_build_action: Union[CiBuildActionField, list[CiBuildActionField]] = None

        :param ci_issue: the fields to include for returned resources of type ciIssues
        :type ci_issue: Union[CiIssueField, list[CiIssueField]] = None

        :param ci_build_run: the fields to include for returned resources of type ciBuildRuns
        :type ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]] = None

        :param ci_test_result: the fields to include for returned resources of type ciTestResults
        :type ci_test_result: Union[CiTestResultField, list[CiTestResultField]] = None

        :param ci_artifact: the fields to include for returned resources of type ciArtifacts
        :type ci_artifact: Union[CiArtifactField, list[CiArtifactField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiBuildActionEndpoint
        '''
        if ci_build_action: self._set_fields('ciBuildActions',ci_build_action if type(ci_build_action) is list else [ci_build_action])
        if ci_issue: self._set_fields('ciIssues',ci_issue if type(ci_issue) is list else [ci_issue])
        if ci_build_run: self._set_fields('ciBuildRuns',ci_build_run if type(ci_build_run) is list else [ci_build_run])
        if ci_test_result: self._set_fields('ciTestResults',ci_test_result if type(ci_test_result) is list else [ci_test_result])
        if ci_artifact: self._set_fields('ciArtifacts',ci_artifact if type(ci_artifact) is list else [ci_artifact])
        return self
        
    class Include(StringEnum):
        BUILD_RUN = 'buildRun'

    def include(self, relationship: Union[Include, list[Include]]) -> CiBuildActionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiBuildActionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> CiBuildActionResponse:
        '''Get the resource.

        :returns: Single CiBuildAction
        :rtype: CiBuildActionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildActionResponse.parse_obj(json)

class ArtifactsOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/artifacts'

    def fields(self, *, ci_artifact: Union[CiArtifactField, list[CiArtifactField]]=None) -> ArtifactsOfCiBuildActionEndpoint:
        '''Fields to return for included related types.

        :param ci_artifact: the fields to include for returned resources of type ciArtifacts
        :type ci_artifact: Union[CiArtifactField, list[CiArtifactField]] = None

        :returns: self
        :rtype: applaud.endpoints.ArtifactsOfCiBuildActionEndpoint
        '''
        if ci_artifact: self._set_fields('ciArtifacts',ci_artifact if type(ci_artifact) is list else [ci_artifact])
        return self
        
    def limit(self, number: int=None) -> ArtifactsOfCiBuildActionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ArtifactsOfCiBuildActionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiArtifactsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: CiArtifactsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiArtifactsResponse.parse_obj(json)

class BuildRunOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/buildRun'

    def fields(self, *, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BuildRunOfCiBuildActionEndpoint:
        '''Fields to return for included related types.

        :param ci_build_run: the fields to include for returned resources of type ciBuildRuns
        :type ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunOfCiBuildActionEndpoint
        '''
        if ci_build_run: self._set_fields('ciBuildRuns',ci_build_run if type(ci_build_run) is list else [ci_build_run])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILDS = 'builds'

    def include(self, relationship: Union[Include, list[Include]]) -> BuildRunOfCiBuildActionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildRunOfCiBuildActionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, builds: int=None) -> BuildRunOfCiBuildActionEndpoint:
        '''Number of included related resources to return.

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunOfCiBuildActionEndpoint
        '''
        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        return self

    def get(self) -> CiBuildRunResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: CiBuildRunResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildRunResponse.parse_obj(json)

class IssuesOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/issues'

    def fields(self, *, ci_issue: Union[CiIssueField, list[CiIssueField]]=None) -> IssuesOfCiBuildActionEndpoint:
        '''Fields to return for included related types.

        :param ci_issue: the fields to include for returned resources of type ciIssues
        :type ci_issue: Union[CiIssueField, list[CiIssueField]] = None

        :returns: self
        :rtype: applaud.endpoints.IssuesOfCiBuildActionEndpoint
        '''
        if ci_issue: self._set_fields('ciIssues',ci_issue if type(ci_issue) is list else [ci_issue])
        return self
        
    def limit(self, number: int=None) -> IssuesOfCiBuildActionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IssuesOfCiBuildActionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiIssuesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: CiIssuesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiIssuesResponse.parse_obj(json)

class TestResultsOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/testResults'

    def fields(self, *, ci_test_result: Union[CiTestResultField, list[CiTestResultField]]=None) -> TestResultsOfCiBuildActionEndpoint:
        '''Fields to return for included related types.

        :param ci_test_result: the fields to include for returned resources of type ciTestResults
        :type ci_test_result: Union[CiTestResultField, list[CiTestResultField]] = None

        :returns: self
        :rtype: applaud.endpoints.TestResultsOfCiBuildActionEndpoint
        '''
        if ci_test_result: self._set_fields('ciTestResults',ci_test_result if type(ci_test_result) is list else [ci_test_result])
        return self
        
    def limit(self, number: int=None) -> TestResultsOfCiBuildActionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TestResultsOfCiBuildActionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiTestResultsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: CiTestResultsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiTestResultsResponse.parse_obj(json)

