from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class LogListOfDiagnosticSignatureEndpoint(IDEndpoint):
    path = '/v1/diagnosticSignatures/{id}/logs'

    def limit(self, number: int=None) -> LogListOfDiagnosticSignatureEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.LogListOfDiagnosticSignatureEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> DiagnosticLogsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: DiagnosticLogsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return DiagnosticLogsResponse.parse_obj(json)

