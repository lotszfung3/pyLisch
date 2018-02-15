from pyLisch.node import Node,PrimNode,OperNode
from pyLisch.utils import split_str_to_list
class Program:
	def __init__(self,string):
		self.eval_list=[]
		self.def_list=[]
		for substr in split_str_to_list(string):
			node=Node.buildTree(substr)
			if(node.value=="define"):
				self.def_list.append(node)
			else:
				self.eval_list.append(node)
				
	def replace_node(self,node):
		'''
		replace every single variable node in eval_list
		'''
		for i in self.eval_list:
			pass
			
	def get_func_node(self,name,arg_list):
		'''
		get new node
		input: name=sq, arg_list=[PrimNode:3]
		output: [OperNode:*] with two PrimNode children of value 3 
		'''
		for defNode in self.def_list:
			if str(defNode.child_list[0])==name:
				assert len(arg_list)==len(defNode.child_list[1])
				new_node=defNode.child_list[1].copyTree()# OperNode:*
		return new_node
	def replace_node(self,node,ctx):
		'''
		node [OperNode:*] with two child Node of value x
		ctx: ["x":3]
		output: [OperNode:*] with two child Node of value 3
		'''
		for i,n in enumerate(node.child_list):
			pass
		
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
	