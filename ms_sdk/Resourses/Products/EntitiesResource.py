import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Resourses.Resource import Resource


class EntitiesResource(Resource):

    def getURI(self):
        return 'entities'