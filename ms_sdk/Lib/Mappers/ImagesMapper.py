from .Mapper import Mapper
from ms_sdk.Entities.Media import Media

class ImagesMapper(Mapper):

    def doCreateObject(self, array):
        return Media(array)