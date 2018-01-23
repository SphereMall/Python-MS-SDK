from .Mapper import Mapper
from .AttributesMapper import AttributesMapper

class ProductAttributeValuesMapper(Mapper):

    def doCreateObject(self, array):
        raw = {}
        # print(array)
        i = 0
        for item in array.values():
            i += 1
            raw.update({str(i) : {
                item.get('attributeId') : {
                    'id' : item.get('attributeId'),
                    'title' : item.get('title'),
                    'code' : item.get('code'),
                    'showInSpecList' : item.get('showInSpecList'),
                    'description' : item.get('description'),
                    'attributeGroupId' : item.get('attributeGroupId'),
                    'cssClass' : item.get('cssClass'),

                    'attributeValues': {
                        'id' : item.get('id'),
                        'value' : item.get('value'),
                        'title' : item.get('valueTitle'),
                        'cssClass': item.get('valueCssClass')
                    }
                }
            }})

        mapper = AttributesMapper()
        result = []
        for item in raw.values():
            result.append(mapper.createObject(item.get(list(item)[0])))

        return result