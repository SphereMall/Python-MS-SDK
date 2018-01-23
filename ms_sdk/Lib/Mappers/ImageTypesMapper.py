from .Mapper import Mapper
from ms_sdk.Entities.MediaType import MediaType

class ImageTypesMapper(Mapper):

    def doCreateObject(self, array):
        return MediaType(array)