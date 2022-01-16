from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SalesReportsEndpoint(Endpoint):
    path = '/v1/salesReports'

    class Frequency(StringEnum):
        DAILY = 'DAILY'
        WEEKLY = 'WEEKLY'
        MONTHLY = 'MONTHLY'
        YEARLY = 'YEARLY'

    class ReportSubType(StringEnum):
        SUMMARY = 'SUMMARY'
        DETAILED = 'DETAILED'

    class ReportType(StringEnum):
        SALES = 'SALES'
        PRE_ORDER = 'PRE_ORDER'
        NEWSSTAND = 'NEWSSTAND'
        SUBSCRIPTION = 'SUBSCRIPTION'
        SUBSCRIPTION_EVENT = 'SUBSCRIPTION_EVENT'
        SUBSCRIBER = 'SUBSCRIBER'

    def filter(self, *, frequency: Union[Frequency, list[Frequency]], report_date: Union[str, list[str]]=None, report_sub_type: Union[ReportSubType, list[ReportSubType]], report_type: Union[ReportType, list[ReportType]], vendor_number: Union[str, list[str]], version: Union[str, list[str]]=None) -> SalesReportsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param frequency: filter by attribute 'frequency'
        :type frequency: Union[Frequency, list[Frequency]]

        :param report_date: filter by attribute 'reportDate'
        :type report_date: Union[str, list[str]] = None

        :param report_sub_type: filter by attribute 'reportSubType'
        :type report_sub_type: Union[ReportSubType, list[ReportSubType]]

        :param report_type: filter by attribute 'reportType'
        :type report_type: Union[ReportType, list[ReportType]]

        :param vendor_number: filter by attribute 'vendorNumber'
        :type vendor_number: Union[str, list[str]]

        :param version: filter by attribute 'version'
        :type version: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.SalesReportsEndpoint
        '''
        if frequency: self._set_filter('frequency', frequency if type(frequency) is list else [frequency])
        
        if report_date: self._set_filter('reportDate', report_date if type(report_date) is list else [report_date])
        
        if report_sub_type: self._set_filter('reportSubType', report_sub_type if type(report_sub_type) is list else [report_sub_type])
        
        if report_type: self._set_filter('reportType', report_type if type(report_type) is list else [report_type])
        
        if vendor_number: self._set_filter('vendorNumber', vendor_number if type(vendor_number) is list else [vendor_number])
        
        if version: self._set_filter('version', version if type(version) is list else [version])
        
        return self
        
    def get(self) -> bytes:
        '''Get one or more resources.

        :returns: List of SalesReports
        :rtype: bytes
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return bytes.parse_obj(json)

