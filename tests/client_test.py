import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from ms_sdk.Resourses import Resource
from ms_sdk.Resourses.Products import ProductsResource
import pytest
from ms_sdk import Client
from tests.settings import *


class TestClient:

    def testClientObjectCreatedNotConfigured(self):
        client = Client()

    def testClientObjectCreatedWithConfiguration(self):
        client = Client({
            'gatewayUrl': API_GATEWAY_URL,
            'clientId': API_CLIENT_ID,
            'secretKey': API_SECRET_KEY,
            'version': API_VERSION,
        })

    def testClientCallService(self):
        client = Client({
            'gatewayUrl': API_GATEWAY_URL,
            'clientId': API_CLIENT_ID,
            'secretKey': API_SECRET_KEY,
            'version': API_VERSION,
        })

        product_service = client.products()
        isinstance(product_service, ProductsResource)

    def testSetVersion(self):
        client = Client({
            'gatewayUrl': API_GATEWAY_URL,
            'clientId': API_CLIENT_ID,
            'secretKey': API_SECRET_KEY,
            'version': 'testV',
        })

        assert 'testV' == client.getVersion()
        client.setVersion('newV')
        assert 'newV' == client.getVersion()


# if __name__ == '__main__':
#     unittest.main()
