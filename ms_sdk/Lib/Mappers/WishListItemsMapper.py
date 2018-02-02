from ms_sdk.Entities.WishListItem import WishListItem
from ms_sdk.Lib.Mappers.Mapper import Mapper
from ms_sdk.Lib.Mappers.ProductsMapper import ProductsMapper


class WishListItemsMapper(Mapper):

    def doCreateObject(self, array):
        orderItem = WishListItem(array)
        print(array)
# array.get('productAttributeValues'):
        if array.get('products')[0]:
            productMapper = ProductsMapper()

            if array.get('images'):
                array['products'][0]['images'] = array['images']

            orderItem.product = productMapper.createObject(array['products'][0])