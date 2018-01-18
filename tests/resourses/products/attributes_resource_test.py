import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from tests.settings import setup_client
from ms_sdk.Lib.Entity import Entity


class TestAttributesResource:
    def testServiceGetList(self):
        attributes = setup_client().attributes()
        attrList = attributes.all()

        for item in attrList:
            isinstance(type(item), Entity)

    def testAttributesBelongEntityAttributeGroupAttribute(self):
        attributes = setup_client().attributes()
        attrList = attributes.belong('product', 2, 1)

        for item in attrList:
            isinstance(type(item), Entity)

    def testAttributesBelongEntityAttributeGroup(self):
        attributes = setup_client().attributes()
        attrList = attributes.belong('product', 2)

        for item in attrList:
            isinstance(type(item), Entity)

    def testAttributesBelongEntity(self):
        attributes = setup_client().attributes()
        attrList = attributes.belong('product')

        for item in attrList:
            isinstance(type(item), Entity)


    def testAttributeHelpMethods(self):
        products = setup_client().products().limit(1).full()
        attributes = products[0].attributes
        products(attributes)