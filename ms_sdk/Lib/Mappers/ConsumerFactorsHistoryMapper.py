from ms_sdk.Lib.Mappers.Mapper import Mapper
from ms_sdk.Entities.ConsumerFactorsHistory import ConsumerFactorsHistory


class ConsumerFactorsHistoryMapper(Mapper):

    def doCreateObject(self, array):
        """
        :param dict array:
        :return ConsumerFactorsHistory:
        """
        return ConsumerFactorsHistory(array)
