import hw6_heathrow as heath
import numpy as np

class TestSample:
    """
    Autograder - *DO NOT* alter this file
    It tests if your functions are working as expected.
    """
    a = np.array([0, 100])
    b = np.array([32, 212])
    
    def test_average(self):
        """
        Test Average
        """
        assert heath.average(0,1) == 0.5 , "should work with regular numbers"
        assert isinstance(heath.average(self.a,self.a), np.ndarray) , "should work with ndarrays"
        assert np.array_equal(heath.average(self.a,self.a), self.a) , "average of the same ndarray should be same"
        assert np.array_equal(heath.average(self.a,self.b), np.array([16,156])) , "check your average"
        
    def test_ftoc(self):
        """
        Test Fahrenheit
        """
        assert heath.fToC(212) == 100 , "should work with regular numbers"
        assert isinstance(heath.fToC(self.b), np.ndarray) , "should work with ndarrays"
        assert np.array_equal(heath.fToC(self.b), self.a) , "check your math"

    def test_ctof(self):
        """
        Test Celcius
        """
        assert heath.cToF(100) == 212 , "should work with regular numbers"
        assert isinstance(heath.cToF(self.a), np.ndarray) , "should work with ndarrays"
        assert np.array_equal(heath.cToF(self.a), self.b) , "check your math"
