from ms_sdk.Entities.Message import Message
from ms_sdk.Lib.Mappers.Mapper import Mapper


class UserMessagesMapper(Mapper):

    def doCreateObject(self, array):
        return Message(array)