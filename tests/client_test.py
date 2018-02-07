import pytest
from tests.settings import *
from ms_sdk.Exceptions.ConfigurationException import ConfigurationException
from ms_sdk.Resourses.Products import ProductsResource


class TestClient:

    def test_client_object_created_not_configured(self):
        with pytest.raises(ConfigurationException):
            client = Client()

    def test_client_object_created_with_configuration(self):
        client = Client({
            'gatewayUrl': API_GATEWAY_URL,
            'clientId': API_CLIENT_ID,
            'secretKey': API_SECRET_KEY,
            'version': API_VERSION,
        })

    def test_client_call_service(self):
        client = Client({
            'gatewayUrl': API_GATEWAY_URL,
            'clientId': API_CLIENT_ID,
            'secretKey': API_SECRET_KEY,
            'version': API_VERSION,
        })

        product_service = client.products()
        isinstance(product_service, ProductsResource)

    def test_set_version(self):
        client = Client({
            'gatewayUrl': API_GATEWAY_URL,
            'clientId': API_CLIENT_ID,
            'secretKey': API_SECRET_KEY,
            'version': 'testV',
        })

        assert 'testV' == client.getVersion()
        client.setVersion('newV')
        assert 'newV' == client.getVersion()
