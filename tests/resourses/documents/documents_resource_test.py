import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Entities.Document import Document
from tests.settings import *

class TestDocumentsResource:

    def testDocumentFull(self):
        documents = setup_client().documents().limit(1).full()
        isinstance(type(documents), Document)

    def testAttributeHelpMethods(self):
        documents = setup_client().documents().limit(1).full()

        attribute = documents.getAttributeByCode('title')
        assert 'title' == attribute.code

        # attributeValue = documents.getFirstValueByAttributeCode('title')
        # assert 'test attribute value' == attributeValue.value