from ms_sdk.Lib.Mappers.AttributesMapper import AttributesMapper
from ms_sdk.Lib.Mappers.FunctionalNamesMapper import FunctionalNamesMapper
from .Mapper import Mapper
from ms_sdk.Entities.Document import Document


class DocumentsMapper(Mapper):

    def doCreateObject(self, array):
        document = Document(array)

        try:
            if array.get('attributes'):
                document.attributes = []
                mapper = AttributesMapper()

                for attribute in array.get('attributes').items():
                    document.attributes.append(mapper.createObject(attribute[1]))
        except:
            pass

        try:
            if array.get('functionalNames'):
                mapper = FunctionalNamesMapper()
                document.functionalName = mapper.createObject(array.get('functionalNames').get(list(array.get('functionalNames'))[0]))
        except:
            pass

        return document
