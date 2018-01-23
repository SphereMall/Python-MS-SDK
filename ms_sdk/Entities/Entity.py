from ms_sdk.Resourses.Mixins.InteractsWithProperties import InteractsWithPropertiesMixin

class Entity(InteractsWithPropertiesMixin):

    def __init__(self, array):
        if not array:
            return self

        return self.setPropertyList(array)

    def asArray(self):
        properties = {}

        for itemKey, itemValue in self:
            if itemKey == 'properties':
                continue
            properties.update( { itemKey : itemValue })

        return properties.update(self.properties)

