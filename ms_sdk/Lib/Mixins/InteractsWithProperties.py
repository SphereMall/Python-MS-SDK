

class InteractsWithPropertiesMixin:

    properties = {}
    entity = {}

    def getProperty(self, name):
        """
        Get value by name from property of class or properties if value is not exist in class
        :param name:
        :rtype None|bool:
        """
        if self.properties[name]:
            return self.properties[name]

        return None

    def getPropertiesField(self):
        """
        :rtype dict:
        """
        return self.properties

    def __get(self, name):
        """
        :param name:
        :rtype bool:
        """
        return self.getProperty(name)

    def setPropertiesField(self, data):
        """
        :param dict data:
        """
        for optionKey, optionValue in data.items():
            self.properties.update({optionKey: optionValue})

    def setPropertyList(self, data):
        """
        :param dict data:
        """
        for optionKey, optionValue in data.items():
            if hasattr(self, optionKey):
                setattr(self, optionKey, optionValue)
            # For reserved vars '_varname'
            elif hasattr(self, '_' + optionKey):
                setattr(self, '_' + optionKey, optionValue)
            else:
                self.properties.update({optionKey: optionValue})
