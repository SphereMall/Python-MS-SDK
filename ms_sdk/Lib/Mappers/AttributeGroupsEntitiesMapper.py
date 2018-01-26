from .Mapper import Mapper
from ms_sdk.Entities.AttributeGroupsEntities import AttributeGroupsEntities


class AttributeGroupsEntitiesMapper(Mapper):

    def doCreateObject(self, array):
        attributeGroup = AttributeGroupsEntities(array)
        return attributeGroup
