from ms_sdk.Entities.AttributeDisplayType import AttributeDisplayType
from .Mapper import Mapper


class AttributeDisplayTypesMapper(Mapper):

    def doCreateObject(self, array):
        attributeDisplayType = AttributeDisplayType(array)
        return attributeDisplayType
