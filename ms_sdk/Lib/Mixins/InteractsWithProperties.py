

class InteractsWithPropertiesMixin:

    properties = {}
    entity = {}

    def getProperty(self, name):
        if self.properties[name]:
            return self.properties[name]

        return None

    def getPropertiesField(self):
        return self.properties

    def __get(self, name):
        return self.getProperty(name)

    def setPropertiesField(self, data):
        for optionKey, optionValue in data.items():
            self.properties.update({optionKey: optionValue})

    def setPropertyList(self, data):
        for optionKey, optionValue in data.items():
            if hasattr(self, optionKey):
                setattr(self, optionKey, optionValue)
            # For reserved vars '_varname'
            elif hasattr(self, '_' + optionKey):
                setattr(self, '_' + optionKey, optionValue)
            else:
                self.properties.update({optionKey: optionValue})
