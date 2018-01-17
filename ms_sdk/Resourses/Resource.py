import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Lib.Http.Request import Request
from ms_sdk.Lib.Http.Response import Response
from ms_sdk.Lib.Makers.ObjectMaker import ObjectMaker
from ms_sdk.Lib.Makers.Maker import Maker

class Resource():
    
    fields = []
    offset = 0
    filter = ''
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


    def get(self, id):
        if not id:
            return print('Id is not specified')

        params = []

        if self.fields:
            params['fields'] = ','.join(self.fields)

        response = self.handler.handle('GET', False, str(id), params)
        return self.make(response, False)


    def all(self):
        
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
        if self.fields:
            params['fields'] = ','.join(self.fields)
        if self.sort:
            params['sort'] = ','.join(self.sort)
        if self.filter:
            params['where'] = self.filter
        if self._in:
            params['in'] = json.dumps(self._in)

        return params


