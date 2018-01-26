import sys
import os

from ms_sdk.Lib.Collection import Collection
from ms_sdk.Lib.Http.Meta import Meta

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from .Maker import Maker
from ms_sdk.Lib.Http.Response import Response
from ms_sdk.Lib.Entity import Entity

from ms_sdk.Lib.Mappers import *


class ObjectMaker(Maker):

    def makeArray(self, response: Response):
        if not response.getSuccess():
            return Collection([], Meta())

        result = self.getResultFromResponse(response)

        if self.asCollection:
            collection = Collection(result, response.getMeta())
            return collection

        return result

    def makeSingle(self, response: Response):
        if not response.getSuccess():
            return None

        result = self.getResultFromResponse(response)
        return result or None

    def getResultFromResponse(self, response: Response):
        result = []
        included = self.getIncludedArray(response.getIncluded())

        for element in response.getData():
            mapperClass = self.getMapperClass(element['type'])
            result.append(self.createObject(mapperClass, element, included))
        if len(result) == 1:
            return result[0]
        return result

    def getIncludedArray(self, included):
        result = {}
        if not included:
            return result

        for include in included:
            try:
                result[include['type']].update(
                    {include['id']: include['attributes']})
            except BaseException:
                result.update(
                    {include['type']: {include['id']: include['attributes']}})

        return result

    def getMapperClass(self, type):
        try:
            return eval(type[0].upper() + type[1:] + 'Mapper.' +
                        type[0].upper() + type[1:] + 'Mapper')
        except Exception as err:
            return None

    def createObject(self, mapperClass, element, included):
        item = self.getAttributes(element)
        relations = self.getRelationships(element, included)

        try:
            item.update(included)
        except BaseException:
            item.append(relations)

        mapper = mapperClass()
        return mapper.createObject(item)

    def getAttributes(self, element):
        if element['attributes'] and isinstance(element['attributes'], dict):
            return element['attributes']
        return {}

    def getRelationships(self, element, included):
        if not element['relationships'] and not isinstance(
                element['relationships'], dict):
            return {}
        result = {}

        for (relationKey, relationValue) in element['relationships'].items():
            for relationData in relationValue['data']:
                if not relationData['id'] in included[relationData['type']]:
                    continue
                result.update({relationKey: included[relationData['type']]})
        return result
