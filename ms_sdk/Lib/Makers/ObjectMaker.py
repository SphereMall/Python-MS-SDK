import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from .Maker import Maker
from .DictMaker import DictMaker
from ms_sdk.Lib.Http.Response import Response
from ms_sdk.Lib.Mappers import (ProductsMapper, UsersMapper)
from ms_sdk.Lib.Entity import Entity

class ObjectMaker(Maker):
    def makeArray(response: Response):
        if not response.getSuccess():
            pass

    def makeSingle(self, response: Response):
        if not response.getSuccess():
            return None

        result = self.getResultFromResponse(response)
        return result or None

    def getResultFromResponse(self, response: Response):
        result = []
        included = self.getIncludedArray(response.getIncluded())
        for element in response.getData():
            # mapperClass = self.getMapperClass(element['type'])
            result.append(self.createObject(element, included))

        return result

    def getIncludedArray(self, included):
        result = []
        if not included:
            return result

        for include in included:
            result[include['type']][include['id']] = include['attributes']
        return result

    # def getMapperClass(self, type):
    #     try:
    #         return eval(type.capitalize() + 'Mapper.' + type.capitalize() + 'Mapper')
    #     except:
    #         return None

    def createObject(self, element, included):
        item = self.getAttributes(element)
        relations = self.getRelationships(element, included)

        try:
            item.update(relations)
        except:
            item += relations

        entities = Entity(item)
        # print(entities)

        return entities

    def getAttributes(self, element):
        if element['attributes'] and type(element['attributes']) == dict:
            return element['attributes']
        return []

    def getRelationships(self, element, included):
        if not element['relationships'] and not type(element['relationships']) == dict:
            return []
        result = []

        for (relationKey, relationValue) in element['relationships'].items():
            for relationData in relationValue['data']:
                result[relationKey] = included[relationData['type']][relationData['id']]
        return result

