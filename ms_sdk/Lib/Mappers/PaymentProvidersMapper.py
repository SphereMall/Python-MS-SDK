from ms_sdk.Entities.PaymentMethod import PaymentMethod
from ms_sdk.Lib.Mappers.Mapper import Mapper


class PaymentProvidersMapper(Mapper):

    def doCreateObject(self, array):
        return PaymentMethod(array)