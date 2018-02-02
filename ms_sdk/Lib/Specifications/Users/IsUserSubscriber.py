from ms_sdk.Lib.Filters.FilterOperators import FilterOperators
from ms_sdk.Lib.Specifications.Basic.FilterSpecification import FilterSpecification
from ms_sdk.Lib.Specifications.Users.UserSpecification import UserSpecification


class IsUserSubscriber(FilterSpecification, UserSpecification):

    def asFilter(self):
        return {'isSubscriber': {FilterOperators.EQUAL: 1 }}

    def isSatisfiedBy(self, user):
        return user.id and user.isSubscriber