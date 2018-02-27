from pyLisch import node
from pyLisch.program import Program
import unittest
class TestOperator(unittest.TestCase):
	def test_plus(self):
		string="(+ 3 4 16)"
		self.assertEqual(next(Program(string).run()),23)
	def test_minus(self):
		string="(- 6 4)"
		self.assertEqual(next(Program(string).run()),2)
	def test_nested_if(self):
		string="(if (< 5 (* 3 2)) 5 6)"
		self.assertEqual(next(Program(string).run()),5)
class TestDefine(unittest.TestCase):
	def test_constant(self):
		string='''
		(define pi 3.14)
		(+ pi 4)
		'''
		self.assertEqual(next(Program(string).run()),'7.14')
	def test_functions(self):
		string='''
		(define (square x)(* x x))
		(square 3)
		'''
		self.assertEqual(next(Program(string).run()),9)
	def test_multi_arg_funct(self):
		string='''
		(define (product_ x y)(* x y))
		(product_ 3 4)
		'''
		self.assertEqual(next(Program(string).run()),12)
	def test_nested_funct(self):
		string='''
		(define get2
		(define (plus1 y)(+ 1 y))
		( plus1 1 ))
		(get2)'''
		self.assertEqual(next(Program(string).run()),2)
	def test_neg_compare_funct(self):
		string='''
		(define (Pos x) (if (< 0 x) 1 -1))
		(Pos -1)
		'''
		self.assertEqual(next(Program(string).run()),-1)
	def test_nested_if_funct(self):
		string='''
		(define (comp x)(if (= x 1) (5) (if (= x 2) 3 4)))
		(comp 2)
		'''
		self.assertEqual(next(Program(string).run()),3)
	def test_recursion_funct(self):
		string='''
		(define (fact x) (if (= x 1) 1 (* x (fact (- x 1)))))
		(fact 4)
		'''
		self.assertEqual(next(Program(string).run()),24)
class TestUtil(unittest.TestCase):
	def test_strange_brackets_indent(self):
		string='''
		(define (square x)	(* x x))
		(square     (3))
		'''
		self.assertEqual(next(Program(string).run()),9)
if __name__=="__main__":
	unittest.main()