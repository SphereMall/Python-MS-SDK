from .Mapper import Mapper
from ms_sdk.Entities.AttributeGroup import AttributeGroup

class AttributeGroupsMapper(Mapper):

    def doCreateObject(self, array):
        attributeGroup = AttributeGroup(array)
        return attributeGroup