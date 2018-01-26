import os
import sys
import pytest
from ms_sdk import Client
from ms_sdk.Entities.Product import Product
from tests.settings import *
from ms_sdk.Lib.Filters.FilterOperators import FilterOperators
from ms_sdk.Lib.Filters.Filter import Filter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class TestBaseResourse:
    entryId = '6363'

    def testGetList(self):
        products = setup_client().products()
        productsList = products.all()

        assert 10 == len(productsList)

        for product in productsList:
            isinstance(type(product), Product)

    def testGetSingle(self):
        products = setup_client().products()
        product = products.get(self.entryId)
        assert self.entryId == product.id

    def testGetFirst(self):
        products = setup_client().products()
        product = products.first()

        isinstance(type(product), Product)

    def testLimitOffsetAndAmountOfCalls(self):
        client = setup_client()
        products = client.products()

        productList = products.limit(3, 0).all()
        assert 3 == len(productList)
        assert 3 == products.getLimit()
        assert 0 == products.getOffset()

        productList = products.limit(5, 0).all()
        assert 5 == len(productList)
        assert 5 == products.getLimit()
        assert 0 == products.getOffset()

        productListOffset1 = products.limit(2, 0).all()
        assert 2 == products.getLimit()
        assert 0 == products.getOffset()

        productListOffset2 = products.limit(1, 1).all()
        assert 1 == products.getLimit()
        assert 1 == products.getOffset()

        assert productListOffset2.id == productListOffset1[1].id

        stat = client.getCallsStatistic()
        assert 4 == stat['amount']

    def testSetIds(self):
        products = setup_client().products().ids([1, 2, 4])
        assert [1, 2, 4] == products.getIds()

    def testFields(self):
        products1 = setup_client().products()

        product = products1.fields(['id', 'title']).get(6329)
        assert product.id is not None
        assert product.title is not None
        assert product.price is None

        assert ['id', 'title'] == products1.getFields()

        product2 = products1.fields(['id', 'price']).get(6329)
        assert product2.id is not None
        assert product2.title is None
        assert product2.price is not None

        assert ['id', 'price'] == products1.getFields()

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
