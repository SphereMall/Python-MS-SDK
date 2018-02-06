from ms_sdk.Entities.Invoice import Invoice
from ms_sdk.Lib.Mappers.Mapper import Mapper


class InvoicesMapper(Mapper):

    def doCreateObject(self, array):
        return Invoice(array)