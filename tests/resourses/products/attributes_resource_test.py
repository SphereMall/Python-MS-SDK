import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from tests.settings import setup_client
from ms_sdk.Entities.Attribute import Attribute


class TestAttributesResource:
    def testServiceGetList(self):
        attributes = setup_client().attributes()
        attrList = attributes.all()

        for item in attrList:
            isinstance(type(item), Attribute)

    def testAttributesBelongEntityAttributeGroupAttribute(self):
        attributes = setup_client().attributes()
        attrList = attributes.belong('product', 2, 0)

        for item in attrList:
            isinstance(type(item), Attribute)

    def testAttributesBelongEntityAttributeGroup(self):
        attributes = setup_client().attributes()
        attrList = attributes.belong('product', 2)

        for item in attrList:
            isinstance(type(item), Attribute)

    def testAttributesBelongEntity(self):
        attributes = setup_client().attributes()
        attrList = attributes.belong('product')

        for item in attrList:
            isinstance(type(item), Attribute)

    def testAttributeHelpMethods(self):
        products = setup_client().products().limit(3).full()
        attributes = products[0].attributes

        for item in attributes:
            isinstance(type(item), Attribute)