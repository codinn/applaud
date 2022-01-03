from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder
from ..fields import *
from typing import Union
from pydantic import parse_obj_as
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppInfoLocalizationListEndpoint(Endpoint):
    path = '/v1/appInfoLocalizations'

    def create(self, request: AppInfoLocalizationCreateRequest) -> AppInfoLocalizationResponse:
        '''Create the resource.

        :param request: AppInfoLocalization representation
        :type request: AppInfoLocalizationCreateRequest

        :returns: Single AppInfoLocalization
        :rtype: AppInfoLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_post(json)
        return AppInfoLocalizationResponse.parse_obj(response_json)

class AppInfoLocalizationEndpoint(IDEndpoint):
    path = '/v1/appInfoLocalizations/{id}'

    def fields(self, *, app_info_localization: Union[AppInfoLocalizationField, list[AppInfoLocalizationField]]=None) -> AppInfoLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_info_localization: the fields to include for returned resources of type appInfoLocalizations
        :type app_info_localization: Union[AppInfoLocalizationField, list[AppInfoLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppInfoLocalizationEndpoint
        '''
        if app_info_localization: self._set_fields('appInfoLocalizations',app_info_localization if type(app_info_localization) is list else [app_info_localization])
        return self
        
    class Include(StringEnum):
        APP_INFO = 'appInfo'

    def include(self, relationship: Union[Include, list[Include]]) -> AppInfoLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppInfoLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppInfoLocalizationResponse:
        '''Get the resource.

        :returns: Single AppInfoLocalization
        :rtype: AppInfoLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppInfoLocalizationResponse.parse_obj(json)

    def update(self, request: AppInfoLocalizationUpdateRequest) -> AppInfoLocalizationResponse:
        '''Modify the resource.

        :param request: AppInfoLocalization representation
        :type request: AppInfoLocalizationUpdateRequest

        :returns: Single AppInfoLocalization
        :rtype: AppInfoLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = request.dict(by_alias=True, exclude_none=True)
        response_json = super()._perform_patch(json)
        return AppInfoLocalizationResponse.parse_obj(response_json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

