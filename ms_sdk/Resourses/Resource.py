import json

class Resource:
    
    fields = []
    offset = 0
    filter = ''
    limit = 10
    sort = []
    ids = []
    _in = []
    
    def __init__(self, client, version=''):
        self.client = client
        self.version = version or client.getVersion()


    def all(self):
        
        params = self.getQueryParams()


    def getQueryParams():
        params = {
            'offset' : self.offset,
            'limit'  : self.limit
        }

        if self.ids:
            params['ids'] = ','.join(ids)
        if self.fields:
            params['fields'] = ','.join(fields)
        if self.sort:
            params['sort'] = ','.join(sort)
        if self.filter:
            params['where'] = self.filter
        if self._in:
            params['in'] = json.dumps(self._in)