from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppScreenshotsEndpoint(Endpoint):
    path = '/v1/appScreenshots'

    def create(self, request: AppScreenshotCreateRequest) -> AppScreenshotResponse:
        '''Create the resource.

        :param request: AppScreenshot representation
        :type request: AppScreenshotCreateRequest

        :returns: Single AppScreenshot
        :rtype: AppScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppScreenshotResponse.parse_obj(json)

class AppScreenshotEndpoint(IDEndpoint):
    path = '/v1/appScreenshots/{id}'

    def fields(self, *, app_screenshot: Union[AppScreenshotField, list[AppScreenshotField]]=None) -> AppScreenshotEndpoint:
        '''Fields to return for included related types.

        :param app_screenshot: the fields to include for returned resources of type appScreenshots
        :type app_screenshot: Union[AppScreenshotField, list[AppScreenshotField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotEndpoint
        '''
        if app_screenshot: self._set_fields('appScreenshots',app_screenshot if type(app_screenshot) is list else [app_screenshot])
        return self
        
    class Include(StringEnum):
        APP_SCREENSHOT_SET = 'appScreenshotSet'

    def include(self, relationship: Union[Include, list[Include]]) -> AppScreenshotEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppScreenshotResponse:
        '''Get the resource.

        :returns: Single AppScreenshot
        :rtype: AppScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppScreenshotResponse.parse_obj(json)

    def update(self, request: AppScreenshotUpdateRequest) -> AppScreenshotResponse:
        '''Modify the resource.

        :param request: AppScreenshot representation
        :type request: AppScreenshotUpdateRequest

        :returns: Single AppScreenshot
        :rtype: AppScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppScreenshotResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

