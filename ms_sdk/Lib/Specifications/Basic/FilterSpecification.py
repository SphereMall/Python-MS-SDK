from ms_sdk.Lib.Filters.FilterOperators import FilterOperators


class FilterSpecification:

    def asFilter(self):
        return {'visible': {FilterOperators.EQUAL: 1}}