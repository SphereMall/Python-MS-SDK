import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from ms_sdk.Entities.Attribute import Attribute
from ms_sdk.Entities.Product import Product
from tests.settings import *


class TestInteractsWithAttributes:

    def testGetAttributeByCode(self):
        product = self.getMockedProduct()
        assert 'second' == product.getAttributeByCode('second').code

    def testGetAttributeById(self):
        product = self.getMockedProduct()
        assert 3 == product.getAttributeById(3).id

    def testGetAttributeByIds(self):
        product = self.getMockedProduct()
        attrs = [Attribute({'id': 2, 'code': 'first'}).id,
                 Attribute({'id': 1, 'code': 'second'}).id]

        assert attrs == \
               list([product.getAttributesByIds([2, 1])[1].id, product.getAttributesByIds([2, 1])[0].id])

    def testGetAttributeByCodes(self):
        product = self.getMockedProduct()
        attrs = [Attribute({'id': 1, 'code': 'first'}).code,
                 Attribute({'id': 2, 'code': 'second'}).code]

        assert attrs == \
               list([product.getAttributesByCodes(['first', 'second'])[0].code, product.getAttributesByCodes(['first', 'second'])[1].code])

    def getMockedProduct(self):
        product = Product({'id' : 1})

        first = Attribute({'id' : 1, 'code' : 'first'})
        second =  Attribute({'id' : 2,'code' : 'second'})
        third = Attribute({'id': 3,'code': 'third'})

        product.attributes = [first, second, third]
        return product