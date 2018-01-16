import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from .Maker import Maker
from .DictMaker import DictMaker
from ms_sdk.Lib.Http.Response import Response
from ms_sdk.Lib import Mappers

class ObjectMaker(Maker):

    def makeArray(response: Response):
        if not response.getSuccess():
            pass


    def makeSingle(self, response: Response):
        if not response.getSuccess():
            return None

        # print(response)

        result = self.getResultFromResponse(response.data)
        
        return result or None


    def getResultFromResponse(self, response: Response):
        result = []
        included = self.getIncludedArray(response.getIncluded())

        for element in response.getData():
            print(element['type'])
            mapperClass = self.getMapperClass(element['type'])
            print(mapperClass)

        return response

    def getIncludedArray(self, included):
        result = []
        for include in included:
            result[include['type']][include['id']] = include['attributes']

        return result

    def getMapperClass(self, type):
        try:
            return eval('Mappers.' + type + 'Mapper')
        except:
            return None


    