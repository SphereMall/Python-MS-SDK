from ms_sdk.Resourses.Products import ProductsResource


class ServiceInjectorMixin:

    # Products service
    # def attributeDisplayTypes(self):
    # return AttributeDisplayTypesResource(self)

    def products(self):
        return ProductsResource(self, self)
