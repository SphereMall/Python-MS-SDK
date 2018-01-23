import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from tests.settings import setup_client
from ms_sdk.Entities.Media import Media


class TestMediaResource:

    def testServiceGetList(self):
        media = setup_client().media()


        for item in media.all():
            isinstance(type(item), Media)