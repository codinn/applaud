"""
A Python script that uploads an app preview to App Store Connect using `applaud` library.
See README.md for help configuring and running this script.
"""

import hashlib
import os
import sys
from pathlib import PurePath
from urllib.parse import urlparse
import tomlkit
import requests

from applaud.connection import Connection
from applaud.schemas.requests import *
from applaud.schemas.responses import AppPreviewSetsResponse

def enable_logging():
    import logging
    import http.client
    
    # Enable logging
    log = logging.getLogger('urllib3')
    log.setLevel(logging.DEBUG)

    # logging from urllib3 to console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    log.addHandler(ch)

    # print statements from `http.client.HTTPConnection` to console/stdout
    http.client.HTTPConnection.debuglevel = 1

# Uncomment next line to enable HTTP logging
# enable_logging()

########
# KEY CONFIGURATION - Put your API Key info to 'credentials.toml'.

_credentials_file = PurePath(__file__).parent / 'credentials.toml'
_credentials = tomlkit.loads(open(_credentials_file).read())

KEY_ID = _credentials['appstore']['key_id']
PRIVATE_KEY_FILE = os.path.expanduser(_credentials['appstore']['key_file'])
ISSUER_ID = _credentials['appstore']['issuer_id']
PRIVATE_KEY = open(PRIVATE_KEY_FILE, 'r').read()

