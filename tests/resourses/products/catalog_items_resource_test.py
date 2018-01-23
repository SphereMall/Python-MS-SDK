import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from tests.settings import setup_client
from ms_sdk.Entities.CatalogItem import CatalogItem


class TestCatalogItemsResource:

    def testServiceGetList(self):
        catalogItems = setup_client().catalogItems()
        itemsList = catalogItems.limit(5).all()

        for item in itemsList:
            isinstance(type(item), CatalogItem)