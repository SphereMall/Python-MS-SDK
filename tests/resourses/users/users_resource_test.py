from ms_sdk.Entities.User import User
from ms_sdk.Entities.WishListItem import WishListItem
from ms_sdk.Lib.Helpers.Guid import Guid
from ms_sdk.Lib.Specifications.Users.IsUserEmail import IsUserEmail
from ms_sdk.Lib.Specifications.Users.IsUserSubscriber import IsUserSubscriber
from tests.settings import *


class TestUsersResource:

    def testServiceGetList(self):
        users = setup_client().users()
        allUsers = users.all()

        for user in allUsers:
            isinstance(type(user), User)


    def testSubscribeUserIfNotExistOrNotSubscriber(self):
        email = 'ttest@test.com'

        users = setup_client().users()
        user = users.filter(IsUserEmail(email).asFilter()).limit(1).all()

        assert user.email == email
        assert '1' == user.isSubscriber
        # assert users.delete(user.id) - Done

    def testSubscribeUserIfExistAndSubscribe(self):
        email = 'pytqhonTest@test.com'

        users = setup_client().users()
        user = users.create({
            'email': email,
            'isSubscriber': 1
        })

        assert '1' == user.isSubscriber
        assert email == user.email
        assert users.subscribe(email) == None
        assert users.delete(user.id)

    def testUnsubscribeUser(self):
        email = 'qwpythonTest@test.com'

        users = setup_client().users()
        user = users.create({
            'email': email,
            'guid': Guid().Generate(),
            'isSubscriber': 1
        })

        isinstance(type(users.unsubscribe(user.guid)), User)
        assert users.delete(user.id)

    def testUnsubscribeUserIfNotExistOrNotSubscriber(self):
        email = 'qwpythonTest@test.com'

        users = setup_client().users()
        user = users.filter(IsUserEmail(email).asFilter()).limit(1)

        # if user or IsUserSubscriber().isSatisfiedBy(user):
        assert user.unsubscribe('0') == None


    def testUserWishList(self):
        userId = '5'
        productId = '6354'

        allWishs = setup_client().users().getWishList(userId)

        for wish in allWishs:
            isinstance(type(wish), WishListItem)

        # wishListItem = setup_client().users().addToWishList(userId, productId)
        # assert userId == int(wishListItem.userId)
        # assert productId == int(wishListItem.productId)
        #
        # setup_client().users().removeFromWishList(userId, productId)