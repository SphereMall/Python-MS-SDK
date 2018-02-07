from tests.settings import setup_client
from ms_sdk.Entities.AttributeType import AttributeType


class TestAttributeTypesResource:

    def test_service_get_list(self):
        attributeDisplayTypes = setup_client().attributeTypes()
        attrList = attributeDisplayTypes.all()

        for item in attrList:
            isinstance(type(item), AttributeType)
