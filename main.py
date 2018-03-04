from pyLisch.parser import Parser
from pyLisch.program import Program

s = '''

(define f (lambda(x) (+ 1 x)))
(f 3)
'''

'''
p = Parser(s)
print(p.parse_program())
'''

p = Program(s)
for i in p.run():
	if i is not None:
		print(i)