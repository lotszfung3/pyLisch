from pyLisch import node
from pyLisch.program import Program
programStr='''
(define get2
(define (plus1 y)(+ 1 y))
( plus1 1 ))
(get2)
'''

program=Program(programStr)

for i in program.run():
	if i:
		print(i)


