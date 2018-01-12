import sys, os 
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import unittest
import importlib.util

from ms_sdk import Client
from ms_sdk.Resourses.Products import ProductsResource
from ms_sdk.Resourses import Resource
from settings import *


class ClientTest(unittest.TestCase):

    def testClientObjectCreatedNotConfigured(self):
        client = Client()


    def testClientObjectCreatedWithConfiguration(self):
        client = Client({
            'gatewayUrl' : API_GATEWAY_URL,
            'clientId'   : API_CLIENT_ID,
            'secretKey'  : API_SECRET_KEY,
            'version'    : API_VERSION,
        })


    def testClientCallService(self):
        client = Client({
            'gatewayUrl' : API_GATEWAY_URL,
            'clientId'   : API_CLIENT_ID,
            'secretKey'  : API_SECRET_KEY,
            'version'    : API_VERSION,
        })

        productService = client.products()

        self.assertIsInstance(productService, type(Resource))
        self.assertIsInstance(productService, type(ProductsResource))

    def testSetVersion(self):
        client = Client({
            'gatewayUrl' : API_GATEWAY_URL,
            'clientId'   : API_CLIENT_ID,
            'secretKey'  : API_SECRET_KEY,
            'version'    : 'testV',
        })

        self.assertEqual('testV', client.getVersion())
        
        client.setVersion('newV')
        self.assertEqual('newV', client.getVersion())

    
if __name__ == '__main__':
    unittest.main()