from ms_sdk.Lib.Makers.ObjectMaker import ObjectMaker


class CountMaker(ObjectMaker):
    def makeSingle(self, response):
        if not response.getSuccess():
            return 0

        data = response.getData()
        try:
            item = self.getAttributes(data[0])
            return int(item['count'])
        except:
            return 0