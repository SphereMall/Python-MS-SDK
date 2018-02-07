from ms_sdk.Entities.Entity import Entity
from ms_sdk.Exceptions.MethodNotFoundException import MethodNotFoundException
from ms_sdk.Resourses.Grapher.CorrelationsResource import CorrelationsResource
from tests.settings import *


class TestCorrelationsResource:

    def test_is_correlation_resource(self):
        correlations = setup_client().correlations()
        isinstance(type(correlations), CorrelationsResource)

    def test_not_available_correlations_get(self):
        correlations = setup_client().correlations()
        isinstance(type(MethodNotFoundException), Exception)

        try:
            correlations.get(1)
            assert False
        except:
            assert True

    def test_not_available_correlations_create(self):
        correlations = setup_client().correlations()
        isinstance(type(MethodNotFoundException), Exception)

        try:
            correlations.create([])
            assert False
        except:
            assert True

    def test_not_available_correlations_update(self):
        correlations = setup_client().correlations()
        isinstance(type(MethodNotFoundException), Exception)

        try:
            correlations.update(1, [])
            assert False
        except:
            assert True

    def test_not_available_correlations_delete(self):
        correlations = setup_client().correlations()
        isinstance(type(MethodNotFoundException), Exception)

        try:
            correlations.delete(1)
            assert False
        except:
            assert True

    def test_is_product_correlations(self):
        correlations = setup_client().correlations().getById(4, 'Product')

        if not correlations:
            assert not correlations
            return

        if type(correlations) == Entity:
            assert True

        for correlation in correlations:
            isinstance(type(correlation), Entity)
