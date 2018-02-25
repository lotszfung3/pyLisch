from pyLisch import node
from pyLisch.program import Program
programStr='''
(if (< 3 (+ 5 4)) 5 4)
'''

program=Program(programStr)
for i in program.eval_list[0].child_list:
	print(i)
for i in program.run():
	if i:
		print("Ans:",i)

