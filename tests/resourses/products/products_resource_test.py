from tests.settings import setup_client
from ms_sdk.Entities.Product import Product
from ms_sdk.Lib.Collection import Collection


class TestProductsResource:

    def test_service_get_list(self):
        products = setup_client().products()
        productArray = products.all()
        productList = Collection(productArray)

        assert 10 == productList.count()

        ids = productList.current().id
        productArray = products.ids(ids).all()
        productList = Collection(productArray)

        assert 1 == productList.count()
        assert ids in products.getIds()

        if 1 == productList.count():
            isinstance(type(productList), Product)
        else:
            raise print('Count Error')

    def test_service_get_list_with_meta(self):
        products = setup_client().products()
        productCollection = products.withMeta().all()
        isinstance(type(productCollection), Collection)

    def test_product_full(self):
        products = setup_client().products().limit(2).full()
        assert 2 == len(products)

        products = setup_client().products().ids(6351).limit(1).full()
        assert '6351' == products.id

        products = setup_client().products().full(6351)
        assert '6351' == products.id

        products = setup_client().products().full('limoen-komkommer-fruitwater')
        assert 'limoen-komkommer-fruitwater' in products.urlCode
        assert type(products) != list

    def test_attribute_help_methods(self):
        product = setup_client().products().limit(1).full()

        attribute = product.getAttributeByCode('test-html')
        assert 'test-html' == attribute.code

        attributeValue = product.getFirstValueByAttributeCode('test-html')
        assert 'fghfghfgh' == attributeValue.value

