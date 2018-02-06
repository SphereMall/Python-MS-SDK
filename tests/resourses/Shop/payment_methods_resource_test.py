from ms_sdk.Entities.PaymentMethod import PaymentMethod
from tests.settings import setup_client


class TestPaymentMethodsResource:

    def test_get_list(self):
        listAll = setup_client().paymentMethods().all()

        try:
            for item in listAll:
                isinstance(type(item), PaymentMethod)
        except:
            isinstance(type(listAll), PaymentMethod)