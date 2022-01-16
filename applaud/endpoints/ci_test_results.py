from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiTestResultEndpoint(IDEndpoint):
    path = '/v1/ciTestResults/{id}'

    def fields(self, *, ci_test_result: Union[CiTestResultField, list[CiTestResultField]]=None) -> CiTestResultEndpoint:
        '''Fields to return for included related types.

        :param ci_test_result: the fields to include for returned resources of type ciTestResults
        :type ci_test_result: Union[CiTestResultField, list[CiTestResultField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiTestResultEndpoint
        '''
        if ci_test_result: self._set_fields('ciTestResults',ci_test_result if type(ci_test_result) is list else [ci_test_result])
        return self
        
    def get(self) -> CiTestResultResponse:
        '''Get the resource.

        :returns: Single CiTestResult
        :rtype: CiTestResultResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiTestResultResponse.parse_obj(json)

