import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from tests.settings import setup_client
from ms_sdk.Entities.Product import Product
from ms_sdk.Lib.Collection import Collection

class TestProductsResource:

    def testServiceGetList(self):
        products = setup_client().products()
        productArray = products.all()
        productList = Collection(productArray)

        assert 10 == productList.count()

        ids = productList.current().id
        productArray = products.ids(ids).all()
        productList = Collection(productArray)

        # assert 1 == productList.count()
        # assert ids == products.getIds()

        # for product in productList:
        #     isinstance(type(product), Product)