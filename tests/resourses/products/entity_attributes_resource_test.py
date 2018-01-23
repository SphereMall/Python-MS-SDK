import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from tests.settings import setup_client
from ms_sdk.Entities.EntityAttribute import EntityAttribute
from ms_sdk.Resourses.Products.EntityAttributesResource import EntityAttributesResource

class TestEntityAttributesResource:

    def testServiceGetList(self):
        entityAttributes = setup_client().entities()
        isinstance(type(entityAttributes), EntityAttributesResource)

        for item in entityAttributes.all():
            isinstance(type(item), EntityAttribute)