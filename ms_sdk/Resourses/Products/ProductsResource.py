import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from ms_sdk.Resourses.Resource import Resource
from ms_sdk.Resourses.Mixins.FullResource import FullResourceMixin


class ProductsResource(Resource, FullResourceMixin):
    
    def getURI(self):
        return 'products'