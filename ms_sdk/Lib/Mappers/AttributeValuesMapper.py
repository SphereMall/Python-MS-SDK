from .Mapper import Mapper
from ms_sdk.Entities.AttributeValue import AttributeValue

class AttributeValuesMapper(Mapper):

    def doCreateObject(self, array):
        return AttributeValue(array)