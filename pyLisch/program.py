from pyLisch.node import Node
from pyLisch.utils import split_str_to_list


operators = ["+","*"]
keywords = ["define"]

class Program:
	eval_list=[]
	def_list={}
	def __init__(self,string):
		for substr in split_str_to_list(string):
			node=Node.buildTree(substr)
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
		
	def isPrimnode(self,node):
		try: 
			int(node.value)
			return True
		except ValueError:
			return False
	
	def eval_node(self,node):
		print (node.value)
		if self.isPrimnode(node):
			return int(node.value)
			
		elif node.value in operators:
			if (node.value=="+"):
				return sum([self.eval_node(child) for child in node.child_list])
			elif(node.value=="*"):
				tempPro=1
				for child in node.child_list:
					tempPro*=self.eval_node(child)
				return tempPro
				
		elif node.value in keywords:
			if node.value == "define":
				if node.value in self.def_list:
					raise "Redefinition???"
				self.def_list[node.child_list[0].value] = node.child_list[1]
				
		else:
			if node.value in self.def_list:
				return self.eval_node(self.def_list[node.value])
			
			
			
			
		'''
		elif node.value in self.def_list:
			return self.def_list[node.value]child_list[1].eval_node()
		assert(False)   
		'''
		
	def run(self):
		for node in self.eval_list:
			yield self.eval_node(node)
	