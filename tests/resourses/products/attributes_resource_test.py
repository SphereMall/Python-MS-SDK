from tests.settings import setup_client
from ms_sdk.Entities.Attribute import Attribute


class TestAttributesResource:

    def test_service_get_list(self):
        attributes = setup_client().attributes()
        attrList = attributes.all()

        for item in attrList:
            isinstance(type(item), Attribute)

    # TODO: Belongs deleted in the database
    # def test_attributes_belong_entity_attribute_group_attribute(self):
    #     attributes = setup_client().attributes()
    #     attrList = attributes.belong('product', 2, 0)
    #
    #     for item in attrList:
    #         isinstance(type(item), Attribute)
    #
    # def test_attributes_belong_entity_attribute_group(self):
    #     attributes = setup_client().attributes()
    #     attrList = attributes.belong('product', 2)
    #
    #     for item in attrList:
    #         isinstance(type(item), Attribute)
    #
    # def test_attributes_belong_entity(self):
    #     attributes = setup_client().attributes()
    #     attrList = attributes.belong('product')
    #
    #     for item in attrList:
    #         isinstance(type(item), Attribute)

    def test_attribute_help_methods(self):
        products = setup_client().products().limit().full()
        attributes = products[0].attributes

        for item in attributes:
            isinstance(type(item), Attribute)
