from pyLisch import node
from pyLisch.program import Program
programStr='''
(define (square x) (* x x) )
(define pi 3)
(+ pi 1)
'''


program=Program(programStr)

for i in program.run():
	print(i)

