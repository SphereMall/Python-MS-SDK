import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Resourses.Resource import Resource


class FunctionalNamesResource(Resource):
    """
    Class FunctionalNamesResource
    :method FunctionalName get(int id):
    :method FunctionalName first():
    :method FunctionalName[] all():
    :method FunctionalName update(id, data):
    :method FunctionalName create(data):
    """

    def getURI(self):
        return 'functionalnames'
