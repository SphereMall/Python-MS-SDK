from ms_sdk.Resourses.Documents.DocumentsResource import DocumentsResource
from ms_sdk.Resourses.Grapher.CorrelationsResource import CorrelationsResource
from ms_sdk.Resourses.Grapher.GridResource import GridResource
from ms_sdk.Resourses.Prices.ProductPriceConfigurationsResource import ProductPriceConfigurationsResource
from ms_sdk.Resourses.Shop.CurrenciesRateResource import CurrenciesRateResource
from ms_sdk.Resourses.Shop.CurrenciesResource import CurrenciesResource
from ms_sdk.Resourses.Shop.DeliveryPaymentsResource import DeliveryPaymentsResource
from ms_sdk.Resourses.Shop.DeliveryProvidersResource import DeliveryProvidersResource
from ms_sdk.Resourses.Shop.InvoicesResource import InvoicesResource
from ms_sdk.Resourses.Shop.OrderItemsResource import OrderItemsResource
from ms_sdk.Resourses.Shop.PaymentMethodsResource import PaymentMethodsResource
from ms_sdk.Resourses.Shop.PaymentProvidersResource import PaymentProvidersResource
from ms_sdk.Resourses.Shop.VatsResource import VatsResource
from ms_sdk.Resourses.Users.CompaniesResource import CompaniesResource
from ms_sdk.Resourses.Users.MessagesResource import MessagesResource
from ms_sdk.Resourses.Users.UsersResource import UsersResource
from ms_sdk.Resourses.Products import (
    ProductsResource,
    AttributeDisplayTypesResource,
    AttributeGroupsEntitiesResource,
    AttributeGroupsResource,
    AttributesResource,
    CatalogItemsResource,
    EntitiesResource,
    MediaResource,
    EntityAttributesResource,
    AttributeTypesResource,
    AttributeValuesResource,
    MediaTypesResource,
    OptionsResource,
    BrandsResource,
    FunctionalNamesResource,
    ProductAttributeValuesResource,
    EntityAttributeValuesResource)
from ms_sdk.Resourses.Users.WishListItemsResource import WishListItemsResource

class ServiceInjectorMixin:

    # Products
    def attributeDisplayTypes(self):
        """
        Client self
        :return AttributeDisplayTypesResource:
        """
        return AttributeDisplayTypesResource(self)

    def attributes(self):
        """
        Client self
        :return AttributesResource:
        """
        return AttributesResource(self)

    def attributeGroupsEntities(self):
        """
        Client self
        :return AttributeGroupsEntitiesResource:
        """
        return AttributeGroupsEntitiesResource(self)

    def attributeGroups(self):
        """
        Client self
        :return AttributeGroupsResource:
        """
        return AttributeGroupsResource(self)

    def attributeTypes(self):
        """
        Client self
        :return AttributeTypesResource:
        """
        return AttributeTypesResource(self)

    def attributeValues(self):
        """
        Client self
        :return AttributeValuesResource:
        """
        return AttributeValuesResource(self)

    def products(self):
        """
        Client self
        :return ProductsResource:
        """
        return ProductsResource(self)

    def brands(self):
        """
        Client self
        :return BrandsResource:
        """
        return BrandsResource(self)

    def options(self):
        """
        Client self
        :return OptionsResource:
        """
        return OptionsResource(self)

    def catalogItems(self):
        """
        Client self
        :return CatalogItemsResource:
        """
        return CatalogItemsResource(self)

    def entities(self):
        """
        Client self
        :return EntitiesResource:
        """
        return EntitiesResource(self)

    def entityAttributes(self):
        """
        Client self
        :return EntityAttributesResource:
        """
        return EntityAttributesResource(self)

    def entityAttributeValues(self):
        """
        Client self
        :return EntityAttributeValuesResource:
        """
        return EntityAttributeValuesResource(self)

    def media(self):
        """
        Client self
        :return MediaResource:
        """
        return MediaResource(self)

    def mediaTypes(self):
        """
        Client self
        :return MediaTypesResource:
        """
        return MediaTypesResource(self)

    def functionalNames(self):
        """
        Client self
        :return FunctionalNamesResource:
        """
        return FunctionalNamesResource(self)

    def productAttributeValues(self):
        """
        Client self
        :return ProductAttributeValuesResource:
        """
        return ProductAttributeValuesResource(self)

    # Documents
    def documents(self):
        """
        Client self
        :return DocumentsResource:
        """
        return DocumentsResource(self)

    # Grapher service
    def correlations(self):
        """
        Client self
        :return CorrelationsResource:
        """
        return CorrelationsResource(self)

    def grid(self):
        """
        Client self
        :return GridResource:
        """
        return GridResource(self)

    # Users service
    def users(self):
        """
        Client self
        :return UsersResource:
        """
        return UsersResource(self)

    def companies(self):
        """
        Client self
        :return CompaniesResource:
        """
        return CompaniesResource(self)

    def messages(self):
        """
        Client self
        :return MessagesResource:
        """
        return MessagesResource(self)

    def wishListItems(self):
        """
        Client self
        :return WishListItemsResource:
        """
        return WishListItemsResource(self)

    # Prices service
    def productPriceConfigurations(self):
        """
        Client self
        :return ProductPriceConfigurationsResource:
        """
        return ProductPriceConfigurationsResource(self)

    # Shop service
    def currencies(self):
        """
        Client self
        :return CurrenciesResource:
        """
        return CurrenciesResource(self)

    def currenciesRate(self):
        """
        Client self
        :return CurrenciesRateResource:
        """
        return CurrenciesRateResource(self)

    def invoices(self):
        """
        Client self
        :return InvoicesResource:
        """
        return InvoicesResource(self)

    def orderItems(self):
        """
        Client self
        :return OrderItemsResource:
        """
        return OrderItemsResource(self)

    def deliveryProviders(self):
        """
        Client self
        :return DeliveryProvidersResource:
        """
        return DeliveryProvidersResource(self)

    def paymentMethods(self):
        """
        Client self
        :return PaymentMethodsResource:
        """
        return PaymentMethodsResource(self)

    def deliveryPayments(self):
        """
        Client self
        :return DeliveryPaymentsResource:
        """
        return DeliveryPaymentsResource(self)

    def paymentProviders(self):
        """
        Client self
        :return PaymentProvidersResource:
        """
        return PaymentProvidersResource(self)

    def vats(self):
        """
        Client self
        :return VatsResource:
        """
        return VatsResource(self)