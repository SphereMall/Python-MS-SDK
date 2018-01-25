import os
import sys
import urllib.parse
from ms_sdk.Lib.Filters.Grid.AttributeFilter import AttributeFilter
from ms_sdk.Lib.Filters.Grid.FunctionalNameFilter import FunctionalNameFilter
from ms_sdk.Lib.Filters.Grid.GridFilter import GridFilter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from tests.settings import *


class TestGridFilter:
    def testGridFilterSingleElement(self):
        gfe = FunctionalNameFilter([6])

        assert 'functionalNames' == gfe.getName()
        assert [6] == gfe.getValues()


    def testGridFilterElements(self):
        gfe = AttributeFilter([128, 1, 2])

        assert 'attributes' == gfe.getName()
        assert [128, 1, 2] == gfe.getValues()

        gfe = AttributeFilter([1, 3, 5])

        assert 'attributes' == gfe.getName()
        assert [1, 3, 5] == gfe.getValues()
        assert [3, 1, 5] != gfe.getValues()


    def testGridFilter(self):
        attr = AttributeFilter([1, 2, 3])
        assert 'attributes' == attr.getName()
        assert [1, 2, 3] == attr.getValues()

        fn = FunctionalNameFilter([1, 2])
        assert 'functionalNames' == fn.getName()
        assert [1, 2] == fn.getValues()

        ffilter = GridFilter()
        # print(filter.elements([attr]))
        f = ffilter.elements([attr]).elements([fn]).toString()


        print(urllib.parse.unquote_plus(f))
        assert 'params=[{"attributes":[1,2,3]},{"functionalNames":[1,2]}]' == urllib.parse.unquote_plus(f)

