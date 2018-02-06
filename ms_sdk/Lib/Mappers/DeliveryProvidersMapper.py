from ms_sdk.Entities.DeliveryProvider import DeliveryProvider
from ms_sdk.Lib.Mappers.Mapper import Mapper


class DeliveryProvidersMapper(Mapper):

    def doCreateObject(self, array):
        return DeliveryProvider(array)