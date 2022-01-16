from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class FinanceReportsEndpoint(Endpoint):
    path = '/v1/financeReports'

    class ReportType(StringEnum):
        FINANCIAL = 'FINANCIAL'
        FINANCE_DETAIL = 'FINANCE_DETAIL'

    def filter(self, *, region_code: Union[str, list[str]], report_date: Union[str, list[str]], report_type: Union[ReportType, list[ReportType]], vendor_number: Union[str, list[str]]) -> FinanceReportsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param region_code: filter by attribute 'regionCode'
        :type region_code: Union[str, list[str]]

        :param report_date: filter by attribute 'reportDate'
        :type report_date: Union[str, list[str]]

        :param report_type: filter by attribute 'reportType'
        :type report_type: Union[ReportType, list[ReportType]]

        :param vendor_number: filter by attribute 'vendorNumber'
        :type vendor_number: Union[str, list[str]]

        :returns: self
        :rtype: applaud.endpoints.FinanceReportsEndpoint
        '''
        if region_code: self._set_filter('regionCode', region_code if type(region_code) is list else [region_code])
        
        if report_date: self._set_filter('reportDate', report_date if type(report_date) is list else [report_date])
        
        if report_type: self._set_filter('reportType', report_type if type(report_type) is list else [report_type])
        
        if vendor_number: self._set_filter('vendorNumber', vendor_number if type(vendor_number) is list else [vendor_number])
        
        return self
        
    def get(self) -> bytes:
        '''Get one or more resources.

        :returns: List of FinanceReports
        :rtype: bytes
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return bytes.parse_obj(json)

