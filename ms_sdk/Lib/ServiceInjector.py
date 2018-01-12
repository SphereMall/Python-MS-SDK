import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from Resourses.Products import ProductsResource 

class ServiceInjectorMixin:

    def products(self):
        return ProductsResource(self, self)