from ms_sdk.Lib.Makers.ObjectMaker import ObjectMaker
from ms_sdk.Lib.Mappers.FacetAttributesMapper import FacetAttributesMapper


class FacetsMaker(ObjectMaker):

    def makeSingle(self, response):
        if not response.getSuccess():
            return None

        result = {}
        data = response.getData()

        for type, items in data.items():
            if type == 'attributes':
                mapper = FacetAttributesMapper()
                result['attributes'] = mapper.createObject(items)
            elif type == 'priceRange':
                result['priceRange'] = items

        return result