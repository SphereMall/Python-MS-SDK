import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from ms_sdk.Resourses import Resource
from ms_sdk.Resourses.Products import ProductsResource


import unittest
from ms_sdk import Client
from tests.settings import *
from tests.Resourses.BaseResourceTest import BaseResourseTest



class ClientTest(unittest.TestCase, BaseResourseTest):

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

        # self.assertIsInstance(productService, Resource)
        self.assertIsInstance(product_service, ProductsResource)

    def testSetVersion(self):
        client = Client({
            'gatewayUrl': API_GATEWAY_URL,
            'clientId': API_CLIENT_ID,
            'secretKey': API_SECRET_KEY,
            'version': 'testV',
        })

        self.assertEqual('testV', client.getVersion())

        client.setVersion('newV')
        self.assertEqual('newV', client.getVersion())


if __name__ == '__main__':
    unittest.main()
