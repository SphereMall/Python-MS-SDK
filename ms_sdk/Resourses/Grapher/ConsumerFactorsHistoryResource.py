import json

from ms_sdk.Exceptions.MethodNotFoundException import MethodNotFoundException
from ms_sdk.Resourses import Resource


class ConsumerFactorsHistoryResource(Resource):
    """
    Class MessagesResource
    :method Message get(int id):
    :method Message first():
    :method Message[] all():
    :method Message update(id, data):
    :method Message create(data):
    """

    def getURI(self):
        return 'consumerfactorshistory'

    # def get(self, id: int):
    #     """
    #     :param int id:
    #     :raises MethodNotFoundException:
    #     """
    #     raise MethodNotFoundException('Method get() can not be use with consumer factors')

    def update(self, id: int, data):
        """
        :param int id:
        :param data:
        :raises MethodNotFoundException:
        """
        raise MethodNotFoundException('Method update() can not be use with consumer factors')

    def create(self, data):
        """
        :param data:
        :raises MethodNotFoundException:
        """
        raise MethodNotFoundException('Method create() can not be use with consumer factors')

    def delete(self, id: int):
        """
        :param int id:
        :raises MethodNotFoundException:
        """
        raise MethodNotFoundException('Method delete() can not be use with consumer factors')

    def set(self, userId: int, factors: list, context: dict):
        """
        Set consumer factors for history and for current entity factors
        :see https://spheremall.atlassian.net/wiki/spaces/MIC/pages/1272676386/Grapher+2.3.5+Release+Notes

        :param userId:
        :param factors:
        :param context:
        :return:
        """
        uriAppend = 'set'

        params = [
            ('userId', userId),
            ('factors', json.dumps(factors)),
            ('context', json.dumps(context))
        ]

        response = self.handler.handle('POST', body=params, uriAppend=uriAppend)
        return self.make(response)
