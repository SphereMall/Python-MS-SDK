from ms_sdk.Exceptions.MethodNotFoundException import MethodNotFoundException
from ms_sdk.Lib.Helpers.ClassReflectionHelper import ClassReflectionHelper
from ms_sdk.Resourses import Resource


class CorrelationsResource(Resource):

    def getURI(self):
        return 'correlations'

    def getById(self, id, forClassName):
        params = self.getQueryParams()

        caseType = ClassReflectionHelper(forClassName).getShortLowerCaseName()
        uriAppend = '{}/{}'.format(caseType, id)

        response = self.handler.handle('GET', False, uriAppend, params)
        return self.make(response)

    def get(self, id):
        raise MethodNotFoundException('Method get() can not be use with correlations')

    def update(self, id, data):
        raise MethodNotFoundException('Method update() can not be use with correlations')

    def create(self, data):
        raise MethodNotFoundException('Method create() can not be use with correlations')

    def delete(self, id):
        raise MethodNotFoundException('Method delete() can not be use with correlations')