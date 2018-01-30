from .Entity import Entity
from ms_sdk.Lib.Mixins.InteractsWithProperties import InteractsWithPropertiesMixin


class Document(Entity, InteractsWithPropertiesMixin):

    id = None
    urlCode = None

    attributes = None
    functionalName = None



