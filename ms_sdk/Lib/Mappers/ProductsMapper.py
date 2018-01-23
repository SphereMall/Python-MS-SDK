from .Mapper import Mapper
from .ProductAttributeValuesMapper import ProductAttributeValuesMapper
from .ImagesMapper import ImagesMapper
from .BrandsMapper import BrandsMapper
from .FunctionalNamesMapper import FunctionalNamesMapper
from ms_sdk.Entities.Product import Product

class ProductsMapper(Mapper):

    def doCreateObject(self, array):
        product = Product(array)

        try:
            if array.get('productAttributeValues'):
                mapper = ProductAttributeValuesMapper()
                product.attributes = mapper.createObject(array.get('productAttributeValues'))
        except:
            pass

        try:
            if array.get('images'):
                mapper = ImagesMapper()

                for image in array.get('images'):
                    product.media.append(mapper.createObject(image))

                if product.media[0]:
                    product.mainMedia = product.media[0]
        except:
            pass

        try:
            if list(array.get('brands'))[0]:
                mapper = BrandsMapper()
                product.brand = mapper.createObject(list(array.get('brands'))[0])
        except:
            pass

        try:
            if list(array.get('functionalNames'))[0]:
                mapper = FunctionalNamesMapper()
                product.brand = mapper.createObject(list(array.get('functionalNames'))[0])
        except:
            pass

        return product