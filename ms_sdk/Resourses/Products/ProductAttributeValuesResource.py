import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Resourses.Resource import Resource


class ProductAttributeValuesResource(Resource):
    """
    Class ProductAttributeValuesResource
    :method Attribute get(int $id):
    :method Attribute first():
    :method Attribute[] all():
    :method Attribute update($id, $data):
    :method Attribute create($data):
    """

    def getURI(self):
        return 'brands'
