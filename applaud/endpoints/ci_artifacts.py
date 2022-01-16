from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiArtifactEndpoint(IDEndpoint):
    path = '/v1/ciArtifacts/{id}'

    def fields(self, *, ci_artifact: Union[CiArtifactField, list[CiArtifactField]]=None) -> CiArtifactEndpoint:
        '''Fields to return for included related types.

        :param ci_artifact: the fields to include for returned resources of type ciArtifacts
        :type ci_artifact: Union[CiArtifactField, list[CiArtifactField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiArtifactEndpoint
        '''
        if ci_artifact: self._set_fields('ciArtifacts',ci_artifact if type(ci_artifact) is list else [ci_artifact])
        return self
        
    def get(self) -> CiArtifactResponse:
        '''Get the resource.

        :returns: Single CiArtifact
        :rtype: CiArtifactResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiArtifactResponse.parse_obj(json)

