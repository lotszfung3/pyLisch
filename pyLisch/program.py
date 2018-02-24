from pyLisch.node import Node
from pyLisch.utils import split_str_to_list
from pyLisch.SymbolTable import SymbolTable


operators = ["+","*"]
keywords = ["define"]

class Program:
	eval_list=[]
	def __init__(self,string):
		for substr in split_str_to_list(string):
			node=Node.buildTree(substr)
			self.eval_list.append(node)
			self.global_table = SymbolTable()
	
	
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
		for defNode in self.table:
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
		
			
	def eval_func(self, func, table):
		## local-level symbol table		
		local_table = SymbolTable(table)
		
		## Get the function arguments (x,y,z,...) and function body
		fun_args , fun_body = table[func.value]
		
		## Build a dict for each arguments in order to replace node in function body
		#assert(len(fun_args) == len(fun_node.child_list[0]))
		arg_list = {}
		for i in range(len(fun_args)):
			arg_list[fun_args[i].value] = self.eval_node(func.child_list[i], local_table)
		
		## Evaluate each statement in the function body
		for x in fun_body:
			x = x.copy()
			f = self.replace_node(x, arg_list)
			result = self.eval_node(f, local_table)
			
		return result
		
		
	
	def eval_node(self,node, table):
		'''
		Parameters:
			- node: current node to be evaluated
			- table: symbol table for checking		
		'''
		#print (node.value)
		if self.isPrimnode(node):
			return int(node.value)
			
		elif node.value in operators:
			if (node.value=="+"):
				return sum([self.eval_node(child, table) for child in node.child_list])
			elif(node.value=="*"):
				tempPro=1
				for child in node.child_list:
					tempPro*=self.eval_node(child, table)
				return tempPro
				
		elif node.value in keywords:
			if node.value == "define":
				#assert (node.child_list[0].value not in self.def_list)
				
				table[node.child_list[0].value] = (node.child_list[0].child_list,node.child_list[1:])
				#print (table.curr)
				return
				
		elif node.value in table:
			## Evaluate defined constants and functions
			return self.eval_func(node, table)	
			
			
			
		
	def run(self):
		for node in self.eval_list:
			yield self.eval_node(node, self.global_table)
	