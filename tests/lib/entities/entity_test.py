import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from ms_sdk.Entities.Attribute import Attribute
from ms_sdk.Entities.Entity import Entity
from ms_sdk.Entities.Product import Product
from tests.settings import *


class TestEntity:
    def test_create_object(self):
        entity = Entity
        isinstance(type(entity), Entity)

    #
    # def testGetEntityType(self):
    #     product = Product
    #     print(product.getType(self))
    #     assert 'product' == product.getType(self)
    #     isinstance(type(product), Product)
    #
    #     attribute = Attribute
    #     assert 'attribute' == attribute.getType(self)
    #     isinstance(type(product), Attribute)
