<<<<<<< HEAD
from pyLisch import node
from pyLisch.program import Program
import unittest
class TestOperator(unittest.TestCase):
	def test_plus(self):
		string="(+ 3 4 16)"
		self.assertEqual(next(Program(string).run()),23)
	def test_minus(self):
		string="(- 3 4 )"
		self.assertEqual(next(Program(string).run()),-1)	   
	def test_multiply(self):
		string="(* 3 4 6)"
		self.assertEqual(next(Program(string).run()),72)
	def test_if(self):
		string="(if (> (* 1 6) 5) 6 7)"
		self.assertEqual(next(Program(string).run()),6)
	def test_bin(self):
		string="(if ( or (= 3 5) (> 6 5) ) 5 6)"
		self.assertEqual(next(Program(string).run()),5)
	def test_def(self):
		string='''
		(define pi 3.14)
		(+ 3 pi)
		'''
		self.assertEqual(next(Program(string).run()),6.14)
if __name__=="__main__":
	unittest.main()