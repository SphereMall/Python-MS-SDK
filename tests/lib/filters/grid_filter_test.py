from ms_sdk.Lib.Filters.Grid.AttributeFilter import AttributeFilter
from ms_sdk.Lib.Filters.Grid.BrandFilter import BrandFilter
from ms_sdk.Lib.Filters.Grid.EntityFilter import EntityFilter
from ms_sdk.Lib.Filters.Grid.FactorFilter import FactorFilter
from ms_sdk.Lib.Filters.Grid.FunctionalNameFilter import FunctionalNameFilter
from ms_sdk.Lib.Filters.Grid.GridFilter import GridFilter
from ms_sdk.Lib.Filters.Grid.PriceRangeFilter import PriceRangeFilter


class TestGridFilter:
    def test_grid_filter_single_element(self):
        gfe = FunctionalNameFilter([6])

        assert 'functionalNames' == gfe.getName()
        assert [6] == gfe.getValues()

    def test_grid_filter_elements(self):
        gfe = AttributeFilter([128, 1, 2])

        assert 'attributes' == gfe.getName()
        assert [128, 1, 2] == gfe.getValues()

        gfe = AttributeFilter([1, 3, 5])

        assert 'attributes' == gfe.getName()
        assert [1, 3, 5] == gfe.getValues()
        assert [3, 1, 5] != gfe.getValues()

    def test_grid_filter(self):
        attr = AttributeFilter([1, 2, 3])

        assert 'attributes' == attr.getName()
        assert [1, 2, 3] == attr.getValues()

        fn = FunctionalNameFilter([1, 2])

        assert 'functionalNames' == fn.getName()
        assert [1, 2] == fn.getValues()

        gfilter = GridFilter()

        f = gfilter.elements([attr]).elements([fn]).toString()
        assert '{"attributes":[1,2,3]}' in f \
               and '{"functionalNames":[1,2]}' in f

        gfilter = GridFilter()
        gfilter.reset()
        fl = gfilter.elements([attr, fn]).toString()

        assert '"attributes":[1,2,3]' in fl \
               and '"functionalNames":[1,2]' in fl

        attrs = AttributeFilter([1022])
        gfilter = GridFilter()
        gfilter.reset()
        fl = gfilter.elements([attrs]).toString()

        assert 'params=[{"attributes":[1022]}]' == fl

        ent = EntityFilter(['product'])
        gfilter = GridFilter()
        fl = gfilter.elements([ent]).toString()

        assert 'params=[{"entity":["product"]}]' == fl

        fn = FunctionalNameFilter([5])
        gfilter = GridFilter()
        fl = gfilter.elements([attrs, ent]).elements([fn]).toString()

        assert '"attributes":[1022]' in fl \
               and '"entity":["product"]' in fl \
               and '{"functionalNames":[5]}' in fl

    def test_grid_filter_params(self):
        attr1 = AttributeFilter([1, 2, 3])
        attr2 = AttributeFilter([3, 2, 4])

        assert 'attributes' == attr1.getName()
        assert [1, 2, 3] == attr1.getValues()

        assert 'attributes' == attr2.getName()
        assert [3, 2, 4] == attr2.getValues()

        fn = FunctionalNameFilter([1, 2])

        assert 'functionalNames' == fn.getName()
        assert [1, 2] == fn.getValues()

        attr1 = AttributeFilter([1, 5])

        gfilter = GridFilter()
        f = gfilter.elements([attr1]).elements([fn, attr2]).toString()

        assert 'params=[{"attributes":[1,5]},' in f \
               and '"functionalNames":[1,2]' in f \
               and '"attributes":[3,2,4]' in f

    def test_grid_filter_with_price(self):
        attr = AttributeFilter([1022])

        assert 'attributes' == attr.getName()
        assert [1022] == attr.getValues()

        fn = FunctionalNameFilter([5])

        assert 'functionalNames' == fn.getName()
        assert [5] == fn.getValues()

        br = BrandFilter([1])

        assert 'brands' == br.getName()
        assert [1] == br.getValues()

        price = PriceRangeFilter([10000, 50000])

        assert 'priceRange' == price.getName()
        assert [10000, 50000] == price.getValues()

        gfilter = GridFilter()
        gfilter.reset()
        f = gfilter.elements([attr, fn, br, price]).toString()

        assert '"attributes":[1022]' in f \
               and '"priceRange":[10000,50000]' in f \
               and '"brands":[1]' in f \
               and '"functionalNames":[5]' in f

    def test_grid_filter_with_factors(self):
        attr = AttributeFilter([1022])

        assert 'attributes' == attr.getName()
        assert [1022] == attr.getValues()

        fn = FunctionalNameFilter([5])

        assert 'functionalNames' == fn.getName()
        assert [5] == fn.getValues()

        factor = FactorFilter([1])

        assert 'factors' == factor.getName()
        assert [1] == factor.getValues()

        gfilter = GridFilter()
        gfilter.reset()
        f = gfilter.elements([attr]).elements([fn, factor]).toString()

        assert '"functionalNames":[5]' in f \
               and '"factors":[1]' in f \
               and 'params=[{"attributes":[1022]},' in f

    def test_grid_filter_with_attribute_and_functional_name(self):
        attr = AttributeFilter([1022])

        assert 'attributes' == attr.getName()
        assert [1022] == attr.getValues()

        fn = FunctionalNameFilter([5])

        assert 'functionalNames' == fn.getName()
        assert [5] == fn.getValues()

        entity = EntityFilter(['product'])

        assert 'entity' == entity.getName()
        assert ['product'] == entity.getValues()

        gfilter = GridFilter()
        gfilter.reset()
        f = gfilter.elements([entity, attr]).toString()

        assert '"entity":["product"]' in f \
               and '"attributes":[1022]' in f

    def test_grid_reset(self):
        attr = AttributeFilter([1022])

        assert 'attributes' == attr.getName()
        assert [1022] == attr.getValues()

        fn = FunctionalNameFilter([5])

        assert 'functionalNames' == fn.getName()
        assert [5] == fn.getValues()

        gfilter = GridFilter()

        gfilter.elements([fn, attr])
        assert {0: {'functionalNames': [5], 'attributes': [
            1022]}} == gfilter.getElements()

        gfilter.reset()
        assert not gfilter.getElements()

        gfilter.elements([fn, attr])
        assert {0: {'functionalNames': [5], 'attributes': [
            1022]}} == gfilter.getElements()

        gfilter.reset()
        assert not gfilter.getElements()
