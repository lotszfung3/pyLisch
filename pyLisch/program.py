from pyLisch.node import Node,PrimNode,OperNode
from pyLisch.utils import split_str_to_list
class Program:
	def __init__(self,string):
		self.eval_list=[]
		self.def_list=[]
		for substr in split_str_to_list(string):
			node=Node.buildTree(substr,self)
			print (substr)
			if(node.value=="define"):			
				self.def_list.append(node)
			else:
				self.eval_list.append(node)
	def eval_node(self,node):
		'''
		input:
			node: node to be replaced
		output:
			node created by node.value
		'''

		for defNode in self.def_list:
			if (defNode.child_list[0].value==node.value):
				assert(len(defNode.child_list[0])==len(node.child_list))
				return defNode.child_list[1].eval_node()
		assert(False)
	def run(self):
		for i in self.eval_list:
			yield round(i.eval_node(),8)
		
		
	