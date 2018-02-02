from ms_sdk.Entities.WishListItem import WishListItem
from tests.settings import setup_client


class TestWishListItemsResource:

    def testServiceGetList(self):
        wishList = setup_client().wishListItems().all()

        try:
            assert wishList[0]
            for wish in wishList:
                isinstance(type(wish), WishListItem)
        except:
            isinstance(type(wishList), WishListItem)
