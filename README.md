# SphereMall Gateway Python SDK
Official Python SDK for integrating with **SphereMall Product**.
[Official documentation](https://spheremall.atlassian.net/wiki/spaces/MIC/pages)

### Version 0.5
[Changelog 1.0.26](https://github.com/SphereMall/PHP-MS-Client/wiki/0.-SDK-Changelogs#version-1016)
#### Supported microservices
* Gateway 1.1.1
* Products 1.1.0
* Users 1.0.0
* Grapher 1.0.0

## Installation
**Step 1**. Create virtual environment:
```
python3 -m venv myvenv
myvenv\Scripts\activate
```

**Step 2**: Install Python-MS-SDK
```
pip3 install Python-MS-SDK
```

**Step: 3**: Import the package
```python
from ms_sdk import Client
```
## Instantiating the SDK Client:

Pass in the configuration to the client:

```python
client = Client({
            'gatewayUrl': 'API_GATEWAY_URL',
            'clientId': 'API_CLIENT_ID',
            'secretKey': 'API_SECRET_KEY'
        })
```

## Using the client with base Resources functionality
* [Multiple Resources](https://github.com/SphereMall/PHP-MS-Client/wiki/1.-Multiple-Resources)
* [Single Resource by ID](https://github.com/SphereMall/PHP-MS-Client/wiki/2.-Single-Resource-by-ID)
* [Limiting and Offsetting Results](https://github.com/SphereMall/PHP-MS-Client/wiki/3.-Limiting-and-Offsetting-Results)
* [Filtering result with specific fields](https://github.com/SphereMall/PHP-MS-Client/wiki/4.-Filtering-result-with-specific-fields)
* [Sorting Results](https://github.com/SphereMall/PHP-MS-Client/wiki/5.-Sorting-Results)
* [Counting Results](https://github.com/SphereMall/PHP-MS-Client/wiki/6.-Counting-Results)
* [Product Resource](https://github.com/SphereMall/PHP-MS-Client/wiki/7.-Product-Resource)
  * [Get full](https://github.com/SphereMall/PHP-MS-Client/wiki/7.1.-Get-full)
