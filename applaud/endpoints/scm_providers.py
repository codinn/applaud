from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class ScmProvidersEndpoint(Endpoint):
    path = '/v1/scmProviders'

    def fields(self, *, scm_provider: Union[ScmProviderField, list[ScmProviderField]]=None, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> ScmProvidersEndpoint:
        '''Fields to return for included related types.

        :param scm_provider: the fields to include for returned resources of type scmProviders
        :type scm_provider: Union[ScmProviderField, list[ScmProviderField]] = None

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.ScmProvidersEndpoint
        '''
        if scm_provider: self._set_fields('scmProviders',scm_provider if type(scm_provider) is list else [scm_provider])
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    def limit(self, number: int=None) -> ScmProvidersEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ScmProvidersEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> ScmProvidersResponse:
        '''Get one or more resources.

        :returns: List of ScmProviders
        :rtype: ScmProvidersResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmProvidersResponse.parse_obj(json)

class ScmProviderEndpoint(IDEndpoint):
    path = '/v1/scmProviders/{id}'

    @endpoint('/v1/scmProviders/{id}/repositories')
    def repositories(self) -> RepositoriesOfScmProviderEndpoint:
        return RepositoriesOfScmProviderEndpoint(self.id, self.session)
        
    def fields(self, *, scm_provider: Union[ScmProviderField, list[ScmProviderField]]=None, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> ScmProviderEndpoint:
        '''Fields to return for included related types.

        :param scm_provider: the fields to include for returned resources of type scmProviders
        :type scm_provider: Union[ScmProviderField, list[ScmProviderField]] = None

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.ScmProviderEndpoint
        '''
        if scm_provider: self._set_fields('scmProviders',scm_provider if type(scm_provider) is list else [scm_provider])
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    def get(self) -> ScmProviderResponse:
        '''Get the resource.

        :returns: Single ScmProvider
        :rtype: ScmProviderResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmProviderResponse.parse_obj(json)

class RepositoriesOfScmProviderEndpoint(IDEndpoint):
    path = '/v1/scmProviders/{id}/repositories'

    def fields(self, *, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> RepositoriesOfScmProviderEndpoint:
        '''Fields to return for included related types.

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.RepositoriesOfScmProviderEndpoint
        '''
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    def filter(self, *, id: Union[str, list[str]]=None) -> RepositoriesOfScmProviderEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.RepositoriesOfScmProviderEndpoint
        '''
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def limit(self, number: int=None) -> RepositoriesOfScmProviderEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.RepositoriesOfScmProviderEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> ScmRepositoriesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: ScmRepositoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmRepositoriesResponse.parse_obj(json)

