import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from tests.settings import setup_client
from ms_sdk.Lib.Entity import Entity


class TestAttributeGroupsResource:
    def testServiceGetList(self):
        attributeDisplayTypes = setup_client().attributeGroups()
        attrList = attributeDisplayTypes.all()
        isinstance(type(attrList[0]), Entity)