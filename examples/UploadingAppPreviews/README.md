# Uploading App Previews with `applaud`

The original sample code is here [Uploading App Previews](https://developer.apple.com/documentation/appstoreconnectapi/app_metadata/uploading_app_previews).

This project rewrite the sample code with [applaud python library](https://github.com/codinn/applaud).

Upload your app previews, including video files, to App Store Connect by using the asset upload APIs.

## Overview

 This sample code includes a script written in Python that uploads a video as an app preview for an app. To run this sample, you must have an app in App Store Connect with a version in the "Prepare for Submission" state, and an app preview file to upload. You'll also need your API key.

 The sample's script first generates an authentication token, so it can call the App Store Connect API. It then creates an app preview set or uses an existing one, if one exists. The script then reserves a new app preview associated with the app preview set, uploads the binary data, and commits the upload.

For more information about the process of uploading assets, see [Uploading Assets to App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi/uploading_assets_to_app_store_connect).

## Configure the Sample Code Project

This project requires Python 3.9, on macOS you can install it with [Homebrew](https://brew.sh/):
```
brew install python
```

The project uses [Python Poetry](https://python-poetry.org/) dependency management system, which you need to install, follow [this guide](https://python-poetry.org/docs/#installation) to install `poetry`.

Follow these steps to install the required Python modules:

1. In Terminal, navigate to the folder that contains this sample project:
    ```
    cd UploadingAppPreviews
    ```

4. Install the Python modules by entering:
   ```
   ~/Library/Python/3.9/bin/poetry install
   ```

   If you've installed your own version of Python, the `poetry` path may be different.

## Add the API Key to the Script and Prepare the Upload

Prepare to run the script by following these steps:

1. Copy `credentials.toml.template` file to `credentials.toml`, add your API Key information to the `[appstore]` section of the file. To find your API key, log in to App Store Connect and open the [Users & Access](https://appstoreconnect.apple.com/access/api) module. The key is found in the Keys tab. For more information, see [Creating API Keys for App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api).

2. Make sure the video file you'd like to upload is available on your local machine. For more information about app previews, including technical specifications, see
   [Show More with App Previews](https://developer.apple.com/app-store/app-previews/).

3. Your app must be in App Store Connect with a version in the "Prepare for Submission" state. To upload the app preview, you'll need the `bundle id`, `platform`, `version number`, and `locale` of this app.

## Provide Command-Line Parameters to Run the Script

On the command line, run this command, replacing the parameters with actual values:

```python
~/Library/Python/3.9/bin/poetry run python3 upload-preview.py {bundle id} {platform} {version} {locale} {preview type} {path to video file}
```
The command-line parameters are:  
* `{bundle id}`—Your app's bundle ID.  
* `{platform}`—Your app's platform. See [Platform](https://developer.apple.com/documentation/appstoreconnectapi/platform) for valid values.  
* `{version}`—The version of your app to which the preview applies.  
* `{locale}`—The locale to which the preview applies. See [Create an App Info Localization](https://developer.apple.com/documentation/appstoreconnectapi/create_an_app_info_localization) for valid values.  
* `{preview type}`—The type of preview. See [Preview Types](https://developer.apple.com/documentation/appstoreconnectapi/previewtype) for valid values.  
* `{path to video file}`—The path to the video file on your computer.  


The following example replaces `{bundle id}` with `com.mycompany.MyApp`; `{platform}` with `IOS`; `{version}` with `1.0`; `{locale}` with `en-US`;  `{preview type}` with `IPHONE_65`; and `{path to video file}` with`../my-video.mp4`.

```python
~/Library/Python/3.9/bin/poetry run python3 upload-preview.py com.mycompany.MyApp IOS 1.0 en-US IPHONE_65 ../my-video.mp4
```


## Generate an Authentication Token

First, the script creates a `Connection` object to contact with App Store Connect service. You pass Issuer ID, Key ID and private key to initialize a `Connection` object:

```python
connection = Connection(ISSUER_ID, KEY_ID, PRIVATE_KEY)
```

## Find or Create the App Preview Set

The App Store Connect API requires the addition of an app preview to an *app preview set*. Create one app preview set for each preview type and each locale. Each set includes up to three previews. For example, a set might have a 6.5 inch iPhone in the US English locale, and another in the Mexican Spanish locale.

Before the sample creates the app preview, it needs to find the right preview set or create a new set. The script first searches for the app by bundle ID.

```python
apps_response = connection.apps().filter(bundle_id=bundle_id).get()
```

Then, the script searches for the version by platform and version number:

```python
versions_response = connection.app(app.id).app_store_versions().filter(
    platform=platform,
    version_string=version
).get()
```

If the version doesn't have a localization for the given locale, the script creates a new one:

```python
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
```

Finally, if the localization doesn't have an app preview set of the given type, the script creates one:

```python
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
```

## Reserve an App Preview

Once the sample project finds or creates the app preview set, it reserves a new app preview associated with the app preview set ID. The reservation tells App Store Connect the name and size of the file the script intends to upload.

```python
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
```

## Upload the Binary Data

In response to the reservation request, App Store Connect responds with a set of upload
operations. Use the upload operations to upload a file, potentially in multiple parts. The sample uses the `offset` and `length` in the upload operation to extract a portion of the source file.

```python
with open(filePath, mode='rb') as file:
    file.seek(upload_operation['offset'])
    bytes = file.read(upload_operation['length'])
```

The `method`, `url` and `requestHeaders` in the upload operation are used for uploading the chunk of data.

```python
requests.request(
    method=upload_operation.method,
    url=upload_operation.url,
    headers={h.name: h.value for h in upload_operation.request_headers},
    data=data
)
```

## Commit the App Preview

Once all the parts of the file are uploaded, the sample code then demonstrates how to commit the app preview by marking it uploaded and providing an MD5 checksum of the original source file.

```python
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
```

## Verify the App Preview

App Store Connect processes the asset asynchronously. Check the upload's status in App
Store Connect or by re-requesting the `/v1/appPreview/{id}` and examining the response.
