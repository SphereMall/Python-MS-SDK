from ms_sdk.Entities.PaymentProvider import PaymentProvider
from tests.settings import setup_client


class TestPaymentProvidersResource:

    def test_get_list(self):
        listAll = setup_client().paymentProviders().all()

        try:
            for item in listAll:
                isinstance(type(item), PaymentProvider)
        except:
            isinstance(type(listAll), PaymentProvider)