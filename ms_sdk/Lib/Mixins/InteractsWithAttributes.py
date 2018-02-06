from ms_sdk.Entities.Attribute import Attribute
from ms_sdk.Entities.AttributeValue import AttributeValue


class InteractsWithAttributesMixin:

    def getAttributeById(self, id):
        return self.getAttributeByFieldNameAndValue('id', id)

    def getAttributesByIds(self, ids):
        return self.getAttributesByFieldNameAndValues('id', ids)

    def getAttributeByCode(self, code):
        return self.getAttributeByFieldNameAndValue('code', code)

    def getAttributesByCodes(self, codes):
        return self.getAttributesByFieldNameAndValues('code', codes)

    def getFirstValueByAttributeCode(self, code):
        attribute = self.getAttributeByCode(code)

        try:
            values = attribute.values[0]
        except:
            values = attribute.values

        if not values:
            return None

        return values

    def getAttributeByFieldNameAndValue(self, fieldName, value):
        if not self.attributes:
            return None

        for attribute in self.attributes:

            if eval('attribute.' + fieldName) == value:
                return attribute

        return None

    def getAttributesByFieldNameAndValues(self, fieldName, value):
        attributes = []

        if not self.attributes or not self.attributes:
            return attributes

        for attribute in self.attributes:
            if (eval('attribute.' + fieldName) in value) or (eval('attribute.' + fieldName) == value):
                attributes.append(attribute)

        return attributes
