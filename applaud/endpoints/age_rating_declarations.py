from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AgeRatingDeclarationEndpoint(IDEndpoint):
    path = '/v1/ageRatingDeclarations/{id}'

    def update(self, request: AgeRatingDeclarationUpdateRequest) -> AgeRatingDeclarationResponse:
        '''Modify the resource.

        :param request: AgeRatingDeclaration representation
        :type request: AgeRatingDeclarationUpdateRequest

        :returns: Single AgeRatingDeclaration
        :rtype: AgeRatingDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_patch(json)
        return AgeRatingDeclarationResponse.parse_obj(response_json)

