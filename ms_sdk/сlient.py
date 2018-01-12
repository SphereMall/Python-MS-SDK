from .Lib.Exceptions import *
from .Lib.ServiceInjector import ServiceInjectorMixin

class Client(ServiceInjectorMixin):

    version = 'v1'
    amountOfCalls = 0
    
    def __init__(self, options = {}):

        for (k, v) in options.items():
            setattr(self, k, v)
        
        if not (set(['gatewayUrl','clientId','secretKey']).issubset(set(options)) & all(options.values())):
            # raise ConfigurationException()
            print('API connection data not set')


    def getVersion(self):
        return self.version


    def setVersion(self, version):
        self.version = version
        return self