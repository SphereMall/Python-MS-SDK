from ms_sdk.Entities.Vat import Vat
from ms_sdk.Lib.Mappers.Mapper import Mapper


class VatMapper(Mapper):

    def doCreateObject(self, array):
        return Vat(array)