from ms_sdk.Entities.Currency import Currency
from tests.settings import setup_client


class TestCurrenciesResource:

    def test_get_list(self):
        listAll = setup_client().currencies().all()

        for item in listAll:
            isinstance(type(item), Currency)
