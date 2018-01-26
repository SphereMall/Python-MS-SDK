from .Mapper import Mapper
from ms_sdk.Entities.SMEntity import SMEntity


class EntitiesMapper(Mapper):

    def doCreateObject(self, array):
        return SMEntity(array)
