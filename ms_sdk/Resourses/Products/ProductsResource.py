import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from Resource import Resource

class ProductsResource(Resource):
    
    def getURI(self):
        return 'products'