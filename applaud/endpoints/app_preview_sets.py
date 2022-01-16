from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppPreviewSetsEndpoint(Endpoint):
    path = '/v1/appPreviewSets'

    def create(self, request: AppPreviewSetCreateRequest) -> AppPreviewSetResponse:
        '''Create the resource.

        :param request: AppPreviewSet representation
        :type request: AppPreviewSetCreateRequest

        :returns: Single AppPreviewSet
        :rtype: AppPreviewSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppPreviewSetResponse.parse_obj(json)

class AppPreviewSetEndpoint(IDEndpoint):
    path = '/v1/appPreviewSets/{id}'

    @endpoint('/v1/appPreviewSets/{id}/appPreviews')
    def app_previews(self) -> AppPreviewsOfAppPreviewSetEndpoint:
        return AppPreviewsOfAppPreviewSetEndpoint(self.id, self.session)
        
    @endpoint('/v1/appPreviewSets/{id}/relationships/appPreviews')
    def app_previews_linkages(self) -> AppPreviewsLinkagesOfAppPreviewSetEndpoint:
        return AppPreviewsLinkagesOfAppPreviewSetEndpoint(self.id, self.session)
        
    def fields(self, *, app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]]=None, app_preview: Union[AppPreviewField, list[AppPreviewField]]=None) -> AppPreviewSetEndpoint:
        '''Fields to return for included related types.

        :param app_preview_set: the fields to include for returned resources of type appPreviewSets
        :type app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]] = None

        :param app_preview: the fields to include for returned resources of type appPreviews
        :type app_preview: Union[AppPreviewField, list[AppPreviewField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetEndpoint
        '''
        if app_preview_set: self._set_fields('appPreviewSets',app_preview_set if type(app_preview_set) is list else [app_preview_set])
        if app_preview: self._set_fields('appPreviews',app_preview if type(app_preview) is list else [app_preview])
        return self
        
    class Include(StringEnum):
        APP_PREVIEWS = 'appPreviews'
        APP_STORE_VERSION_LOCALIZATION = 'appStoreVersionLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> AppPreviewSetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_previews: int=None) -> AppPreviewSetEndpoint:
        '''Number of included related resources to return.

        :param app_previews: maximum number of related appPreviews returned (when they are included). The maximum limit is 50
        :type app_previews: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetEndpoint
        '''
        if app_previews and app_previews > 50:
            raise ValueError(f'The maximum limit is 50')
        if app_previews: self._set_limit('appPreviews', app_previews)

        return self

    def get(self) -> AppPreviewSetResponse:
        '''Get the resource.

        :returns: Single AppPreviewSet
        :rtype: AppPreviewSetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPreviewSetResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppPreviewsLinkagesOfAppPreviewSetEndpoint(IDEndpoint):
    path = '/v1/appPreviewSets/{id}/relationships/appPreviews'

    def limit(self, number: int=None) -> AppPreviewsLinkagesOfAppPreviewSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewsLinkagesOfAppPreviewSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> AppPreviewSetAppPreviewsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppPreviewSetAppPreviewsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPreviewSetAppPreviewsLinkagesResponse.parse_obj(json)

    def update(self, request: AppPreviewSetAppPreviewsLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: AppPreviewSetAppPreviewsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class AppPreviewsOfAppPreviewSetEndpoint(IDEndpoint):
    path = '/v1/appPreviewSets/{id}/appPreviews'

    def fields(self, *, app_preview: Union[AppPreviewField, list[AppPreviewField]]=None) -> AppPreviewsOfAppPreviewSetEndpoint:
        '''Fields to return for included related types.

        :param app_preview: the fields to include for returned resources of type appPreviews
        :type app_preview: Union[AppPreviewField, list[AppPreviewField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewsOfAppPreviewSetEndpoint
        '''
        if app_preview: self._set_fields('appPreviews',app_preview if type(app_preview) is list else [app_preview])
        return self
        
    def limit(self, number: int=None) -> AppPreviewsOfAppPreviewSetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewsOfAppPreviewSetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of default-limit is 200')
        if number: self._set_limit('default-limit', number)
        
        return self

    def get(self) -> AppPreviewsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppPreviewsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPreviewsResponse.parse_obj(json)

