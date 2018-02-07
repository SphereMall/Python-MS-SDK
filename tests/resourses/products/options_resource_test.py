from tests.settings import setup_client
from ms_sdk.Entities.Option import Option


class TestOptionsResource:

    def test_service_get_list(self):
        entities = setup_client().options()

        for item in entities.all():
            isinstance(type(item), Option)
