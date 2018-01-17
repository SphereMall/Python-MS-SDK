import os
import sys
import unittest
from ms_sdk import Client
from tests.settings import *

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class BaseResourseTest:
    entryId = None

    def testSetUp(self):
        client = setUp()

        products = client.products()
        product = products.limit(10).all()
        self.entryId = product[9].id

    def testGetList(self):
        client = setUp()
        products = client.products().all()
        # print(products[0].title)
        self.assertEqual(10, len(products))

    def testGetSingle(self):
        client = setUp()
        product = client.products().get(self.entryId)
        # print(len(product))
        # self.assertEqual(self.entryId, product.id)

if __name__ == '__main__':
    unittest.main()


def setUp():
    return Client({
        'gatewayUrl': API_GATEWAY_URL,
        'clientId': API_CLIENT_ID,
        'secretKey': API_SECRET_KEY,
        'version': API_VERSION,
    })
