from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}'

    @endpoint('/v1/appInfos/{id}/ageRatingDeclaration')
    def age_rating_declaration(self) -> AgeRatingDeclarationOfAppInfoEndpoint:
        return AgeRatingDeclarationOfAppInfoEndpoint(self.id, self.session)
        
    @endpoint('/v1/appInfos/{id}/appInfoLocalizations')
    def app_info_localizations(self) -> AppInfoLocalizationsOfAppInfoEndpoint:
        return AppInfoLocalizationsOfAppInfoEndpoint(self.id, self.session)
        
    @endpoint('/v1/appInfos/{id}/primaryCategory')
    def primary_category(self) -> PrimaryCategoryOfAppInfoEndpoint:
        return PrimaryCategoryOfAppInfoEndpoint(self.id, self.session)
        
    @endpoint('/v1/appInfos/{id}/primarySubcategoryOne')
    def primary_subcategory_one(self) -> PrimarySubcategoryOneOfAppInfoEndpoint:
        return PrimarySubcategoryOneOfAppInfoEndpoint(self.id, self.session)
        
    @endpoint('/v1/appInfos/{id}/primarySubcategoryTwo')
    def primary_subcategory_two(self) -> PrimarySubcategoryTwoOfAppInfoEndpoint:
        return PrimarySubcategoryTwoOfAppInfoEndpoint(self.id, self.session)
        
    @endpoint('/v1/appInfos/{id}/secondaryCategory')
    def secondary_category(self) -> SecondaryCategoryOfAppInfoEndpoint:
        return SecondaryCategoryOfAppInfoEndpoint(self.id, self.session)
        
    @endpoint('/v1/appInfos/{id}/secondarySubcategoryOne')
    def secondary_subcategory_one(self) -> SecondarySubcategoryOneOfAppInfoEndpoint:
        return SecondarySubcategoryOneOfAppInfoEndpoint(self.id, self.session)
        
    @endpoint('/v1/appInfos/{id}/secondarySubcategoryTwo')
    def secondary_subcategory_two(self) -> SecondarySubcategoryTwoOfAppInfoEndpoint:
        return SecondarySubcategoryTwoOfAppInfoEndpoint(self.id, self.session)
        
    def fields(self, *, app_info: Union[AppInfoField, list[AppInfoField]]=None, age_rating_declaration: Union[AgeRatingDeclarationField, list[AgeRatingDeclarationField]]=None, app_info_localization: Union[AppInfoLocalizationField, list[AppInfoLocalizationField]]=None, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> AppInfoEndpoint:
        '''Fields to return for included related types.

        :param app_info: the fields to include for returned resources of type appInfos
        :type app_info: Union[AppInfoField, list[AppInfoField]] = None

        :param age_rating_declaration: the fields to include for returned resources of type ageRatingDeclarations
        :type age_rating_declaration: Union[AgeRatingDeclarationField, list[AgeRatingDeclarationField]] = None

        :param app_info_localization: the fields to include for returned resources of type appInfoLocalizations
        :type app_info_localization: Union[AppInfoLocalizationField, list[AppInfoLocalizationField]] = None

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppInfoEndpoint
        '''
        if app_info: self._set_fields('appInfos',app_info if type(app_info) is list else [app_info])
        if age_rating_declaration: self._set_fields('ageRatingDeclarations',age_rating_declaration if type(age_rating_declaration) is list else [age_rating_declaration])
        if app_info_localization: self._set_fields('appInfoLocalizations',app_info_localization if type(app_info_localization) is list else [app_info_localization])
        if app_category: self._set_fields('appCategories',app_category if type(app_category) is list else [app_category])
        return self
        
    class Include(StringEnum):
        AGE_RATING_DECLARATION = 'ageRatingDeclaration'
        APP = 'app'
        APP_INFO_LOCALIZATIONS = 'appInfoLocalizations'
        PRIMARY_CATEGORY = 'primaryCategory'
        PRIMARY_SUBCATEGORY_ONE = 'primarySubcategoryOne'
        PRIMARY_SUBCATEGORY_TWO = 'primarySubcategoryTwo'
        SECONDARY_CATEGORY = 'secondaryCategory'
        SECONDARY_SUBCATEGORY_ONE = 'secondarySubcategoryOne'
        SECONDARY_SUBCATEGORY_TWO = 'secondarySubcategoryTwo'

    def include(self, relationship: Union[Include, list[Include]]) -> AppInfoEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppInfoEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_info_localizations: int=None) -> AppInfoEndpoint:
        '''Number of included related resources to return.

        :param app_info_localizations: maximum number of related appInfoLocalizations returned (when they are included). The maximum limit is 50
        :type app_info_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppInfoEndpoint
        '''
        if app_info_localizations and app_info_localizations > 50:
            raise ValueError(f'The maximum limit of app_info_localizations is 50')
        if app_info_localizations: self._set_limit(app_info_localizations, 'appInfoLocalizations')

        return self

    def get(self) -> AppInfoResponse:
        '''Get the resource.

        :returns: Single AppInfo
        :rtype: AppInfoResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppInfoResponse.parse_obj(json)

    def update(self, request: AppInfoUpdateRequest) -> AppInfoResponse:
        '''Modify the resource.

        :param request: AppInfo representation
        :type request: AppInfoUpdateRequest

        :returns: Single AppInfo
        :rtype: AppInfoResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppInfoResponse.parse_obj(json)

class AgeRatingDeclarationOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/ageRatingDeclaration'

    def fields(self, *, age_rating_declaration: Union[AgeRatingDeclarationField, list[AgeRatingDeclarationField]]=None) -> AgeRatingDeclarationOfAppInfoEndpoint:
        '''Fields to return for included related types.

        :param age_rating_declaration: the fields to include for returned resources of type ageRatingDeclarations
        :type age_rating_declaration: Union[AgeRatingDeclarationField, list[AgeRatingDeclarationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AgeRatingDeclarationOfAppInfoEndpoint
        '''
        if age_rating_declaration: self._set_fields('ageRatingDeclarations',age_rating_declaration if type(age_rating_declaration) is list else [age_rating_declaration])
        return self
        
    def get(self) -> AgeRatingDeclarationResponse:
        '''Get the resource.

        :returns: Related resource
        :rtype: AgeRatingDeclarationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AgeRatingDeclarationResponse.parse_obj(json)

class AppInfoLocalizationsOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/appInfoLocalizations'

    def fields(self, *, app_info_localization: Union[AppInfoLocalizationField, list[AppInfoLocalizationField]]=None) -> AppInfoLocalizationsOfAppInfoEndpoint:
        '''Fields to return for included related types.

        :param app_info_localization: the fields to include for returned resources of type appInfoLocalizations
        :type app_info_localization: Union[AppInfoLocalizationField, list[AppInfoLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppInfoLocalizationsOfAppInfoEndpoint
        '''
        if app_info_localization: self._set_fields('appInfoLocalizations',app_info_localization if type(app_info_localization) is list else [app_info_localization])
        return self
        
    def filter(self, *, locale: Union[str, list[str]]=None) -> AppInfoLocalizationsOfAppInfoEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param locale: filter by attribute 'locale'
        :type locale: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppInfoLocalizationsOfAppInfoEndpoint
        '''
        if locale: self._set_filter('locale', locale if type(locale) is list else [locale])
        
        return self
        
    def limit(self, number: int=None) -> AppInfoLocalizationsOfAppInfoEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppInfoLocalizationsOfAppInfoEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppInfoLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of related resources
        :rtype: AppInfoLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppInfoLocalizationsResponse.parse_obj(json)

class PrimaryCategoryOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/primaryCategory'

    def fields(self, *, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> PrimaryCategoryOfAppInfoEndpoint:
        '''Fields to return for included related types.

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.PrimaryCategoryOfAppInfoEndpoint
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

class PrimarySubcategoryOneOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/primarySubcategoryOne'

    def fields(self, *, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> PrimarySubcategoryOneOfAppInfoEndpoint:
        '''Fields to return for included related types.

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.PrimarySubcategoryOneOfAppInfoEndpoint
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

class PrimarySubcategoryTwoOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/primarySubcategoryTwo'

    def fields(self, *, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> PrimarySubcategoryTwoOfAppInfoEndpoint:
        '''Fields to return for included related types.

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.PrimarySubcategoryTwoOfAppInfoEndpoint
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

class SecondaryCategoryOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/secondaryCategory'

    def fields(self, *, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> SecondaryCategoryOfAppInfoEndpoint:
        '''Fields to return for included related types.

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.SecondaryCategoryOfAppInfoEndpoint
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

class SecondarySubcategoryOneOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/secondarySubcategoryOne'

    def fields(self, *, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> SecondarySubcategoryOneOfAppInfoEndpoint:
        '''Fields to return for included related types.

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.SecondarySubcategoryOneOfAppInfoEndpoint
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

class SecondarySubcategoryTwoOfAppInfoEndpoint(IDEndpoint):
    path = '/v1/appInfos/{id}/secondarySubcategoryTwo'

    def fields(self, *, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> SecondarySubcategoryTwoOfAppInfoEndpoint:
        '''Fields to return for included related types.

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.SecondarySubcategoryTwoOfAppInfoEndpoint
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