########
# UPLOAD - This is where the interaction with App Store Connect API happens.
def upload(bundle_id, platform, version, locale, preview_type, file_path):
    """
    This function does all the real work. It:
    1. Create an Applaud Connection object.
    2. Looks up the app by bundle id.
    3. Looks up the version by platform and version number.
    4. Gets all localizations for the version and looks for the requested locale.
    5. Creates the localization if the requested localization doesn't exist.
    6. Gets all available app preview sets from the localization.
    7. Creates the app preview set for the requested type if it doesn't exist.
    8. Reserves an app preview in the selected app preview set.
    9. Uploads each part according to the returned upload operations.
    10. Commits the reservation and provides a checksum.

    If anything goes wrong during this process the error is reported and the
    script exits with a non-zero status.
    """

    # 1. Create an Applaud Connection object.
    connection = Connection(ISSUER_ID, KEY_ID, PRIVATE_KEY)

    print("Find (or create) app preview set.")

    # 2. Look up the app by bundle id.
    #    If the app is not found, report an error and exit.
    apps_response = connection.apps().filter(bundle_id=bundle_id).get()
    apps = apps_response.data
    if apps:
        app = apps[0]
    else:
        die(1, f"No app found with bundle id {bundle_id}.")


    # 3. Look up the version version by platform and version number.
    #    If the version is not found, report an error and exit.
    versions_response = connection.app(app.id).app_store_versions().filter(
            platform=platform,
            version_string=version
        ).get()
    versions = versions_response.data
    if versions:
        version = versions[0]
    else:
        die(2, f"No app store version found with version {version}.")

    # 4. Get all localizations for the version and look for the requested locale.
    localizations_response = connection.app_store_version(version.id).app_store_version_localizations().get()
    localizations = localizations_response.data
    selected_localizations = [loc for loc in localizations if loc.attributes.locale == locale]


    # 5. If the requested localization does not exist, create it.
    #    Localized attributes are copied from the primary locale so there's
    #    no need to worry about them here.
    if selected_localizations:
        selected_localization = selected_localizations[0]
    else:
        request = AppStoreVersionLocalizationCreateRequest(
            data=AppStoreVersionLocalizationCreateRequest.Data(
                attributes=AppStoreVersionLocalizationCreateRequest.Data.Attributes(
                    locale=locale
                ),
                relationships=AppStoreVersionLocalizationCreateRequest.Data.Relationships(
                    app_store_version=AppStoreVersionLocalizationCreateRequest.Data.Relationships.AppStoreVersion(
                        data=AppStoreVersionLocalizationCreateRequest.Data.Relationships.AppStoreVersion.Data(
                            id=version.id,
                        )
                    )
                )
            )
        )
        selected_localization_response = connection.app_store_version_localizations().create(request)
        selected_localization = selected_localization_response.data


    # 6. Get all available app preview sets from the localization.
    #    If a preview set for the desired preview type already exists, use it.
    #    Otherwise, make a new one.
    preview_sets_response = connection.generic_endpoint(selected_localization.relationships.app_preview_sets.links.related).get(response_class=AppPreviewSetsResponse)
    preview_sets = preview_sets_response.data
    selected_preview_sets = [set for set in preview_sets
                             if set.attributes.preview_type == preview_type]


    # 7. If an app preview set for the requested type doesn't exist, create it.
    if selected_preview_sets:
        selected_preview_set = selected_preview_sets[0]
    else:
        request = AppPreviewSetCreateRequest(
            data=AppPreviewSetCreateRequest.Data(
                attributes=AppPreviewSetCreateRequest.Data.Attributes(
                    preview_type=preview_type
                ),
                relationships=AppPreviewSetCreateRequest.Data.Relationships(
                    app_store_version_localization=AppPreviewSetCreateRequest.Data.Relationships.AppStoreVersionLocalization(
                        data=AppPreviewSetCreateRequest.Data.Relationships.AppStoreVersionLocalization.Data(
                            id=selected_localization.id
                        )
                    )
                )
            )
        )
        preview_set_response = connection.app_preview_sets().create(request)
        selected_preview_set = preview_set_response.data
        

    # 8. Reserve an app preview in the selected app preview set.
    #    Tell the API to create a preview before uploading the
    #    preview data.
    print("Reserve new app preview.")
    request = AppPreviewCreateRequest(
        data=AppPreviewCreateRequest.Data(
            attributes=AppPreviewCreateRequest.Data.Attributes(
                file_name=os.path.basename(file_path),
                file_size=os.path.getsize(file_path)
            ),
            relationships=AppPreviewCreateRequest.Data.Relationships(
                app_preview_set=AppPreviewCreateRequest.Data.Relationships.AppPreviewSet(
                    data=AppPreviewCreateRequest.Data.Relationships.AppPreviewSet.Data(
                        id=selected_preview_set.id
                    )
                )
            )
        )
    )
    reserve_preview_response = connection.app_previews().create(request)
    preview = reserve_preview_response.data


    # 9. Upload each part according to the returned upload operations.
    #     The reservation returned uploadOperations, which instructs us how
    #     to split the asset into parts. Upload each part individually.
    #     Note: To speed up the process, upload multiple parts asynchronously
    #     if you have the bandwidth.
    upload_operations = preview.attributes.upload_operations

    for part_number, upload_operation in enumerate(upload_operations):
        print(f"Upload part {part_number+1} of {len(upload_operations)} at offset "
              f"{upload_operation.offset} with length {upload_operation.length}.")

        # Read the requested byte range.
        with open(file_path, mode='rb') as file:
            file.seek(upload_operation.offset)
            data = file.read(upload_operation.length)

        # Upload the data using the request info specified in the upload operation.
        requests.request(
            method=upload_operation.method,
            url=upload_operation.url,
            headers={h.name: h.value for h in upload_operation.request_headers},
            data=data
        )


    # 10. Commit the reservation and provide a checksum.
    #     Committing tells App Store Connect the script is finished uploading parts.
    #     App Store Connect uses the checksum to ensure the parts were uploaded
    #     successfully.
    print("Commit the reservation.")
    preview_url = preview.links.self
    commit_request = AppPreviewUpdateRequest(
        data=AppPreviewUpdateRequest.Data(
            id=preview.id,
            attributes=AppPreviewUpdateRequest.Data.Attributes(
                uploaded=True,
                source_file_checksum=hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            )
        )
    )
    connection.app_preview(preview.id).update(commit_request)


    # Report success to the caller.
    print()
    print("App Preview successfully uploaded to:")
    print(blue(preview_url))
    print("You can verify success in App Store Connect or using the API.")
    print()


def die(status, message):
    print(red(message), file=sys.stderr)
    sys.exit(status)

########
# TEXT COLORS - Functions to color text for pretty output.
def red(text):
    return f"\033[91m{text}\033[0m"

def green(text):
    return f"\033[92m{text}\033[0m"

def blue(text):
    return f"\033[94m{text}\033[0m"

########
# ENTRY POINT - When run directly, check arguments and call upload().
if __name__ == "__main__":
    if len(sys.argv) != 7:
        die(-1, "usage: python3 upload-preview.py {bundle id} {platform} {version} {locale} "
                "{preview type} {file path}")
    upload(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
