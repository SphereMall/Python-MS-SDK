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
    ProductAttributeValuesResource)
from ms_sdk.Resourses.Users.WishListItemsResource import WishListItemsResource

class ServiceInjectorMixin:

    # Products
    def attributeDisplayTypes(self):
        return AttributeDisplayTypesResource(self)

    def attributes(self):
        return AttributesResource(self)

    def attributeGroupsEntities(self):
        return AttributeGroupsEntitiesResource(self)

    def attributeGroups(self):
        return AttributeGroupsResource(self)

    def attributeTypes(self):
        return AttributeTypesResource(self)

    def attributeValues(self):
        return AttributeValuesResource(self)

    def products(self):
        return ProductsResource(self)

    def brands(self):
        return BrandsResource(self)

    def options(self):
        return OptionsResource(self)

    def catalogItems(self):
        return CatalogItemsResource(self)

    def entities(self):
        return EntitiesResource(self)

    def entityAttributes(self):
        return EntityAttributesResource(self)

    def media(self):
        return MediaResource(self)

    def mediaTypes(self):
        return MediaTypesResource(self)

    def functionalNames(self):
        return FunctionalNamesResource(self)

    def productAttributeValues(self):
        return ProductAttributeValuesResource(self)

    # Documents
    def documents(self):
        return DocumentsResource(self)

    # Grapher service
    def correlations(self):
        return CorrelationsResource(self)

    def grid(self):
        return GridResource(self)

    # Users service
    def users(self):
        return UsersResource(self)

    def companies(self):
        return CompaniesResource(self)

    def messages(self):
        return MessagesResource(self)

    def wishListItems(self):
        return WishListItemsResource(self)

    # Prices service
    def productPriceConfigurations(self):
        return ProductPriceConfigurationsResource(self)

    # Shop service
    def currencies(self):
        return CurrenciesResource(self)

    def currenciesRate(self):
        return CurrenciesRateResource(self)

    def invoices(self):
        return InvoicesResource(self)

    def orderItems(self):
        return OrderItemsResource(self)

    def deliveryProviders(self):
        return DeliveryProvidersResource(self)

    def paymentMethods(self):
        return PaymentMethodsResource(self)

    def deliveryPayments(self):
        return DeliveryPaymentsResource(self)

    def paymentProviders(self):
        return PaymentProvidersResource(self)

    def vats(self):
        return VatsResource(self)