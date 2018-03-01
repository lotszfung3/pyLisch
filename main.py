from pyLisch import node
from pyLisch.program import Program

programStr='''

(define (f x) (+ x x))
(define (g x) (* x x))
(define (ff f g x) (f (g x)))
(ff f g 3)
'''

program=Program(programStr)

for i in program.run():
	print(i)


