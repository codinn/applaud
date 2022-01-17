from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppClipAdvancedExperiencesEndpoint(Endpoint):
    path = '/v1/appClipAdvancedExperiences'

    def create(self, request: AppClipAdvancedExperienceCreateRequest) -> AppClipAdvancedExperienceResponse:
        '''Create the resource.

        :param request: AppClipAdvancedExperience representation
        :type request: AppClipAdvancedExperienceCreateRequest

        :returns: Single AppClipAdvancedExperience
        :rtype: AppClipAdvancedExperienceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppClipAdvancedExperienceResponse.parse_obj(json)

class AppClipAdvancedExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipAdvancedExperiences/{id}'

    def fields(self, *, app_clip_advanced_experience: Union[AppClipAdvancedExperienceField, list[AppClipAdvancedExperienceField]]=None) -> AppClipAdvancedExperienceEndpoint:
        '''Fields to return for included related types.

        :param app_clip_advanced_experience: the fields to include for returned resources of type appClipAdvancedExperiences
        :type app_clip_advanced_experience: Union[AppClipAdvancedExperienceField, list[AppClipAdvancedExperienceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipAdvancedExperienceEndpoint
        '''
        if app_clip_advanced_experience: self._set_fields('appClipAdvancedExperiences',app_clip_advanced_experience if type(app_clip_advanced_experience) is list else [app_clip_advanced_experience])
        return self
        
    class Include(StringEnum):
        APP_CLIP = 'appClip'
        HEADER_IMAGE = 'headerImage'
        LOCALIZATIONS = 'localizations'

    def include(self, relationship: Union[Include, list[Include]]) -> AppClipAdvancedExperienceEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipAdvancedExperienceEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, localizations: int=None) -> AppClipAdvancedExperienceEndpoint:
        '''Number of included related resources to return.

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipAdvancedExperienceEndpoint
        '''
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        return self

    def get(self) -> AppClipAdvancedExperienceResponse:
        '''Get the resource.

        :returns: Single AppClipAdvancedExperience
        :rtype: AppClipAdvancedExperienceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipAdvancedExperienceResponse.parse_obj(json)

    def update(self, request: AppClipAdvancedExperienceUpdateRequest) -> AppClipAdvancedExperienceResponse:
        '''Modify the resource.

        :param request: AppClipAdvancedExperience representation
        :type request: AppClipAdvancedExperienceUpdateRequest

        :returns: Single AppClipAdvancedExperience
        :rtype: AppClipAdvancedExperienceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppClipAdvancedExperienceResponse.parse_obj(json)

