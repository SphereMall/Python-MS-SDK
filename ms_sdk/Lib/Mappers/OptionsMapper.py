from .Mapper import Mapper
from ms_sdk.Entities.Option import Option

class OptionsMapper(Mapper):

    def doCreateObject(self, array):
        return Option(array)