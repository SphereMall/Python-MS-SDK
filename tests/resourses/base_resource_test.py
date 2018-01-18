import os
import sys
import pytest
from ms_sdk import Client
from tests.settings import *
from ms_sdk.Lib.Filters.FilterOperators import FilterOperators
from ms_sdk.Lib.Filters.Filter import Filter
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

class TestBaseResourse:

    entryId = '6363'

    def testGetList(self):
        products = setup_client().products().all()
        assert 10 == len(products)

    def testGetSingle(self):
        product = setup_client().products().get(self.entryId)
        assert self.entryId == product.id

    def testGetFirst(self):
        product = setup_client().products().first()

    # def testGetFilter(self):
    #     products = self.setup_client.products().filter({
    #     'title':{FilterOperators.LIKE : 'test'} })
    #
    #     assert products._filter == Filter({'title':{FilterOperators.LIKE : 'test'} })

    # def testMultipleFilter(self):
    #     products = self.setup_client.products()
    #
    #     product = products.get(self.entryId)
    #     titleLike = product.title[2:5]
    #
    #     productTest = products.filter({
    #         'title' : {FilterOperators.LIKE : titleLike},
    #         'price' : {FilterOperators.GREATER_THAN_OR_EQUAL : 100}
    #     }).limit(1).all()
    #
    #     print(productTest)
        # assert titleLike in productTest[0].title
