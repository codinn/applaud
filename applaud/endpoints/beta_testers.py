from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaTestersEndpoint(Endpoint):
    path = '/v1/betaTesters'

    def fields(self, *, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, app: Union[AppField, list[AppField]]=None, build: Union[BuildField, list[BuildField]]=None, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None) -> BetaTestersEndpoint:
        '''Fields to return for included related types.

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaTestersEndpoint
        '''
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        return self
        
    class Include(StringEnum):
        APPS = 'apps'
        BETA_GROUPS = 'betaGroups'
        BUILDS = 'builds'

    def filter(self, *, email: Union[str, list[str]]=None, first_name: Union[str, list[str]]=None, invite_type: Union[BetaInviteType, list[BetaInviteType]]=None, last_name: Union[str, list[str]]=None, apps: Union[str, list[str]]=None, beta_groups: Union[str, list[str]]=None, builds: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> BetaTestersEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param email: filter by attribute 'email'
        :type email: Union[str, list[str]] = None

        :param first_name: filter by attribute 'firstName'
        :type first_name: Union[str, list[str]] = None

        :param invite_type: filter by attribute 'inviteType'
        :type invite_type: Union[BetaInviteType, list[BetaInviteType]] = None

        :param last_name: filter by attribute 'lastName'
        :type last_name: Union[str, list[str]] = None

        :param apps: filter by id(s) of related 'apps'
        :type apps: Union[str, list[str]] = None

        :param beta_groups: filter by id(s) of related 'betaGroups'
        :type beta_groups: Union[str, list[str]] = None

        :param builds: filter by id(s) of related 'builds'
        :type builds: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaTestersEndpoint
        '''
        if email: self._set_filter('email', email if type(email) is list else [email])
        
        if first_name: self._set_filter('firstName', first_name if type(first_name) is list else [first_name])
        
        if invite_type: self._set_filter('inviteType', invite_type if type(invite_type) is list else [invite_type])
        
        if last_name: self._set_filter('lastName', last_name if type(last_name) is list else [last_name])
        
        if apps: self._set_filter('apps', apps if type(apps) is list else [apps])
        
        if beta_groups: self._set_filter('betaGroups', beta_groups if type(beta_groups) is list else [beta_groups])
        
        if builds: self._set_filter('builds', builds if type(builds) is list else [builds])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BetaTestersEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaTestersEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, email: SortOrder=None, first_name: SortOrder=None, invite_type: SortOrder=None, last_name: SortOrder=None) -> BetaTestersEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BetaTestersEndpoint
        '''
        if email: self.sort_expressions.append('email' if email == SortOrder.ASC else '-email')
        if first_name: self.sort_expressions.append('firstName' if first_name == SortOrder.ASC else '-firstName')
        if invite_type: self.sort_expressions.append('inviteType' if invite_type == SortOrder.ASC else '-inviteType')
        if last_name: self.sort_expressions.append('lastName' if last_name == SortOrder.ASC else '-lastName')
        return self
        
    def limit(self, number: int=None, *, apps: int=None, beta_groups: int=None, builds: int=None) -> BetaTestersEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param apps: maximum number of related apps returned (when they are included). The maximum limit is 50
        :type apps: int = None

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaTestersEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if apps and apps > 50:
            raise ValueError(f'The maximum limit is 50')
        if apps: self._set_limit('apps', apps)

        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit is 50')
        if beta_groups: self._set_limit('betaGroups', beta_groups)

        if builds and builds > 50:
            raise ValueError(f'The maximum limit is 50')
        if builds: self._set_limit('builds', builds)

        return self

    def get(self) -> BetaTestersResponse:
        '''Get one or more resources.

        :returns: List of BetaTesters
        :rtype: BetaTestersResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaTestersResponse.parse_obj(json)

    def create(self, request: BetaTesterCreateRequest) -> BetaTesterResponse:
        '''Create the resource.

        :param request: BetaTester representation
        :type request: BetaTesterCreateRequest

        :returns: Single BetaTester
        :rtype: BetaTesterResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BetaTesterResponse.parse_obj(json)

class BetaTesterEndpoint(IDEndpoint):
    path = '/v1/betaTesters/{id}'

    @endpoint('/v1/betaTesters/{id}/apps')
    def apps(self) -> AppsOfBetaTesterEndpoint:
        return AppsOfBetaTesterEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaTesters/{id}/betaGroups')
    def beta_groups(self) -> BetaGroupsOfBetaTesterEndpoint:
        return BetaGroupsOfBetaTesterEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaTesters/{id}/builds')
    def builds(self) -> BuildsOfBetaTesterEndpoint:
        return BuildsOfBetaTesterEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaTesters/{id}/relationships/apps')
    def apps_linkages(self) -> AppsLinkagesOfBetaTesterEndpoint:
        return AppsLinkagesOfBetaTesterEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaTesters/{id}/relationships/betaGroups')
    def beta_groups_linkages(self) -> BetaGroupsLinkagesOfBetaTesterEndpoint:
        return BetaGroupsLinkagesOfBetaTesterEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaTesters/{id}/relationships/builds')
    def builds_linkages(self) -> BuildsLinkagesOfBetaTesterEndpoint:
        return BuildsLinkagesOfBetaTesterEndpoint(self.id, self.session)
        
    def fields(self, *, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, app: Union[AppField, list[AppField]]=None, build: Union[BuildField, list[BuildField]]=None, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None) -> BetaTesterEndpoint:
        '''Fields to return for included related types.

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaTesterEndpoint
        '''
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        return self
        
    class Include(StringEnum):
        APPS = 'apps'
        BETA_GROUPS = 'betaGroups'
        BUILDS = 'builds'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaTesterEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaTesterEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, apps: int=None, beta_groups: int=None, builds: int=None) -> BetaTesterEndpoint:
        '''Number of included related resources to return.

        :param apps: maximum number of related apps returned (when they are included). The maximum limit is 50
        :type apps: int = None

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaTesterEndpoint
        '''
        if apps and apps > 50:
            raise ValueError(f'The maximum limit is 50')
        if apps: self._set_limit('apps', apps)

        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit is 50')
        if beta_groups: self._set_limit('betaGroups', beta_groups)

        if builds and builds > 50:
            raise ValueError(f'The maximum limit is 50')
        if builds: self._set_limit('builds', builds)

        return self

    def get(self) -> BetaTesterResponse:
        '''Get the resource.

        :returns: Single BetaTester
        :rtype: BetaTesterResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaTesterResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppsLinkagesOfBetaTesterEndpoint(IDEndpoint):
    path = '/v1/betaTesters/{id}/relationships/apps'

    def limit(self, number: int=None) -> AppsLinkagesOfBetaTesterEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppsLinkagesOfBetaTesterEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaTesterAppsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BetaTesterAppsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaTesterAppsLinkagesResponse.parse_obj(json)

    def delete(self, request: BetaTesterAppsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BetaTesterAppsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class AppsOfBetaTesterEndpoint(IDEndpoint):
    path = '/v1/betaTesters/{id}/apps'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppsOfBetaTesterEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppsOfBetaTesterEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    def limit(self, number: int=None) -> AppsOfBetaTesterEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppsOfBetaTesterEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> AppsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppsResponse.parse_obj(json)

class BetaGroupsLinkagesOfBetaTesterEndpoint(IDEndpoint):
    path = '/v1/betaTesters/{id}/relationships/betaGroups'

    def limit(self, number: int=None) -> BetaGroupsLinkagesOfBetaTesterEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsLinkagesOfBetaTesterEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaTesterBetaGroupsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BetaTesterBetaGroupsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaTesterBetaGroupsLinkagesResponse.parse_obj(json)

    def create(self, request: BetaTesterBetaGroupsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: BetaTesterBetaGroupsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: BetaTesterBetaGroupsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BetaTesterBetaGroupsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class BetaGroupsOfBetaTesterEndpoint(IDEndpoint):
    path = '/v1/betaTesters/{id}/betaGroups'

    def fields(self, *, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None) -> BetaGroupsOfBetaTesterEndpoint:
        '''Fields to return for included related types.

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsOfBetaTesterEndpoint
        '''
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        return self
        
    def limit(self, number: int=None) -> BetaGroupsOfBetaTesterEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsOfBetaTesterEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaGroupsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: BetaGroupsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupsResponse.parse_obj(json)

class BuildsLinkagesOfBetaTesterEndpoint(IDEndpoint):
    path = '/v1/betaTesters/{id}/relationships/builds'

    def limit(self, number: int=None) -> BuildsLinkagesOfBetaTesterEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsLinkagesOfBetaTesterEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> BetaTesterBuildsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BetaTesterBuildsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaTesterBuildsLinkagesResponse.parse_obj(json)

    def create(self, request: BetaTesterBuildsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: BetaTesterBuildsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: BetaTesterBuildsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BetaTesterBuildsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class BuildsOfBetaTesterEndpoint(IDEndpoint):
    path = '/v1/betaTesters/{id}/builds'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildsOfBetaTesterEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfBetaTesterEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    def limit(self, number: int=None) -> BuildsOfBetaTesterEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfBetaTesterEndpoint
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

