from ms_sdk.Entities.Invoice import Invoice
from tests.settings import setup_client


class TestInvoicesResource:

    def test_get_list(self):
        listAll = setup_client().invoices().all()

        for item in listAll:
            isinstance(type(item), Invoice)
