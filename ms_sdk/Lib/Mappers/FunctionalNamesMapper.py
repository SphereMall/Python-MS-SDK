from .Mapper import Mapper
from ms_sdk.Entities.FunctionalName import FunctionalName

class FunctionalNamesMapper(Mapper):

    def doCreateObject(self, array):
        return FunctionalName(array)