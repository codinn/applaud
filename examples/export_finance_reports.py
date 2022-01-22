import os
from applaud.endpoints.finance_reports import FinanceReportsEndpoint
from applaud.connection import Connection

KEY_ID = "XXXXXXXXXX"
ISSUER_ID = "XXXXXX-XXXXXXX-XXXXXX-XXXXXXX"
PATH_TO_KEY = os.path.expanduser('path/to/your/key.p8')
# You can find your vendor number here [Payments and Financial Reports](https://help.apple.com/app-store-connect/#/dev3a16f3fe0)
VENDOR_NUMBER = 'XXXXXXXX'

with open(PATH_TO_KEY, 'r') as f:
    PRIVATE_KEY = f.read()

# Create the Connection
connection = Connection(ISSUER_ID, KEY_ID, PRIVATE_KEY)

r = connection.finance_reports().filter(
    report_type=FinanceReportsEndpoint.ReportType.FINANCE_DETAIL, # or 'FINANCE_DETAIL'
    region_code='Z1',
    report_date='2021-12',
    vendor_number=VENDOR_NUMBER
).get()

r.save('finance_reports.txt', decompress=True)
