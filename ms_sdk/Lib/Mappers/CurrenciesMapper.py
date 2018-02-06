from ms_sdk.Entities.Currency import Currency
from ms_sdk.Lib.Mappers.Mapper import Mapper


class CurrenciesMapper(Mapper):

    def doCreateObject(self, array):
        return Currency(array)