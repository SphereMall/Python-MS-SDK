from tests.settings import setup_client
from ms_sdk.Entities.AttributeValue import AttributeValue


class TestAttributeValuesResource:

    def test_service_get_list(self):
        attributeValues = setup_client().attributeValues()
        attrList = attributeValues.all()

        for item in attrList:
            isinstance(type(item), AttributeValue)
