from ms_sdk.Lib.Mappers.Mapper import Mapper
from ms_sdk.Entities.Product import Product
from .ImagesMapper import ImagesMapper
from .BrandsMapper import BrandsMapper
from .FunctionalNamesMapper import FunctionalNamesMapper
from .ProductAttributeValuesMapper import ProductAttributeValuesMapper


class ProductsMapper(Mapper):

    def doCreateObject(self, array):
        """
        :param dict array:
        :return Product:
        """
        product = Product(array)

        try:
            if array.get('productAttributeValues'):
                mapper = ProductAttributeValuesMapper()
                product.attributes = mapper.createObject(
                    array.get('productAttributeValues'))
        except BaseException:
            pass

        try:
            if array.get('images'):
                mapper = ImagesMapper()

                for image in array.get('images'):
                    product.media.append(mapper.createObject(image))

                if product.media[0]:
                    product.mainMedia = product.media[0]
        except BaseException:
            pass

        try:
            if list(array.get('brands'))[0]:
                mapper = BrandsMapper()
                product.brand = mapper.createObject(
                    list(array.get('brands'))[0])
        except BaseException:
            pass

        try:
            if list(array.get('functionalNames'))[0]:
                mapper = FunctionalNamesMapper()
                product.brand = mapper.createObject(
                    list(array.get('functionalNames'))[0])
        except BaseException:
            pass

        return product
