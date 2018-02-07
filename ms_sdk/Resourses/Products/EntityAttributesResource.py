import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Resourses.Resource import Resource


class EntityAttributesResource(Resource):
    """
    Class EntityAttributesResource
    :method EntityAttribute get(int id):
    :method EntityAttribute first():
    :method EntityAttribute[] all():
    :method EntityAttribute update(id, data):
    :method EntityAttribute create(data):
    """

    def getURI(self):
        return 'entityattributes'
