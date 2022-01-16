from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppScreenshotSetsEndpoint(Endpoint):
    path = '/v1/appScreenshotSets'

    def create(self, request: AppScreenshotSetCreateRequest) -> AppScreenshotSetResponse:
        '''Create the resource.

        :param request: AppScreenshotSet representation
        :type request: AppScreenshotSetCreateRequest

        :returns: Single AppScreenshotSet
        :rtype: AppScreenshotSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppScreenshotSetResponse.parse_obj(json)

class AppScreenshotSetEndpoint(IDEndpoint):
    path = '/v1/appScreenshotSets/{id}'

    @endpoint('/v1/appScreenshotSets/{id}/appScreenshots')
    def app_screenshots(self) -> AppScreenshotsOfAppScreenshotSetEndpoint:
        return AppScreenshotsOfAppScreenshotSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/appScreenshotSets/{id}/relationships/appScreenshots')
    def app_screenshots_linkages(self) -> AppScreenshotsLinkagesOfAppScreenshotSetEndpoint:
        return AppScreenshotsLinkagesOfAppScreenshotSetEndpoint(self.id, self.session)
        
    def fields(self, *, app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]]=None, app_screenshot: Union[AppScreenshotField, list[AppScreenshotField]]=None) -> AppScreenshotSetEndpoint:
        '''Fields to return for included related types.

        :param app_screenshot_set: the fields to include for returned resources of type appScreenshotSets
        :type app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]] = None

        :param app_screenshot: the fields to include for returned resources of type appScreenshots
        :type app_screenshot: Union[AppScreenshotField, list[AppScreenshotField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetEndpoint
        '''
        if app_screenshot_set: self._set_fields('appScreenshotSets',app_screenshot_set if type(app_screenshot_set) is list else [app_screenshot_set])
        if app_screenshot: self._set_fields('appScreenshots',app_screenshot if type(app_screenshot) is list else [app_screenshot])
        return self
        
    class Include(StringEnum):
        APP_SCREENSHOTS = 'appScreenshots'
        APP_STORE_VERSION_LOCALIZATION = 'appStoreVersionLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> AppScreenshotSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_screenshots: int=None) -> AppScreenshotSetEndpoint:
        '''Number of included related resources to return.

        :param app_screenshots: maximum number of related appScreenshots returned (when they are included). The maximum limit is 50
        :type app_screenshots: int = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetEndpoint
        '''
        if app_screenshots and app_screenshots > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_screenshots: self._set_limit('appScreenshots', app_screenshots)

        return self

    def get(self) -> AppScreenshotSetResponse:
        '''Get the resource.

        :returns: Single AppScreenshotSet
        :rtype: AppScreenshotSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppScreenshotSetResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppScreenshotsLinkagesOfAppScreenshotSetEndpoint(IDEndpoint):
    path = '/v1/appScreenshotSets/{id}/relationships/appScreenshots'

    def limit(self, number: int=None) -> AppScreenshotsLinkagesOfAppScreenshotSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotsLinkagesOfAppScreenshotSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> AppScreenshotSetAppScreenshotsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppScreenshotSetAppScreenshotsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppScreenshotSetAppScreenshotsLinkagesResponse.parse_obj(json)

    def update(self, request: AppScreenshotSetAppScreenshotsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: AppScreenshotSetAppScreenshotsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class AppScreenshotsOfAppScreenshotSetEndpoint(IDEndpoint):
    path = '/v1/appScreenshotSets/{id}/appScreenshots'

    def fields(self, *, app_screenshot: Union[AppScreenshotField, list[AppScreenshotField]]=None) -> AppScreenshotsOfAppScreenshotSetEndpoint:
        '''Fields to return for included related types.

        :param app_screenshot: the fields to include for returned resources of type appScreenshots
        :type app_screenshot: Union[AppScreenshotField, list[AppScreenshotField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotsOfAppScreenshotSetEndpoint
        '''
        if app_screenshot: self._set_fields('appScreenshots',app_screenshot if type(app_screenshot) is list else [app_screenshot])
        return self
        
    def limit(self, number: int=None) -> AppScreenshotsOfAppScreenshotSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotsOfAppScreenshotSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> AppScreenshotsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppScreenshotsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppScreenshotsResponse.parse_obj(json)

