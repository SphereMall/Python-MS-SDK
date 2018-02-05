from ms_sdk.Entities.WishListItem import WishListItem
from ms_sdk.Lib.Mappers.Mapper import Mapper
from ms_sdk.Lib.Mappers.ProductsMapper import ProductsMapper


class WishListItemsMapper(Mapper):

    def doCreateObject(self, array):
        orderItem = WishListItem(array)

        try:
            first = array.get('products')[0]
        except:
            first = array

        if first:
            productMapper = ProductsMapper()

            if array.get('images'):
                array['products'][0]['images'] = array['images']

            orderItem.product = productMapper.createObject(first)

        return orderItem