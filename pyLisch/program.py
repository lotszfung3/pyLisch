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
	
	
	def isPrimnode(self,node):
		try: 
			int(node.value)
			return True
		except ValueError:
			return False
		
	def replace_node(self,node,arg_list):
		'''
		node [OperNode:*] with two child Node of value x
		ctx: ["x":3]
		output: [OperNode:*] with two child Node of value 3
		'''
		if node.value in arg_list:
			node.value = arg_list[node.value]
		
		if len(node.child_list) == 0:
			return node
			
		tempNode = Node(node.value)
		for child in node.child_list:
			tempNode.child_list.append(self.replace_node(child, arg_list))
		return tempNode
		
			
	def eval_func(self,fun_name,args):
		fun_args , fun_node = self.def_list[fun_name]
		assert(len(fun_args) == len(args))
		arg_list = {}
		for i in range(len(fun_args)):
			arg_list[fun_args[i].value] = self.eval_node(args[i])
		
		f = self.replace_node(fun_node, arg_list)
		return self.eval_node(f)
		
	
	def eval_node(self,node):
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
				assert (node.child_list[0].value not in self.def_list)
				self.def_list[node.child_list[0].value] = (node.child_list[0].child_list, node.child_list[1])
				return
				
		else:
			assert (node.value in self.def_list)
			if len(node.child_list) == 0:
				return self.eval_node(self.def_list[node.value])
			return self.eval_func(node.value, node.child_list)	
			
			
			
		
	def run(self):
		for node in self.eval_list:
			yield self.eval_node(node)
	