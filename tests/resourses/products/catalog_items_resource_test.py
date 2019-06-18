from tests.settings import setup_client
from ms_sdk.Entities.CatalogItem import CatalogItem


class TestCatalogItemsResource:

    def test_service_get_list(self):
        catalogItems = setup_client().catalogItems()
        itemsList = catalogItems.limit().all()

        for item in itemsList:
            isinstance(type(item), CatalogItem)
