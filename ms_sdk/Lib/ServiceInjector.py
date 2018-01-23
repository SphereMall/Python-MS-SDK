from ms_sdk.Resourses.Products import (ProductsResource,
                                       AttributeDisplayTypesResource,
                                       AttributeGroupsEntitiesResource,
                                       AttributeGroupsResource,
                                       AttributesResource)


class ServiceInjectorMixin:

    # products service
    # def attributeDisplayTypes(self):
    # return AttributeDisplayTypesResource(self)

    def attributeDisplayTypes(self):
        return AttributeDisplayTypesResource(self)

    def attributeGroupsEntities(self):
        return AttributeGroupsEntitiesResource(self)

    def attributeGroups(self):
        return AttributeGroupsResource(self)

    def products(self):
        return ProductsResource(self, self)

    def attributes(self):
        return AttributesResource(self)