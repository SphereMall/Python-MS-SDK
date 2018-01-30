import json
import sys
import os

from ms_sdk.Lib.Makers.CountMaker import CountMaker
from ms_sdk.Lib.Specifications.Basic.IsVisible import IsVisible

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Lib.Http.Request import Request
from ms_sdk.Lib.Http.Response import Response
from ms_sdk.Lib.Makers.ObjectMaker import ObjectMaker
from ms_sdk.Lib.Makers.Maker import Maker
from ms_sdk.Lib.Filters.Filter import Filter


class Resource:
    _fields = []
    offset = 0
    _filter = ''
    _limit = 10
    _sort = []
    _ids = {}
    _in = []
    meta = False

    def __init__(self, client, version=''):
        self.client = client
        self.version = version or client.getVersion()
        self.handler = Request(self.client, self)
        self.maker = ObjectMaker()

        # Reset params
        self.resetData()

    def limit(self, _limit=10, offset=0):
        self._limit = _limit
        self.offset = offset

        return self

    def getLimit(self):
        return self._limit

    def getOffset(self):
        return self.offset

    def ids(self, ids):
        self._ids = []
        if type(ids) == list:
            self._ids = ids
        else:
            self._ids.append(str(ids))
        return self

    def getIds(self):
        return self._ids

    def fields(self, fields):
        self._fields = fields
        return self

    def setIn(self, field, values):
        self._in = {field : values}
        return self

    def sort(self, field):
        self._sort.append(field)
        return self

    def getSort(self):
        return self._sort

    def resetSort(self):
        self._sort = []
        return self

    def getFields(self):
        return self._fields

    def filter(self, _filter):
        if type(_filter) == IsVisible:
            self._filter = Filter(_filter.asFilter())
        else:
            self._filter = Filter(_filter)

        return self

    def getFilter(self):
        return self._filter.getFilters()

    def resetFilters(self):
        try:
            self._filter.filters = {}
        except:
            self._filter = None
        return self

    def withMeta(self):
        self.meta = True
        return self

    def get(self, id):
        if not id:
            return print('Id is not specified')
        params = {}

        if self._fields:
            params['fields'] = ','.join(self._fields)

        response = self.handler.handle('GET', False, str(id), params)
        return self.make(response, False)

    def all(self):
        params = self.getQueryParams()
        response = self.handler.handle('GET', False, 'by', params)
        return self.make(response, False)

    def first(self):
        self.limit(1, 0)
        params = self.getQueryParams()
        response = self.handler.handle('GET', False, 'by', params)
        return self.make(response, False)

    def count(self):
        params = self.getQueryParams()
        response = self.handler.handle('GET', False, 'count', params)
        return self.make(response, False, CountMaker())

    def make(self, response, makeArray=True, maker: Maker = None):
        if not maker:
            maker = self.maker

        maker.setAsCollection(self.meta)

        if isinstance(response, Response):
            # TODO: add afterAPICall
            if makeArray:
                return maker.makeArray(response)

            return maker.makeSingle(response)

        return {'response': response, 'maker': maker, 'makeArray': makeArray}

    def getQueryParams(self):
        params = {
            'offset': self.offset,
            'limit': self._limit
        }

        if self._ids:
            params['ids'] = ','.join(self._ids)
        if self._fields:
            params['fields'] = ','.join(self._fields)
        if self._sort:
            params['sort'] = ','.join(self._sort)
        if self._filter:
            params['where'] = self._filter.toString()
        if self._in:
            params['in'] = json.dumps(self._in)

        return params

    def resetData(self):
        self._fields = []
        self.offset = 0
        self._filter = ''
        self._limit = 10
        self._sort = []
        self._ids = {}
        self._in = []