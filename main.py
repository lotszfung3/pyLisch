from pyLisch import node
from pyLisch.program import Program
programStr='''
(define pi 4) 
(+ pi 3)
'''
program=Program(programStr)

for i in program.run():
    print(i)

