from .Entity import Entity
from ms_sdk.Resourses.Mixins.InteractsWithProperties import InteractsWithPropertiesMixin

class Product(Entity, InteractsWithPropertiesMixin):

    id = None
    urlCode = None
    title = None
    shortDescription = None
    fullDescription = None
    seoTitle = None
    seoDescription = None
    seoKeywords = None
    visible = None
    purchasePrice = None
    price = None
    oldPrice = None
    importedId = None
    variantsCompound = None

    attributes = None
    brand = None
    functionalName = None

    media = []
    mainMedia = None