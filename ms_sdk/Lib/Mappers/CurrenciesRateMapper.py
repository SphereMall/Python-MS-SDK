from ms_sdk.Entities.CurrencyRate import CurrencyRate
from ms_sdk.Lib.Mappers.Mapper import Mapper


class CurrenciesRateMapper(Mapper):

    def doCreateObject(self, array):
        return CurrencyRate(array)