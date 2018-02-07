from tests.settings import setup_client
from ms_sdk.Entities.SMEntity import SMEntity


class TestEntitiesResource:

    def test_service_get_list(self):
        entities = setup_client().entities()

        for item in entities.all():
            isinstance(type(item), SMEntity)
