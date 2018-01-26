import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from tests.settings import setup_client
from ms_sdk.Entities.Option import Option


class TestOptionsResource:

    def testServiceGetList(self):
        entities = setup_client().options()

        for item in entities.all():
            isinstance(type(item), Option)
