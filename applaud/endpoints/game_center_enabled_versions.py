from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CompatibleVersionsLinkagesOfGameCenterEnabledVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions'

    def limit(self, number: int=None) -> CompatibleVersionsLinkagesOfGameCenterEnabledVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CompatibleVersionsLinkagesOfGameCenterEnabledVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterEnabledVersionCompatibleVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterEnabledVersionCompatibleVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterEnabledVersionCompatibleVersionsLinkagesResponse.parse_obj(json)

    def create(self, request: GameCenterEnabledVersionCompatibleVersionsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterEnabledVersionCompatibleVersionsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def update(self, request: GameCenterEnabledVersionCompatibleVersionsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterEnabledVersionCompatibleVersionsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

    def delete(self, request: GameCenterEnabledVersionCompatibleVersionsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterEnabledVersionCompatibleVersionsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class CompatibleVersionsOfGameCenterEnabledVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterEnabledVersions/{id}/compatibleVersions'

    def fields(self, *, game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]]=None) -> CompatibleVersionsOfGameCenterEnabledVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_enabled_version: the fields to include for returned resources of type gameCenterEnabledVersions
        :type game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.CompatibleVersionsOfGameCenterEnabledVersionEndpoint
        '''
        if game_center_enabled_version: self._set_fields('gameCenterEnabledVersions',game_center_enabled_version if type(game_center_enabled_version) is list else [game_center_enabled_version])
        return self
        
    class Include(StringEnum):
        COMPATIBLE_VERSIONS = 'compatibleVersions'

    def filter(self, *, platform: Union[Platform, list[Platform]]=None, version_string: Union[str, list[str]]=None, app: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> CompatibleVersionsOfGameCenterEnabledVersionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param version_string: filter by attribute 'versionString'
        :type version_string: Union[str, list[str]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.CompatibleVersionsOfGameCenterEnabledVersionEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if version_string: self._set_filter('versionString', version_string if type(version_string) is list else [version_string])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> CompatibleVersionsOfGameCenterEnabledVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CompatibleVersionsOfGameCenterEnabledVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, version_string: SortOrder=None) -> CompatibleVersionsOfGameCenterEnabledVersionEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.CompatibleVersionsOfGameCenterEnabledVersionEndpoint
        '''
        if version_string: self.sort_expressions.append('versionString' if version_string == SortOrder.ASC else '-versionString')
        return self
        
    def limit(self, number: int=None, *, compatible_versions: int=None) -> CompatibleVersionsOfGameCenterEnabledVersionEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param compatible_versions: maximum number of related compatibleVersions returned (when they are included). The maximum limit is 50
        :type compatible_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.CompatibleVersionsOfGameCenterEnabledVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if compatible_versions and compatible_versions > 50:
            raise ValueError(f'The maximum limit of compatible_versions is 50')
        if compatible_versions: self._set_limit(compatible_versions, 'compatibleVersions')

        return self

    def get(self) -> GameCenterEnabledVersionsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: GameCenterEnabledVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterEnabledVersionsResponse.parse_obj(json)

class GameCenterEnabledVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterEnabledVersions/{id}'

    @endpoint('/v1/gameCenterEnabledVersions/{id}/compatibleVersions')
    def compatible_versions(self) -> CompatibleVersionsOfGameCenterEnabledVersionEndpoint:
        return CompatibleVersionsOfGameCenterEnabledVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterEnabledVersions/{id}/relationships/compatibleVersions')
    def compatible_versions_linkages(self) -> CompatibleVersionsLinkagesOfGameCenterEnabledVersionEndpoint:
        return CompatibleVersionsLinkagesOfGameCenterEnabledVersionEndpoint(self.id, self.session)
        
