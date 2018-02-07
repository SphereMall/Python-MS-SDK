from ms_sdk.Entities.Entity import Entity


class TestEntity:

    def test_create_object(self):
        entity = Entity
        isinstance(type(entity), Entity)

    # TODO: add Entity type test