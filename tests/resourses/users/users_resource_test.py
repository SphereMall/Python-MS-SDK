from ms_sdk.Entities.User import User
from ms_sdk.Entities.WishListItem import WishListItem
from ms_sdk.Lib.Helpers.Guid import Guid
from ms_sdk.Lib.Specifications.Users.IsUserEmail import IsUserEmail
from ms_sdk.Lib.Specifications.Users.IsUserSubscriber import IsUserSubscriber
from tests.settings import *


class TestUsersResource:

    def test_service_get_list(self):
        users = setup_client().users()
        allUsers = users.all()

        for user in allUsers:
            isinstance(type(user), User)

    def test_subscribe_user_if_not_exist_or_not_subscriber(self):
        email = 'test_unique@test.com'

        users = setup_client().users()
        user = users.filter(IsUserEmail(email).asFilter()).limit().all()

        assert user.email == email
        assert '0' == user.isSubscriber
        # assert users.delete(user.id)

    def test_subscribe_user_if_exist_and_subscribe(self):
        email = 'pytq33st@test.com'

        users = setup_client().users()
        user = users.create({
            'email': email,
            'isSubscriber': 1
        })

        assert '1' == user.isSubscriber
        assert email == user.email
        assert users.subscribe(email) == None
        assert users.delete(user.id)

    def test_unsubscribe_user(self):
        email = 'qwpythonTe2st@test.com'

        users = setup_client().users()
        user = users.create({
            'email': email,
            'guid': Guid().Generate(),
            'isSubscriber': 1
        })

        isinstance(type(users.unsubscribe(user.guid)), User)
        assert users.delete(user.id)

    def test_unsubscribe_user_if_not_exist_or_not_subscriber(self):
        email = 'qwpythonTest@test.com'

        users = setup_client().users()
        user = users.filter(IsUserEmail(email).asFilter()).limit()

        assert user.unsubscribe('0') == None

    def test_user_wish_list(self):
        userId = 5
        productId = get_prod().id

        allWishs = setup_client().users().getWishList(userId)

        for wish in allWishs:
            isinstance(type(wish), WishListItem)

        wishListItem = setup_client().users().addToWishList(userId, productId)

        assert userId == int(wishListItem.userId)
        assert productId == int(wishListItem.productId)

        setup_client().users().removeFromWishList(userId, productId)

