import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from tests.settings import setup_client
from ms_sdk.Entities.MediaType import MediaType


class TestMediaResource:

    def testServiceGetList(self):
        media = setup_client().mediaTypes()

        for item in media.all():
            isinstance(type(item), MediaType)