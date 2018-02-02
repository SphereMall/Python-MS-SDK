from ms_sdk.Entities.User import User
from ms_sdk.Lib.Filters.FilterOperators import FilterOperators
from ms_sdk.Lib.Helpers.Guid import Guid
from ms_sdk.Lib.Specifications.Users.IsUserEmail import IsUserEmail
from ms_sdk.Lib.Specifications.Users.IsUserSubscriber import IsUserSubscriber
from ms_sdk.Resourses import Resource


class UsersResource(Resource):

    def getURI(self):
        return 'users'

    def subscribe(self, email, name=''):
        userList = self.filter(IsUserEmail(email).asFilter()).limit(1).all()

        user = userList or User({
            'email': email,
            'name': name,
            'guid': Guid.Generate(),
            'isSubscriber': 1
        })

        if IsUserSubscriber().isSatisfiedBy(user):
            return None

        if user.id:
            return self.update(user.id, {'isSubscriber': 1})

        return self.create(user)

    def unsubscribe(self, guid):
        userList = self.fields(['isSubscriber']).filter({'guid': {FilterOperators.EQUAL: guid}}).limit(1).all()

        try:
            return self.update(userList.id, {'isSubscriber': 0})
        except:
            return None

    def getWishList(self, userId):
        response = self.handler.handle('GET', False, 'wishlist/' + str(userId))
        return self.make(response, True)