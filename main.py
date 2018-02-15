from pyLisch import node
from pyLisch.program import Program
programStr='''
(define (square x) (* x x) )
(square 3)


'''


program=Program(programStr)

for i in program.run():
	if i:
		print(i)

