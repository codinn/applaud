from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaGroupsEndpoint(Endpoint):
    path = '/v1/betaGroups'

    def fields(self, *, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, app: Union[AppField, list[AppField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BetaGroupsEndpoint:
        '''Fields to return for included related types.

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsEndpoint
        '''
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BETA_TESTERS = 'betaTesters'
        BUILDS = 'builds'

    def filter(self, *, is_internal_group: Union[str, list[str]]=None, name: Union[str, list[str]]=None, public_link: Union[str, list[str]]=None, public_link_enabled: Union[str, list[str]]=None, public_link_limit_enabled: Union[str, list[str]]=None, app: Union[str, list[str]]=None, builds: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> BetaGroupsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param is_internal_group: filter by attribute 'isInternalGroup'
        :type is_internal_group: Union[str, list[str]] = None

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param public_link: filter by attribute 'publicLink'
        :type public_link: Union[str, list[str]] = None

        :param public_link_enabled: filter by attribute 'publicLinkEnabled'
        :type public_link_enabled: Union[str, list[str]] = None

        :param public_link_limit_enabled: filter by attribute 'publicLinkLimitEnabled'
        :type public_link_limit_enabled: Union[str, list[str]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :param builds: filter by id(s) of related 'builds'
        :type builds: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsEndpoint
        '''
        if is_internal_group: self._set_filter('isInternalGroup', is_internal_group if type(is_internal_group) is list else [is_internal_group])
        
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if public_link: self._set_filter('publicLink', public_link if type(public_link) is list else [public_link])
        
        if public_link_enabled: self._set_filter('publicLinkEnabled', public_link_enabled if type(public_link_enabled) is list else [public_link_enabled])
        
        if public_link_limit_enabled: self._set_filter('publicLinkLimitEnabled', public_link_limit_enabled if type(public_link_limit_enabled) is list else [public_link_limit_enabled])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        if builds: self._set_filter('builds', builds if type(builds) is list else [builds])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BetaGroupsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, created_date: SortOrder=None, name: SortOrder=None, public_link_enabled: SortOrder=None, public_link_limit: SortOrder=None) -> BetaGroupsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsEndpoint
        '''
        if created_date: self.sort_expressions.append('createdDate' if created_date == SortOrder.ASC else '-createdDate')
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if public_link_enabled: self.sort_expressions.append('publicLinkEnabled' if public_link_enabled == SortOrder.ASC else '-publicLinkEnabled')
        if public_link_limit: self.sort_expressions.append('publicLinkLimit' if public_link_limit == SortOrder.ASC else '-publicLinkLimit')
        return self
        
    def limit(self, number: int=None, *, beta_testers: int=None, builds: int=None) -> BetaGroupsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param beta_testers: maximum number of related betaTesters returned (when they are included). The maximum limit is 50
        :type beta_testers: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 1000
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if beta_testers and beta_testers > 50:
            raise ValueError(f'The maximum limit is 50')
        if beta_testers: self._set_limit('betaTesters', beta_testers)

        if builds and builds > 1000:
            raise ValueError(f'The maximum limit is 1000')
        if builds: self._set_limit('builds', builds)

        return self

    def get(self) -> BetaGroupsResponse:
        '''Get one or more resources.

        :returns: List of BetaGroups
        :rtype: BetaGroupsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupsResponse.parse_obj(json)

    def create(self, request: BetaGroupCreateRequest) -> BetaGroupResponse:
        '''Create the resource.

        :param request: BetaGroup representation
        :type request: BetaGroupCreateRequest

        :returns: Single BetaGroup
        :rtype: BetaGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BetaGroupResponse.parse_obj(json)

class BetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}'

    @endpoint('/v1/betaGroups/{id}/app')
    def app(self) -> AppOfBetaGroupEndpoint:
        return AppOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/betaTesters')
    def beta_testers(self) -> BetaTestersOfBetaGroupEndpoint:
        return BetaTestersOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/builds')
    def builds(self) -> BuildsOfBetaGroupEndpoint:
        return BuildsOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/relationships/betaTesters')
    def beta_testers_linkages(self) -> BetaTestersLinkagesOfBetaGroupEndpoint:
        return BetaTestersLinkagesOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/relationships/builds')
    def builds_linkages(self) -> BuildsLinkagesOfBetaGroupEndpoint:
        return BuildsLinkagesOfBetaGroupEndpoint(self.id, self.session)
        
    def fields(self, *, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, app: Union[AppField, list[AppField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BetaGroupEndpoint:
        '''Fields to return for included related types.

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupEndpoint
        '''
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BETA_TESTERS = 'betaTesters'
        BUILDS = 'builds'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, beta_testers: int=None, builds: int=None) -> BetaGroupEndpoint:
        '''Number of included related resources to return.

        :param beta_testers: maximum number of related betaTesters returned (when they are included). The maximum limit is 50
        :type beta_testers: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 1000
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupEndpoint
        '''
        if beta_testers and beta_testers > 50:
            raise ValueError(f'The maximum limit is 50')
        if beta_testers: self._set_limit('betaTesters', beta_testers)

        if builds and builds > 1000:
            raise ValueError(f'The maximum limit is 1000')
        if builds: self._set_limit('builds', builds)

        return self

    def get(self) -> BetaGroupResponse:
        '''Get the resource.

        :returns: Single BetaGroup
        :rtype: BetaGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupResponse.parse_obj(json)

    def update(self, request: BetaGroupUpdateRequest) -> BetaGroupResponse:
        '''Modify the resource.

        :param request: BetaGroup representation
        :type request: BetaGroupUpdateRequest

        :returns: Single BetaGroup
        :rtype: BetaGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BetaGroupResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppOfBetaGroupEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfBetaGroupEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    def get(self) -> AppResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppResponse.parse_obj(json)

class BetaTestersLinkagesOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/relationships/betaTesters'

    def limit(self, number: int=None) -> BetaTestersLinkagesOfBetaGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaTestersLinkagesOfBetaGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaGroupBetaTestersLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BetaGroupBetaTestersLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupBetaTestersLinkagesResponse.parse_obj(json)

    def create(self, request: BetaGroupBetaTestersLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: BetaGroupBetaTestersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: BetaGroupBetaTestersLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BetaGroupBetaTestersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class BetaTestersOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/betaTesters'

    def fields(self, *, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None) -> BetaTestersOfBetaGroupEndpoint:
        '''Fields to return for included related types.

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaTestersOfBetaGroupEndpoint
        '''
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        return self
        
    def limit(self, number: int=None) -> BetaTestersOfBetaGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaTestersOfBetaGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaTestersResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BetaTestersResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaTestersResponse.parse_obj(json)

class BuildsLinkagesOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/relationships/builds'

    def limit(self, number: int=None) -> BuildsLinkagesOfBetaGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsLinkagesOfBetaGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaGroupBuildsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BetaGroupBuildsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupBuildsLinkagesResponse.parse_obj(json)

    def create(self, request: BetaGroupBuildsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: BetaGroupBuildsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: BetaGroupBuildsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BetaGroupBuildsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class BuildsOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/builds'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildsOfBetaGroupEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfBetaGroupEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    def limit(self, number: int=None) -> BuildsOfBetaGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfBetaGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BuildsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BuildsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildsResponse.parse_obj(json)

