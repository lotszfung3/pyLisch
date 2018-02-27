from pyLisch import node
from pyLisch.program import Program
programStr='''
(define (fact x) (if (= x 1) 1 (* x (fact (- x 1)))))
(fact 4)
'''

program=Program(programStr)

for i in program.run():
	if i:
		print(i)


