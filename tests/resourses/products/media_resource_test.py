from tests.settings import setup_client
from ms_sdk.Entities.Media import Media


class TestMediaResource:

    def test_service_get_list(self):
        media = setup_client().media()

        for item in media.all():
            isinstance(type(item), Media)
