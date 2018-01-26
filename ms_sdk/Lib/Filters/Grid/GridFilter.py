import json
import urllib.parse

from ms_sdk.Lib.Filters.Filter import Filter


class GridFilter(Filter):
    level = 0
    _elements = {}

    def elements(self, elements):
        self._elements[self.level] = {}

        for element in elements:
            self._elements[self.level].update({element.getName() : element.getValues()})

        self.level += 1
        return self


    def reset(self):
        self._elements.clear()
        self.level = 0
        return self


    def setFilters(self, filters = {}):
        for key, value in filters:
            self.addFilter(key, value)
        return self


    def addFilter(self, field, value, operator = None):
        self.filters.update({field : value})
        return self


    def getElements(self):
        return self._elements


    def toString(self):
        setParams = self.getStandardFilter()

        if self._elements:
            setParams['params'] = json.dumps(self._elements)
        return urllib.parse.unquote_plus(urllib.parse.urlencode(setParams)).replace('={"0": ', '=[').replace('"1": ', '').replace('}}', '}]').replace(' ', '')


    def getStandardFilter(self):
        setParams = {}
        if self.filters:
            for key, value in self.filters:
                if type(value) == dict:
                    setParams.update({key : ','.join(value)})
                else:
                    setParams.update({key : value})
        return setParams