import json
from .Mapper import Mapper
from ms_sdk.Entities.CatalogItem import CatalogItem


class CatalogItemsMapper(Mapper):

    def doCreateObject(self, array):
        catalogItem = CatalogItem(array)

        if catalogItem.filterSettings:
            catalogItem.filterSettings = json.loads(
                str(catalogItem.filterSettings))
        return catalogItem
