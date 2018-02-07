from ms_sdk.Entities.Document import Document
from ms_sdk.Entities.Entity import Entity
from ms_sdk.Entities.Product import Product
from ms_sdk.Lib.Filters.Grid.EntityFilter import EntityFilter
from ms_sdk.Lib.Filters.Grid.GridFilter import GridFilter
from ms_sdk.Lib.Http.Meta import Meta
from tests.settings import *


class TestGridResource:

    def test_service_get_list(self):
        all = setup_client().grid().all()

        for item in all:
            isinstance(type(item), Entity)

    def test_grid_filter(self):
        gFilter = GridFilter()
        gFilter.elements([EntityFilter(['product'])])

        isinstance(type(gFilter), GridFilter)

        grid = setup_client().grid().filter(gFilter).all()

        for item in grid:
            isinstance(item, Product)

        gFilter = GridFilter()
        gFilter.elements([EntityFilter(['document'])])
        grid = setup_client().grid().filter(gFilter).all()

        for item in grid:
            isinstance(type(item), Document)

    def test_grid_count(self):
        gFilter = GridFilter()
        gFilter.elements([EntityFilter(['product'])])

        amount = setup_client().grid().filter(gFilter).count()
        assert 0 < amount

    def test_service_get_with_meta(self):
        all = setup_client().grid().withMeta().all()
        isinstance(type(all.getMeta()), Meta)

        try:
            for item in all:
                isinstance(type(item), Entity)
        except:
            isinstance(type(all), Entity)

    def test_grid_facets(self):
        all = setup_client().grid().facets()

        for items in all:
            for item in items:
                if isinstance(item, object):
                    isinstance(type(item), Entity)