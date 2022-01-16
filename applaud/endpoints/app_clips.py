from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppClipEndpoint(IDEndpoint):
    path = '/v1/appClips/{id}'

    @endpoint('/v1/appClips/{id}/appClipAdvancedExperiences')
    def app_clip_advanced_experiences(self) -> AppClipAdvancedExperiencesOfAppClipEndpoint:
        return AppClipAdvancedExperiencesOfAppClipEndpoint(self.id, self.session)
        
    @endpoint('/v1/appClips/{id}/appClipDefaultExperiences')
    def app_clip_default_experiences(self) -> AppClipDefaultExperiencesOfAppClipEndpoint:
        return AppClipDefaultExperiencesOfAppClipEndpoint(self.id, self.session)
        
    def fields(self, *, app_clip: Union[AppClipField, list[AppClipField]]=None, app_clip_advanced_experience: Union[AppClipAdvancedExperienceField, list[AppClipAdvancedExperienceField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None) -> AppClipEndpoint:
        '''Fields to return for included related types.

        :param app_clip: the fields to include for returned resources of type appClips
        :type app_clip: Union[AppClipField, list[AppClipField]] = None

        :param app_clip_advanced_experience: the fields to include for returned resources of type appClipAdvancedExperiences
        :type app_clip_advanced_experience: Union[AppClipAdvancedExperienceField, list[AppClipAdvancedExperienceField]] = None

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipEndpoint
        '''
        if app_clip: self._set_fields('appClips',app_clip if type(app_clip) is list else [app_clip])
        if app_clip_advanced_experience: self._set_fields('appClipAdvancedExperiences',app_clip_advanced_experience if type(app_clip_advanced_experience) is list else [app_clip_advanced_experience])
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        APP_CLIP_DEFAULT_EXPERIENCES = 'appClipDefaultExperiences'

    def include(self, relationship: Union[Include, list[Include]]) -> AppClipEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_clip_default_experiences: int=None) -> AppClipEndpoint:
        '''Number of included related resources to return.

        :param app_clip_default_experiences: maximum number of related appClipDefaultExperiences returned (when they are included). The maximum limit is 50
        :type app_clip_default_experiences: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipEndpoint
        '''
        if app_clip_default_experiences and app_clip_default_experiences > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_clip_default_experiences: self._set_limit('appClipDefaultExperiences', app_clip_default_experiences)

        return self

    def get(self) -> AppClipResponse:
        '''Get the resource.

        :returns: Single AppClip
        :rtype: AppClipResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipResponse.parse_obj(json)

class AppClipAdvancedExperiencesOfAppClipEndpoint(IDEndpoint):
    path = '/v1/appClips/{id}/appClipAdvancedExperiences'

    def fields(self, *, app_clip_advanced_experience: Union[AppClipAdvancedExperienceField, list[AppClipAdvancedExperienceField]]=None, app_clip_advanced_experience_localization: Union[AppClipAdvancedExperienceLocalizationField, list[AppClipAdvancedExperienceLocalizationField]]=None) -> AppClipAdvancedExperiencesOfAppClipEndpoint:
        '''Fields to return for included related types.

        :param app_clip_advanced_experience: the fields to include for returned resources of type appClipAdvancedExperiences
        :type app_clip_advanced_experience: Union[AppClipAdvancedExperienceField, list[AppClipAdvancedExperienceField]] = None

        :param app_clip_advanced_experience_localization: the fields to include for returned resources of type appClipAdvancedExperienceLocalizations
        :type app_clip_advanced_experience_localization: Union[AppClipAdvancedExperienceLocalizationField, list[AppClipAdvancedExperienceLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipAdvancedExperiencesOfAppClipEndpoint
        '''
        if app_clip_advanced_experience: self._set_fields('appClipAdvancedExperiences',app_clip_advanced_experience if type(app_clip_advanced_experience) is list else [app_clip_advanced_experience])
        if app_clip_advanced_experience_localization: self._set_fields('appClipAdvancedExperienceLocalizations',app_clip_advanced_experience_localization if type(app_clip_advanced_experience_localization) is list else [app_clip_advanced_experience_localization])
        return self
        
    class Include(StringEnum):
        LOCALIZATIONS = 'localizations'

    def filter(self, *, action: Union[AppClipAction, list[AppClipAction]]=None, place_status: Union[AppClipAdvancedExperiencePlaceStatus, list[AppClipAdvancedExperiencePlaceStatus]]=None, status: Union[AppClipAdvancedExperienceStatus, list[AppClipAdvancedExperienceStatus]]=None) -> AppClipAdvancedExperiencesOfAppClipEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param action: filter by attribute 'action'
        :type action: Union[AppClipAction, list[AppClipAction]] = None

        :param place_status: filter by attribute 'placeStatus'
        :type place_status: Union[AppClipAdvancedExperiencePlaceStatus, list[AppClipAdvancedExperiencePlaceStatus]] = None

        :param status: filter by attribute 'status'
        :type status: Union[AppClipAdvancedExperienceStatus, list[AppClipAdvancedExperienceStatus]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipAdvancedExperiencesOfAppClipEndpoint
        '''
        if action: self._set_filter('action', action if type(action) is list else [action])
        
        if place_status: self._set_filter('placeStatus', place_status if type(place_status) is list else [place_status])
        
        if status: self._set_filter('status', status if type(status) is list else [status])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppClipAdvancedExperiencesOfAppClipEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipAdvancedExperiencesOfAppClipEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None) -> AppClipAdvancedExperiencesOfAppClipEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipAdvancedExperiencesOfAppClipEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit is 50')
        if localizations: self._set_limit('localizations', localizations)

        return self

    def get(self) -> AppClipAdvancedExperiencesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppClipAdvancedExperiencesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipAdvancedExperiencesResponse.parse_obj(json)

class AppClipDefaultExperiencesOfAppClipEndpoint(IDEndpoint):
    path = '/v1/appClips/{id}/appClipDefaultExperiences'

    def fields(self, *, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]]=None) -> AppClipDefaultExperiencesOfAppClipEndpoint:
        '''Fields to return for included related types.

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :param app_clip_default_experience_localization: the fields to include for returned resources of type appClipDefaultExperienceLocalizations
        :type app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperiencesOfAppClipEndpoint
        '''
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        if app_clip_default_experience_localization: self._set_fields('appClipDefaultExperienceLocalizations',app_clip_default_experience_localization if type(app_clip_default_experience_localization) is list else [app_clip_default_experience_localization])
        return self
        
    class Include(StringEnum):
        APP_CLIP_DEFAULT_EXPERIENCE_LOCALIZATIONS = 'appClipDefaultExperienceLocalizations'

    def exists(self, *, release_with_app_store_version: bool=None) -> AppClipDefaultExperiencesOfAppClipEndpoint:
        ''' Filter by existence or non-existence of related resource.
        
        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperiencesOfAppClipEndpoint
        '''
        if release_with_app_store_version == None:
            return
        
        self._set_exists('releaseWithAppStoreVersion', 'true' if release_with_app_store_version  else 'false')
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppClipDefaultExperiencesOfAppClipEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperiencesOfAppClipEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_clip_default_experience_localizations: int=None) -> AppClipDefaultExperiencesOfAppClipEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_clip_default_experience_localizations: maximum number of related appClipDefaultExperienceLocalizations returned (when they are included). The maximum limit is 50
        :type app_clip_default_experience_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperiencesOfAppClipEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        if app_clip_default_experience_localizations and app_clip_default_experience_localizations > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_clip_default_experience_localizations: self._set_limit('appClipDefaultExperienceLocalizations', app_clip_default_experience_localizations)

        return self

    def get(self) -> AppClipDefaultExperiencesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppClipDefaultExperiencesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperiencesResponse.parse_obj(json)

