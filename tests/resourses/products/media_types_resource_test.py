from tests.settings import setup_client
from ms_sdk.Entities.MediaType import MediaType


class TestMediaResource:

    def test_service_get_list(self):
        media = setup_client().mediaTypes()

        for item in media.all():
            isinstance(type(item), MediaType)
