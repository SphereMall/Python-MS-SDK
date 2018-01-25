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
            if type(param) == type(1):
                uriAppend = uriAppend + '/' + str(param)
            else:
                uriAppend = 'url/' + str(param)

        response = self.handler.handle('GET', False, uriAppend, params)
        return self.make(response)
