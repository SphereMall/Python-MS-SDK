from ms_sdk.Entities.DeliveryProvider import DeliveryProvider
from tests.settings import setup_client


class TestDeliveryResource:

    def test_get_list(self):
        deliveryProviders = setup_client().deliveryProviders().all()
        isinstance(type(deliveryProviders[0]), DeliveryProvider)
