import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from tests.settings import setup_client
from ms_sdk.Entities.AttributeValue import AttributeValue


class TestAttributeValuesResource:
    def testServiceGetList(self):
        attributeValues = setup_client().attributeValues()
        attrList = attributeValues.all()

        for item in attrList:
            isinstance(type(item), AttributeValue)