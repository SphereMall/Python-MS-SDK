from .Entity import Entity
from ms_sdk.Resourses.Mixins.InteractsWithProperties import InteractsWithPropertiesMixin


class Document(Entity, InteractsWithPropertiesMixin):

    id = None
    urlCode = None

    attributes = None
    functionalName = None



