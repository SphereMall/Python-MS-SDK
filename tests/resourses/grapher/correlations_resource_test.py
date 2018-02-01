import pytest

from ms_sdk.Entities.Entity import Entity
from ms_sdk.Entities.Product import Product
from ms_sdk.Exceptions.MethodNotFoundException import MethodNotFoundException
from ms_sdk.Resourses.Grapher.CorrelationsResource import CorrelationsResource
from tests.settings import *


class TestCorrelationsResource:

    def testIsCorrelationResource(self):
        correlations = setup_client().correlations()
        isinstance(type(correlations), CorrelationsResource)

    def testNotAvailableCorrelationsGet(self):
        correlations = setup_client().correlations()
        isinstance(type(MethodNotFoundException), Exception)

        try:
            correlations.get(1)
            assert False
        except:
            assert True

    def testNotAvailableCorrelationsCreate(self):
        correlations = setup_client().correlations()
        isinstance(type(MethodNotFoundException), Exception)

        try:
            correlations.create([])
            assert False
        except:
            assert True

    def testNotAvailableCorrelationsUpdate(self):
        correlations = setup_client().correlations()
        isinstance(type(MethodNotFoundException), Exception)

        try:
            correlations.update(1, [])
            assert False
        except:
            assert True

    def testNotAvailableCorrelationsDelete(self):
        correlations = setup_client().correlations()
        isinstance(type(MethodNotFoundException), Exception)

        try:
            correlations.delete(1)
            assert False
        except:
            assert True

    def testIsProductCorrelations(self):
        correlations = setup_client().correlations().getById(4, 'Product')

        if not correlations:
            assert not correlations
            return

        if type(correlations) == Entity:
            assert True

        for correlation in correlations:
            isinstance(type(correlation), Entity)
