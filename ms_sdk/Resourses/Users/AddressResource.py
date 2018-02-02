from pip._vendor.distlib.resources import Resource


class AddressResource(Resource):

    def getURI(self):
        return 'addresses'