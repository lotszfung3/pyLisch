from pyLisch import node
from pyLisch.program import Program
programStr='''

(define (get2 )
((define ( plus1 y)(+ 1 y))
(plus1 1 )))
(get2)

(define (square x) (* x x))
(square 6)
(square 3)

(define (multiply x y) (* x y))
(multiply 3 4)

(define (applyTwice f x) (f (f (x))))

'''


program=Program(programStr)

for i in program.run():
	if i:
		print(i)

