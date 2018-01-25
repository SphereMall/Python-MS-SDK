from .FilterOperators import FilterOperators
from .FilterConditions import FilterConditions

class Filter(FilterOperators, FilterConditions):
    availableFilters = {
        FilterOperators.LIKE,
        FilterOperators.LIKE_LEFT,
        FilterOperators.LIKE_RIGHT,
        FilterOperators.EQUAL,
        FilterOperators.NOT_EQUAL,
        FilterOperators.GREATER_THAN,
        FilterOperators.LESS_THAN,
        FilterOperators.GREATER_THAN_OR_EQUAL,
        FilterOperators.LESS_THAN_OR_EQUAL,
        FilterOperators.IS_NULL
    }

    filters = {}

    def __init__(self, filters = {}):
        if filters:
            self.setFilters(filters)



    def getFilters(self, filters):
        return self.filters


    def setFilters(self, filters):
        print(filters)
        for (field, rules) in enumerate(filters):
            print('-------- First for A --------')
            if field == 'fullSearch':
                print('-------- First for B --------')
                self.addFilter(field, rules, None)
                continue

            for (operator, value) in enumerate(rules):
                print('-------- Second for A --------')
                print(rules[operator])
                if (not operator in self.availableFilters) or ((not value) and value != '0'):
                    print('-------- Second for B --------')
                    continue
                self.addFilter(field, value, operator)
        return self

    def addFilter(self, field, value, operator):
        print('-------- BBBBB --------')
        if field and (value or value == '0'):
            if operator == None:
                self.filters[field][operator] = value
            else:
                print(self.filters)
                self.filters[field] = value

        return self
