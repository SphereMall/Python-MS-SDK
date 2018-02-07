import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Resourses.Resource import Resource


class OptionsResource(Resource):
    """
    Class OptionResource
    :method Option get(int $id):
    :method Option first():
    :method Option[] all():
    :method Option update($id, $data):
    :method Option create($data):
    """

    def getURI(self):
        return 'options'
