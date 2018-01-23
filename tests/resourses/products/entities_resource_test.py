import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from tests.settings import setup_client
from ms_sdk.Entities.SMEntity import SMEntity


class TestEntitiesResource:

    def testServiceGetList(self):
        entities = setup_client().entities()

        for item in entities.all():
            isinstance(type(item), SMEntity)