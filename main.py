from pyLisch import Node
from pyLisch.program import Program
programStr='''
(+ pi 3)
'''
node=Node.buildTree(programStr)
new_node=node.copyTree()


