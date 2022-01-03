from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class IdfaDeclarationListEndpoint(Endpoint):
    path = '/v1/idfaDeclarations'

    @deprecated
    def create(self, request: IdfaDeclarationCreateRequest) -> IdfaDeclarationResponse:
        '''Create the resource.

        :param request: IdfaDeclaration representation
        :type request: IdfaDeclarationCreateRequest

        :returns: Single IdfaDeclaration
        :rtype: IdfaDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_post(json)
        return IdfaDeclarationResponse.parse_obj(response_json)

class IdfaDeclarationEndpoint(IDEndpoint):
    path = '/v1/idfaDeclarations/{id}'

    @deprecated
    def update(self, request: IdfaDeclarationUpdateRequest) -> IdfaDeclarationResponse:
        '''Modify the resource.

        :param request: IdfaDeclaration representation
        :type request: IdfaDeclarationUpdateRequest

        :returns: Single IdfaDeclaration
        :rtype: IdfaDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_patch(json)
        return IdfaDeclarationResponse.parse_obj(response_json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

