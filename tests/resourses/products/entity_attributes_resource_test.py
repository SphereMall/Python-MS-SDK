from tests.settings import setup_client
from ms_sdk.Entities.EntityAttribute import EntityAttribute
from ms_sdk.Resourses.Products.EntityAttributesResource import EntityAttributesResource


class TestEntityAttributesResource:

    def test_service_get_list(self):
        entityAttributes = setup_client().entities()
        isinstance(type(entityAttributes), EntityAttributesResource)

        for item in entityAttributes.all():
            isinstance(type(item), EntityAttribute)
