from ms_sdk.Entities.Address import Address
from tests.settings import setup_client


class TestAddressesResource:

    def test_service_get_list(self):
        addresses = setup_client().companies().all()

        try:
            assert addresses[0]
            for company in addresses:
                isinstance(type(company), Address)
        except:
            isinstance(type(addresses), Address)