from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiIssueEndpoint(IDEndpoint):
    path = '/v1/ciIssues/{id}'

    def fields(self, *, ci_issue: Union[CiIssueField, list[CiIssueField]]=None) -> CiIssueEndpoint:
        '''Fields to return for included related types.

        :param ci_issue: the fields to include for returned resources of type ciIssues
        :type ci_issue: Union[CiIssueField, list[CiIssueField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiIssueEndpoint
        '''
        if ci_issue: self._set_fields('ciIssues',ci_issue if type(ci_issue) is list else [ci_issue])
        return self
        
    def get(self) -> CiIssueResponse:
        '''Get the resource.

        :returns: Single CiIssue
        :rtype: CiIssueResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiIssueResponse.parse_obj(json)

