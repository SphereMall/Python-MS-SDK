from ms_sdk.Entities.OrderItem import OrderItem
from tests.settings import setup_client


class TestOrderItemsResource:

    def test_get_list(self):
        listAll = setup_client().orderItems().all()

        for item in listAll:
            isinstance(type(item), OrderItem)
