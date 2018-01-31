import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Resourses.Mixins.FullResource import FullResourceMixin
from ms_sdk.Resourses.Resource import Resource


class DocumentsResource(Resource, FullResourceMixin):

    def getURI(self):
        return 'documents'
