from ms_sdk.Resourses.Products import (ProductsResource,
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
                                       OptionsResource)


class ServiceInjectorMixin:

    def attributes(self):
        return AttributesResource(self)

    def attributeDisplayTypes(self):
        return AttributeDisplayTypesResource(self)

    def attributeGroupsEntities(self):
        return AttributeGroupsEntitiesResource(self)

    def attributeGroups(self):
        return AttributeGroupsResource(self)

    def attributeTypes(self):
        return AttributeTypesResource(self)

    def attributeValues(self):
        return AttributeValuesResource(self)

    def products(self):
        return ProductsResource(self, self)

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
