import os
import sys
import pytest
from ms_sdk import Client
from ms_sdk.Entities.Product import Product
from ms_sdk.Lib.Specifications.Basic.IsVisible import IsVisible
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

    def testGetFilter(self):
        products = setup_client().products().filter({
            'title' : {FilterOperators.LIKE : 'test'}
        })

        assert Filter(filters = {'title' : {FilterOperators.LIKE : 'test'}}).getFilters() == products.getFilter()

    def testMultipleFilter(self):
        products = setup_client().products()

        product = products.get(self.entryId)
        titleLike = product.title[2:5]

        productTest = products.filter({
            'title' : {FilterOperators.LIKE : titleLike},
            'price' : {FilterOperators.GREATER_THAN_OR_EQUAL : 100}
        }).limit(1).all()

        assert titleLike in productTest.title

    def testFilterSpecification(self):
        products = setup_client().products()

        productTest = products.filter(IsVisible()).limit(1).all()

        assert str(1) == productTest.visible

    def testFilterLike(self):
        products = setup_client().products()

        product = products.get(self.entryId)
        titleLike = product.title[2:5]

        productTest = products\
            .filter({'title' : {FilterOperators.LIKE : titleLike}})\
            .limit(1)\
            .all()

        assert titleLike in productTest.title

    def testFilterLikeLeft(self):
        products = setup_client().products()

        product = products.get(self.entryId)
        titleLike = product.title[2: len(product.title)]

        productTest = products\
            .filter({'title': {FilterOperators.LIKE_LEFT : titleLike}})\
            .limit(1)\
            .all()

        assert titleLike in productTest.title


    def testFilterLikeRight(self):
        products = setup_client().products()

        product = products.get(self.entryId)
        titleLike = product.title[0:5]

        productTest = products \
            .filter({'title': {FilterOperators.LIKE_RIGHT : titleLike}}) \
            .limit(1) \
            .all()

        assert titleLike in productTest.title

    def testFilterEqual(self):
        products = setup_client().products()

        product = products.get(self.entryId)
        titleLike = product.title

        productTest = products \
            .filter({'title': {FilterOperators.EQUAL : titleLike}}) \
            .limit(1) \
            .all()

        assert titleLike == productTest.title

    def testFilterNotEqual(self):
        products = setup_client().products()

        titleLike = 'test'

        productTest = products \
            .filter({'title': {FilterOperators.NOT_EQUAL : titleLike}}) \
            .limit(1) \
            .all()

        assert titleLike != productTest.title

    def testFilterGreaterThan(self):
        products = setup_client().products()

        productTest = products \
            .filter({'price': {FilterOperators.GREATER_THAN : 60000}}) \
            .limit(1) \
            .all()

        assert int(productTest.price) > 60000

    def testFilterLessThan(self):
        products = setup_client().products()

        productTest = products \
            .filter({'price': {FilterOperators.LESS_THAN : 60000}}) \
            .limit(1) \
            .all()

        assert int(productTest.price) < 60000

    def testFilterGreaterOrEqualThan(self):
        products = setup_client().products()

        productTest = products \
            .filter({'price': {FilterOperators.GREATER_THAN_OR_EQUAL : 60000}}) \
            .limit(1) \
            .all()


        assert int(productTest.price) >= 60000

    def testFilterLessOrEqualThan(self):
        products = setup_client().products()

        productTest = products \
            .filter({'price': {FilterOperators.LESS_THAN_OR_EQUAL : 60000}}) \
            .limit(1) \
            .all()

        assert int(productTest.price) <= 60000

    def testIn(self):
        products = setup_client().products()
        productsList = products.limit(2).all()

        productsTest = products.setIn('title', [productsList[0].title, productsList[1].title]).all()

        assert len(productsTest) == 2

        assert productsList[0].title == productsTest[0].title
        assert productsList[1].title == productsTest[1].title

    def testSort(self):
        products1 = setup_client().products()
        productList1 = products1.limit(2).sort('title').all()
        assert ['title'] == products1.getSort()

    def testCount(self):
        products1 = setup_client().products()
        productCount = products1.filter({'price' : {FilterOperators.GREATER_THAN_OR_EQUAL : 60000}})\
            .sort('title')\
            .count()

        productList = products1.filter({'price' : {FilterOperators.GREATER_THAN_OR_EQUAL : 60000}})\
            .sort('title')\
            .all()

        assert productCount == len(productList)

    def testCollectionAsArray(self):
        products1 = setup_client().products();
        products = products1.limit(2).all()
        assert type(products) == list

    # def testFilterIsNull(self):
    #     products = setup_client().products()
    #
    #     productTest = products \
    #         .filter({'titleMask': {FilterOperators.IS_NULL : None }}) \
    #         .limit(1) \
    #         .all()
    #
    #     products._filter = {}
    #
    #     assert not productTest.titleMask
    #


















