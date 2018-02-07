from tests.settings import setup_client
from ms_sdk.Entities.Entity import Entity


class TestAttributeGroupsEntitiesResource:

    def test_service_get_list(self):
        attributeGroupsEntities = setup_client().attributeGroupsEntities()
        attrList = attributeGroupsEntities.all()
        isinstance(type(attrList[0]), Entity)
