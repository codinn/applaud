import os
from applaud.connection import Connection

KEY_ID = "XXXXXXXXXX"
ISSUER_ID = "XXXXXX-XXXXXXX-XXXXXX-XXXXXXX"
PATH_TO_KEY = os.path.expanduser('path/to/your/key.p8')

with open(PATH_TO_KEY, 'r') as f:
    PRIVATE_KEY = f.read()

# Create the Connection
connection = Connection(ISSUER_ID, KEY_ID, PRIVATE_KEY)
# API Request
r = connection.users().limit(10).get()

# Print user names
for user in r.data:
    print(user.attributes.username, user.attributes.first_name, user.attributes.last_name)

# Write the response in a pretty printed JSON file
with open('output.json', 'w') as out:
    out.write(r.json(indent=4))
