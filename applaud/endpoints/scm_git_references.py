from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class ScmGitReferenceEndpoint(IDEndpoint):
    path = '/v1/scmGitReferences/{id}'

    def fields(self, *, scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]]=None) -> ScmGitReferenceEndpoint:
        '''Fields to return for included related types.

        :param scm_git_reference: the fields to include for returned resources of type scmGitReferences
        :type scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]] = None

        :returns: self
        :rtype: applaud.endpoints.ScmGitReferenceEndpoint
        '''
        if scm_git_reference: self._set_fields('scmGitReferences',scm_git_reference if type(scm_git_reference) is list else [scm_git_reference])
        return self
        
    class Include(StringEnum):
        REPOSITORY = 'repository'

    def include(self, relationship: Union[Include, list[Include]]) -> ScmGitReferenceEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ScmGitReferenceEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> ScmGitReferenceResponse:
        '''Get the resource.

        :returns: Single ScmGitReference
        :rtype: ScmGitReferenceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmGitReferenceResponse.parse_obj(json)

