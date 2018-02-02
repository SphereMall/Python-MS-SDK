from ms_sdk.Entities.User import User
from ms_sdk.Lib.Mappers.Mapper import Mapper


class UsersMapper(Mapper):

    def doCreateObject(self, array):
        return User(array)