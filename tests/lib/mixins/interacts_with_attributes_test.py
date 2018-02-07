from ms_sdk.Entities.Attribute import Attribute
from ms_sdk.Entities.Product import Product


class TestInteractsWithAttributes:

    def test_get_attribute_by_code(self):
        product = self.get_mocked_product()
        assert 'second' == product.getAttributeByCode('second').code

    def test_get_attribute_by_id(self):
        product = self.get_mocked_product()
        assert 3 == product.getAttributeById(3).id

    def test_get_attribute_by_ids(self):
        product = self.get_mocked_product()
        attrs = [Attribute({'id': 2, 'code': 'first'}).id,
                 Attribute({'id': 1, 'code': 'second'}).id]

        assert attrs == \
               list([product.getAttributesByIds([2, 1])[1].id, product.getAttributesByIds([2, 1])[0].id])

    def test_get_attribute_by_codes(self):
        product = self.get_mocked_product()
        attrs = [Attribute({'id': 1, 'code': 'first'}).code,
                 Attribute({'id': 2, 'code': 'second'}).code]

        assert attrs == \
               list([product.getAttributesByCodes(['first', 'second'])[0].code, product.getAttributesByCodes(['first', 'second'])[1].code])

    def get_mocked_product(self):
        product = Product({'id' : 1})

        first = Attribute({'id' : 1, 'code' : 'first'})
        second =  Attribute({'id' : 2,'code' : 'second'})
        third = Attribute({'id': 3,'code': 'third'})

        product.attributes = [first, second, third]
        return product