import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from ms_sdk.Resourses.Resource import Resource


class AttributesResource(Resource):

    def getURI(self):
        return 'attributes'

    def belong(self, entityClass, attributeGroupId=None, attributeId=None):
        # TODO: Remake entityClass
        uriAppend = '/belong/' + entityClass.lower() + 's'
        params = self.getQueryParams()

        if attributeGroupId:
            uriAppend += '/' + str(attributeGroupId)
            if attributeId:
                uriAppend += '/' + str(attributeId)

        response = self.handler.handle('GET', False, uriAppend, params)
        return self.make(response)
