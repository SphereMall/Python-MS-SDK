import pytest
import requests
import requests_mock
from ms_sdk.Exceptions.MethodNotFoundException import MethodNotFoundException
from ms_sdk.Lib.Mappers.ProductPriceConfigurationsMapper import ProductPriceConfigurationsMapper
from ms_sdk.Lib.Prices.PriceConfigurationFilter import PriceConfigurationFilter
from ms_sdk.Lib.Prices.PriceProduct import PriceProduct
from ms_sdk.Resourses.Prices.ProductPriceConfigurationsResource import ProductPriceConfigurationsResource
from tests.settings import setup_client


class TestProductPriceConfigurationsResource:

    priceConfigurationResult = {}
    priceConfigurationResult['success'] = True
    priceConfigurationResult['included'] = []

    priceConfigurationResult['data'] = [
        {
            'type': 'productPriceConfigurations',
            'id': '282',
            'attributes': {
                'id': '282',
                'productId': 607,
                'prices': {
                    'affectAttributes': {'226', '227'},
                    'priceTable': {
                        '3748;3749': '4769',
                        '3748;3750': '5269',
                        '3748;3751': '5769',
                        '3748;3752': '6269',
                        '3748;3753': '6769',
                        '3748;3754': '7269',
                        '3748;3755': '7769',
                        '3748;3756': '8269',
                        '3748;3757': '8864',
                        '3748;3758': '9509',
                        '3748;3759': '10154',
                        '3748;3760': '10947',
                        '3748;3761': '11840',
                        '3748;3762': '12633',
                        '3748;3763': '13625',
                        '3748;3764': '14716',
                        '3748;3765': '15460',
                        '3748;3766': '15707',
                        '3748;3767': '16005',
                        '3748;3768': '16402',
                        '3748;3769': '16749',
                        '3748;3770': '16947',
                    },
                },
            },
        },
    ]

    def test_is_product_price_configuration_resource_available(self):
        priceConfiguration = setup_client().productPriceConfigurations()
        isinstance(type(priceConfiguration), ProductPriceConfigurationsResource)

    def test_not_available_product_price_configurations_get(self):
        priceConfiguration = setup_client().productPriceConfigurations()

        with pytest.raises(MethodNotFoundException):
            priceConfiguration.get(1)

    def test_not_available_product_price_configurations_delete(self):
        priceConfiguration = setup_client().productPriceConfigurations()

        with pytest.raises(MethodNotFoundException):
            priceConfiguration.delete(1)

    def test_not_available_product_price_configurations_update(self):
        priceConfiguration = setup_client().productPriceConfigurations()

        with pytest.raises(MethodNotFoundException):
            priceConfiguration.update(1, [])

    # def test_not_available_product_price_configurations_create(self):
    #     priceConfiguration = setup_client().productPriceConfigurations()
    #
    #     with pytest.raises(MethodNotFoundException):
    #         priceConfiguration.create([])
    #
    # def test_available_method_find_price(self):
    #     priceConfigurationFilter = PriceConfigurationFilter()
    #     priceConfigurationFilter.addProduct(PriceProduct(607, 1))
    #
    #     productPriceConfigurationsResource = self.getProductPriceConfMockedResource(priceConfigurationFilter)
    #
    #     productPriceConfigurations = productPriceConfigurationsResource.findPrice(priceConfigurationFilter)
    #     assert 1 == productPriceConfigurations
    #
    #     productPriceConfiguration = ProductPriceConfigurationsMapper()\
    #         .createObject(self.priceConfigurationResult['data'][0]['attributes'])
    #     assert productPriceConfiguration == productPriceConfigurations[0]

    # def getProductPriceConfMockedResource(self, priceConfigurationFilter):
        #
        # with requests_mock.Mocker() as m:
        #     m.post('http://test.com', text='resp')
        #     assert requests.get('http://test.com').text == 'resp'
        # requestHandler =

        # productPriceConfigurationsResource = ProductPriceConfigurationsResource(
        #     setup_client(),
        #     'v1',
        #     # requestHandler
        # )
        #
        # return productPriceConfigurationsResource
