from ms_sdk.Entities.Vat import Vat
from tests.settings import setup_client


class TestVatsResource:

    def test_get_list(self):
        listAll = setup_client().vats().all()

        for item in listAll:
            isinstance(type(item), Vat)
