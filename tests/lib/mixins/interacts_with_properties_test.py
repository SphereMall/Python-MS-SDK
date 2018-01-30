import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from ms_sdk.Entities.Document import Document

class TestInteractsWithProperties:

    def testGetProperty(self):
        pass
        # document = Document({'id' : 1, 'test' : 'test-value'})

        # assert 'test-value' == document.test
        # assert 'test-value' == document.getProperty('test')

        # order = Order({'id' : 1, 'test' : 'test-value'})