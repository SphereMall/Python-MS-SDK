from ms_sdk import Client


API_GATEWAY_URL = 'http://gateway-main.alpha.spheremall.net:8082'
API_CLIENT_ID = 'demo_pass'
API_SECRET_KEY = 'api_demo_user'
API_VERSION = 'v1'

def setup_client():
    return Client({
        'gatewayUrl': API_GATEWAY_URL,
        'clientId': API_CLIENT_ID,
        'secretKey': API_SECRET_KEY,
        'version': API_VERSION,
    })