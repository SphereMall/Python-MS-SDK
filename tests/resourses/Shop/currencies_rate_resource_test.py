from ms_sdk.Entities.CurrencyRate import CurrencyRate
from tests.settings import setup_client


class TestCurrenciesRateResource:

    def test_get_list(self):
        listAll = setup_client().currenciesRate().all()

        for item in listAll:
            isinstance(type(item), CurrencyRate)
