from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppCategoriesEndpoint(Endpoint):
    path = '/v1/appCategories'

    def fields(self, *, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> AppCategoriesEndpoint:
        '''Fields to return for included related types.

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCategoriesEndpoint
        '''
        if app_category: self._set_fields('appCategories',app_category if type(app_category) is list else [app_category])
        return self
        
    class Include(StringEnum):
        PARENT = 'parent'
        SUBCATEGORIES = 'subcategories'

    def exists(self, *, parent: bool=None) -> AppCategoriesEndpoint:
        ''' Filter by existence or non-existence of related resource.
        
        :returns: self
        :rtype: applaud.endpoints.AppCategoriesEndpoint
        '''
        if parent == None:
            return
        
        self._set_exists('parent', 'true' if parent  else 'false')
        return self
        
    def filter(self, *, platforms: Union[Platform, list[Platform]]=None) -> AppCategoriesEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platforms: filter by attribute 'platforms'
        :type platforms: Union[Platform, list[Platform]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCategoriesEndpoint
        '''
        if platforms: self._set_filter('platforms', platforms if type(platforms) is list else [platforms])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppCategoriesEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppCategoriesEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, subcategories: int=None) -> AppCategoriesEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param subcategories: maximum number of related subcategories returned (when they are included). The maximum limit is 50
        :type subcategories: int = None

        :returns: self
        :rtype: applaud.endpoints.AppCategoriesEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if subcategories and subcategories > 50:
            raise ValueError(f'The maximum limit of subcategories is 50')
        if subcategories: self._set_limit(subcategories, 'subcategories')

        return self

    def get(self) -> AppCategoriesResponse:
        '''Get one or more resources.

        :returns: List of AppCategories
        :rtype: AppCategoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCategoriesResponse.parse_obj(json)

class AppCategoryEndpoint(IDEndpoint):
    path = '/v1/appCategories/{id}'

    @endpoint('/v1/appCategories/{id}/parent')
    def parent(self) -> ParentOfAppCategoryEndpoint:
        return ParentOfAppCategoryEndpoint(self.id, self.session)
        
    @endpoint('/v1/appCategories/{id}/subcategories')
    def subcategories(self) -> SubcategoriesOfAppCategoryEndpoint:
        return SubcategoriesOfAppCategoryEndpoint(self.id, self.session)
        
    def fields(self, *, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> AppCategoryEndpoint:
        '''Fields to return for included related types.

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCategoryEndpoint
        '''
        if app_category: self._set_fields('appCategories',app_category if type(app_category) is list else [app_category])
        return self
        
    class Include(StringEnum):
        PARENT = 'parent'
        SUBCATEGORIES = 'subcategories'

    def include(self, relationship: Union[Include, list[Include]]) -> AppCategoryEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppCategoryEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, subcategories: int=None) -> AppCategoryEndpoint:
        '''Number of included related resources to return.

        :param subcategories: maximum number of related subcategories returned (when they are included). The maximum limit is 50
        :type subcategories: int = None

        :returns: self
        :rtype: applaud.endpoints.AppCategoryEndpoint
        '''
        if subcategories and subcategories > 50:
            raise ValueError(f'The maximum limit of subcategories is 50')
        if subcategories: self._set_limit(subcategories, 'subcategories')

        return self

    def get(self) -> AppCategoryResponse:
        '''Get the resource.

        :returns: Single AppCategory
        :rtype: AppCategoryResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCategoryResponse.parse_obj(json)

class ParentOfAppCategoryEndpoint(IDEndpoint):
    path = '/v1/appCategories/{id}/parent'

    def fields(self, *, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> ParentOfAppCategoryEndpoint:
        '''Fields to return for included related types.

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.ParentOfAppCategoryEndpoint
        '''
        if app_category: self._set_fields('appCategories',app_category if type(app_category) is list else [app_category])
        return self
        
    def get(self) -> AppCategoryResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AppCategoryResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCategoryResponse.parse_obj(json)

class SubcategoriesOfAppCategoryEndpoint(IDEndpoint):
    path = '/v1/appCategories/{id}/subcategories'

    def fields(self, *, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> SubcategoriesOfAppCategoryEndpoint:
        '''Fields to return for included related types.

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubcategoriesOfAppCategoryEndpoint
        '''
        if app_category: self._set_fields('appCategories',app_category if type(app_category) is list else [app_category])
        return self
        
    def limit(self, number: int=None) -> SubcategoriesOfAppCategoryEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SubcategoriesOfAppCategoryEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppCategoriesResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppCategoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCategoriesResponse.parse_obj(json)

