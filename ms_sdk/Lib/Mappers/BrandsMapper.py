from .Mapper import Mapper
from ms_sdk.Entities.Brand import Brand


class BrandsMapper(Mapper):

    def doCreateObject(self, array):
        return Brand(array)
