class FullResourceMixin:

    def fullAll(self):
        return self.full()

    def fullById(self, id):
        pass

    def fullByCode(self, code):
        pass

    def full(self, param=None):
        uriAppend = 'full'
        params = self.getQueryParams()

        if param:
            if isinstance(param, int):
                uriAppend = uriAppend + '/' + param
            else:
                uriAppend = 'url/' + param

        response = self.handler.handle('GET', False, uriAppend, params)
        return self.make(response)
