from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaAppClipInvocationsEndpoint(Endpoint):
    path = '/v1/betaAppClipInvocations'

    def create(self, request: BetaAppClipInvocationCreateRequest) -> BetaAppClipInvocationResponse:
        '''Create the resource.

        :param request: BetaAppClipInvocation representation
        :type request: BetaAppClipInvocationCreateRequest

        :returns: Single BetaAppClipInvocation
        :rtype: BetaAppClipInvocationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BetaAppClipInvocationResponse.parse_obj(json)

class BetaAppClipInvocationEndpoint(IDEndpoint):
    path = '/v1/betaAppClipInvocations/{id}'

    def fields(self, *, beta_app_clip_invocation: Union[BetaAppClipInvocationField, list[BetaAppClipInvocationField]]=None) -> BetaAppClipInvocationEndpoint:
        '''Fields to return for included related types.

        :param beta_app_clip_invocation: the fields to include for returned resources of type betaAppClipInvocations
        :type beta_app_clip_invocation: Union[BetaAppClipInvocationField, list[BetaAppClipInvocationField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppClipInvocationEndpoint
        '''
        if beta_app_clip_invocation: self._set_fields('betaAppClipInvocations',beta_app_clip_invocation if type(beta_app_clip_invocation) is list else [beta_app_clip_invocation])
        return self
        
    class Include(StringEnum):
        BETA_APP_CLIP_INVOCATION_LOCALIZATIONS = 'betaAppClipInvocationLocalizations'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaAppClipInvocationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaAppClipInvocationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, beta_app_clip_invocation_localizations: int=None) -> BetaAppClipInvocationEndpoint:
        '''Number of included related resources to return.

        :param beta_app_clip_invocation_localizations: maximum number of related betaAppClipInvocationLocalizations returned (when they are included). The maximum limit is 50
        :type beta_app_clip_invocation_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppClipInvocationEndpoint
        '''
        if beta_app_clip_invocation_localizations and beta_app_clip_invocation_localizations > 50:
            raise ValueError(f'The maximum limit of beta_app_clip_invocation_localizations is 50')
        if beta_app_clip_invocation_localizations: self._set_limit(beta_app_clip_invocation_localizations, 'betaAppClipInvocationLocalizations')

        return self

    def get(self) -> BetaAppClipInvocationResponse:
        '''Get the resource.

        :returns: Single BetaAppClipInvocation
        :rtype: BetaAppClipInvocationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppClipInvocationResponse.parse_obj(json)

    def update(self, request: BetaAppClipInvocationUpdateRequest) -> BetaAppClipInvocationResponse:
        '''Modify the resource.

        :param request: BetaAppClipInvocation representation
        :type request: BetaAppClipInvocationUpdateRequest

        :returns: Single BetaAppClipInvocation
        :rtype: BetaAppClipInvocationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BetaAppClipInvocationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

