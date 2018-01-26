import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from tests.settings import setup_client
from ms_sdk.Entities.AttributeType import AttributeType


class TestAttributeTypesResource:
    def testServiceGetList(self):
        attributeDisplayTypes = setup_client().attributeTypes()
        attrList = attributeDisplayTypes.all()

        for item in attrList:
            isinstance(type(item), AttributeType)
