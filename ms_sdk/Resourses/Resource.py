import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Lib.Http.Request import Request
from ms_sdk.Lib.Http.Response import Response
from ms_sdk.Lib.Makers.ObjectMaker import ObjectMaker
from ms_sdk.Lib.Makers.Maker import Maker
from ms_sdk.Lib.Filters.Filter import Filter

class Resource():
    _fields = []
    offset = 0
    _filter = ''
    _limit = 10
    sort = []
    ids = []
    _in = []
    meta = False
    
    def __init__(self, client, version=''):
        self.client = client
        self.version = version or client.getVersion()

        self.handler = Request(self.client, self)

        self.maker = ObjectMaker()

    def limit(self, _limit = 10, offset = 0):
        self._limit = _limit
        self.offset = offset

        return self

    def getLimit(self):
        return self.limit

    def getOffset(self):
        return self.offset

    def ids(self, ids):
        self.ids = ids
        return self

    def getIds(self):
        return self.ids

    def fields(self, fields):
        self._fields = fields
        return self

    def getFields(self):
        return self._fields

    def filter(self, _filter):
        # if _filter == list:
            # print('asddasasddas')
        _filter = Filter(_filter)

        self._filter = _filter
        return self._filter


    def get(self, id):
        if not id:
            return print('Id is not specified')
        params = []

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

    def make(self, response, makeArray = True, maker: Maker = None):
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
            'offset' : self.offset,
            'limit'  : self._limit
        }

        # if self.ids:
            # params['ids'] = ','.join(self.ids)
        if self._fields:
            params['fields'] = ','.join(self._fields)
        if self.sort:
            params['sort'] = ','.join(self.sort)
        if self._filter:
            params['where'] = str(self.filter)
            print(params['where'])
        if self._in:
            params['in'] = json.dumps(self._in)

        return params


