from .Mapper import Mapper
from .ProductAttributeValuesMapper import ProductAttributeValuesMapper
from ms_sdk.Entities.Product import Product

class ProductsMapper(Mapper):

    def doCreateObject(self, array):
        product = Product(array)

        if array.get('productAttributeValues'):
            mapper = ProductAttributeValuesMapper()
            # print(array)
            product.attributes = mapper.createObject(array.get('productAttributeValues'))

        return product