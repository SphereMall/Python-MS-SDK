import os
import sys

from ms_sdk.Entities.Entity import Entity

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from tests.settings import setup_client



class TestAttributeGroupsResource:
    def testServiceGetList(self):
        attributeDisplayTypes = setup_client().attributeGroups()
        attrList = attributeDisplayTypes.all()
        isinstance(type(attrList[0]), Entity)
