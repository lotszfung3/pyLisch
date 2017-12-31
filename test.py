from src import Manager
from src import utils
import unittest
class TestBasicOperator(unittest.TestCase):
    def test_plus(self):
        run_str="(+ 3 4 16)"
        Manager.run(run_str)
    def test_minus(self):
        run_str="(- 3 4 )"
        Manager.run(run_str)        
    def test_multiply(self):
        run_str="(* 3 4 6)"
        Manager.run(run_str)
        
if __name__=="__main__":
    unittest.skip("oper")
    unittest.main()