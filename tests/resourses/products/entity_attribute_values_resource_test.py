from tests.settings import setup_client
from ms_sdk.Entities.EntityAttribute import EntityAttribute
from ms_sdk.Resourses.Products.EntityAttributeValuesResource import EntityAttributeValuesResource


class TestEntityAttributeValuesResource:

    def test_service_get_list(self):
        entityAttributeValues = setup_client().entityAttributeValues()
        isinstance(type(entityAttributeValues), EntityAttributeValuesResource)

        for item in entityAttributeValues.all():
            isinstance(type(item), EntityAttribute)
