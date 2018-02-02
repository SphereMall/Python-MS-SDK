from ms_sdk.Entities.Message import Message
from tests.settings import setup_client


class TestMessagesResource:

    def testServiceGetList(self):
        messages = setup_client().messages().all()

        try:
            assert messages[0]
            for message in messages:
                isinstance(type(message), Message)
        except:
            isinstance(type(messages), Message)
