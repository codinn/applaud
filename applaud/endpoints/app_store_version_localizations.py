from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionLocalizationsEndpoint(Endpoint):
    path = '/v1/appStoreVersionLocalizations'

    def create(self, request: AppStoreVersionLocalizationCreateRequest) -> AppStoreVersionLocalizationResponse:
        '''Create the resource.

        :param request: AppStoreVersionLocalization representation
        :type request: AppStoreVersionLocalizationCreateRequest

        :returns: Single AppStoreVersionLocalization
        :rtype: AppStoreVersionLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreVersionLocalizationResponse.parse_obj(json)

class AppStoreVersionLocalizationEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionLocalizations/{id}'

    @endpoint('/v1/appStoreVersionLocalizations/{id}/appPreviewSets')
    def app_preview_sets(self) -> AppPreviewSetsOfAppStoreVersionLocalizationEndpoint:
        return AppPreviewSetsOfAppStoreVersionLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersionLocalizations/{id}/appScreenshotSets')
    def app_screenshot_sets(self) -> AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint:
        return AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None, app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]]=None, app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]]=None) -> AppStoreVersionLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_localization: the fields to include for returned resources of type appStoreVersionLocalizations
        :type app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]] = None

        :param app_screenshot_set: the fields to include for returned resources of type appScreenshotSets
        :type app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]] = None

        :param app_preview_set: the fields to include for returned resources of type appPreviewSets
        :type app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionLocalizationEndpoint
        '''
        if app_store_version_localization: self._set_fields('appStoreVersionLocalizations',app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        if app_screenshot_set: self._set_fields('appScreenshotSets',app_screenshot_set if type(app_screenshot_set) is list else [app_screenshot_set])
        if app_preview_set: self._set_fields('appPreviewSets',app_preview_set if type(app_preview_set) is list else [app_preview_set])
        return self
        
    class Include(StringEnum):
        APP_PREVIEW_SETS = 'appPreviewSets'
        APP_SCREENSHOT_SETS = 'appScreenshotSets'
        APP_STORE_VERSION = 'appStoreVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_preview_sets: int=None, app_screenshot_sets: int=None) -> AppStoreVersionLocalizationEndpoint:
        '''Number of included related resources to return.

        :param app_preview_sets: maximum number of related appPreviewSets returned (when they are included). The maximum limit is 50
        :type app_preview_sets: int = None

        :param app_screenshot_sets: maximum number of related appScreenshotSets returned (when they are included). The maximum limit is 50
        :type app_screenshot_sets: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionLocalizationEndpoint
        '''
        if app_preview_sets and app_preview_sets > 50:
            raise ValueError(f'The maximum limit of app_preview_sets is 50')
        if app_preview_sets: self._set_limit(app_preview_sets, 'appPreviewSets')

        if app_screenshot_sets and app_screenshot_sets > 50:
            raise ValueError(f'The maximum limit of app_screenshot_sets is 50')
        if app_screenshot_sets: self._set_limit(app_screenshot_sets, 'appScreenshotSets')

        return self

    def get(self) -> AppStoreVersionLocalizationResponse:
        '''Get the resource.

        :returns: Single AppStoreVersionLocalization
        :rtype: AppStoreVersionLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionLocalizationResponse.parse_obj(json)

    def update(self, request: AppStoreVersionLocalizationUpdateRequest) -> AppStoreVersionLocalizationResponse:
        '''Modify the resource.

        :param request: AppStoreVersionLocalization representation
        :type request: AppStoreVersionLocalizationUpdateRequest

        :returns: Single AppStoreVersionLocalization
        :rtype: AppStoreVersionLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppStoreVersionLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppPreviewSetsOfAppStoreVersionLocalizationEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionLocalizations/{id}/appPreviewSets'

    def fields(self, *, app_preview: Union[AppPreviewField, list[AppPreviewField]]=None, app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]]=None) -> AppPreviewSetsOfAppStoreVersionLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_preview: the fields to include for returned resources of type appPreviews
        :type app_preview: Union[AppPreviewField, list[AppPreviewField]] = None

        :param app_preview_set: the fields to include for returned resources of type appPreviewSets
        :type app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetsOfAppStoreVersionLocalizationEndpoint
        '''
        if app_preview: self._set_fields('appPreviews',app_preview if type(app_preview) is list else [app_preview])
        if app_preview_set: self._set_fields('appPreviewSets',app_preview_set if type(app_preview_set) is list else [app_preview_set])
        return self
        
    class Include(StringEnum):
        APP_PREVIEWS = 'appPreviews'

    def filter(self, *, preview_type: Union[PreviewType, list[PreviewType]]=None) -> AppPreviewSetsOfAppStoreVersionLocalizationEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param preview_type: filter by attribute 'previewType'
        :type preview_type: Union[PreviewType, list[PreviewType]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetsOfAppStoreVersionLocalizationEndpoint
        '''
        if preview_type: self._set_filter('previewType', preview_type if type(preview_type) is list else [preview_type])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppPreviewSetsOfAppStoreVersionLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetsOfAppStoreVersionLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_previews: int=None) -> AppPreviewSetsOfAppStoreVersionLocalizationEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_previews: maximum number of related appPreviews returned (when they are included). The maximum limit is 50
        :type app_previews: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetsOfAppStoreVersionLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_previews and app_previews > 50:
            raise ValueError(f'The maximum limit of app_previews is 50')
        if app_previews: self._set_limit(app_previews, 'appPreviews')

        return self

    def get(self) -> AppPreviewSetsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppPreviewSetsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPreviewSetsResponse.parse_obj(json)

class AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionLocalizations/{id}/appScreenshotSets'

    def fields(self, *, app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]]=None, app_screenshot: Union[AppScreenshotField, list[AppScreenshotField]]=None) -> AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_screenshot_set: the fields to include for returned resources of type appScreenshotSets
        :type app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]] = None

        :param app_screenshot: the fields to include for returned resources of type appScreenshots
        :type app_screenshot: Union[AppScreenshotField, list[AppScreenshotField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint
        '''
        if app_screenshot_set: self._set_fields('appScreenshotSets',app_screenshot_set if type(app_screenshot_set) is list else [app_screenshot_set])
        if app_screenshot: self._set_fields('appScreenshots',app_screenshot if type(app_screenshot) is list else [app_screenshot])
        return self
        
    class Include(StringEnum):
        APP_SCREENSHOTS = 'appScreenshots'

    def filter(self, *, screenshot_display_type: Union[ScreenshotDisplayType, list[ScreenshotDisplayType]]=None) -> AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param screenshot_display_type: filter by attribute 'screenshotDisplayType'
        :type screenshot_display_type: Union[ScreenshotDisplayType, list[ScreenshotDisplayType]] = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint
        '''
        if screenshot_display_type: self._set_filter('screenshotDisplayType', screenshot_display_type if type(screenshot_display_type) is list else [screenshot_display_type])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_screenshots: int=None) -> AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_screenshots: maximum number of related appScreenshots returned (when they are included). The maximum limit is 50
        :type app_screenshots: int = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetsOfAppStoreVersionLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_screenshots and app_screenshots > 50:
            raise ValueError(f'The maximum limit of app_screenshots is 50')
        if app_screenshots: self._set_limit(app_screenshots, 'appScreenshots')

        return self

    def get(self) -> AppScreenshotSetsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppScreenshotSetsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppScreenshotSetsResponse.parse_obj(json)

