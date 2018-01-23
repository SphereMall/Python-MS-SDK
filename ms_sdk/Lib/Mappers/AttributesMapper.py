from .Mapper import Mapper
from .AttributeValuesMapper import AttributeValuesMapper
from .AttributeGroupsMapper import AttributeGroupsMapper
from ms_sdk.Entities.Attribute import Attribute

class AttributesMapper(Mapper):

    def doCreateObject(self, array):
        attribute = Attribute(array)

        try:
            if array.get('attributeValues'):
                mapper = AttributeValuesMapper()
                attribute.values = mapper.createObject(array.get('attributeValues'))
        except:
            pass

        try:
            if array.get('attributeGroups'):
                mapper = AttributeGroupsMapper()
                attribute.group = mapper.createObject(array.get('attributeGroups'))
        except:
            pass

        return attribute
