from tests.settings import setup_client
from ms_sdk.Entities.Entity import Entity


class TestAttributeGroupsResource:

    def test_service_get_list(self):
        attributeDisplayTypes = setup_client().attributeGroups()
        attrList = attributeDisplayTypes.all()
        isinstance(type(attrList[0]), Entity)
