from .Mapper import Mapper
from ms_sdk.Entities.AttributeType import AttributeType

class AttributeTypesMapper(Mapper):

    def doCreateObject(self, array):
        return AttributeType(array)