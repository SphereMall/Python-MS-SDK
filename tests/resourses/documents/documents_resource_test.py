from ms_sdk.Entities.Document import Document
from tests.settings import *


class TestDocumentsResource:

    def test_document_full(self):
        documents = setup_client().documents().limit(1).full()
        isinstance(type(documents), Document)

    def test_attribute_help_methods(self):
        documents = setup_client().documents().limit(1).full()
        attribute = documents.getAttributeByCode('title')
        assert 'title' == attribute.code

        attributeValue = documents.getFirstValueByAttributeCode('title')
        assert 'test attribute value' == attributeValue.value
