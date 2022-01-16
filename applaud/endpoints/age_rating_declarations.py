from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
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
        json = super()._perform_patch(request)
        return AgeRatingDeclarationResponse.parse_obj(json)

