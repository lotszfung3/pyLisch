from pyLisch.node import Node,PrimNode,OperNode
from pyLisch.utils import split_str_to_list
from pyLisch.SymbolTable import SymbolTable


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
			self.global_table = SymbolTable()
		#add all global function to global_table
		for node in self.def_list:
			self.global_table[node.child_list[0].value] = (node.child_list[0].child_list,node.child_list[1:])
	
		
	def replace_node(self,node,arg_list):
		'''
		node [OperNode:*] with two child Node of value x
		ctx: ["x":3]
		output: [OperNode:*] with two child Node of value 3
		'''
		assert(False)
		if node.value in arg_list:
			node.value = arg_list[node.value]
		
		if len(node.child_list) == 0:
			return node
			
		tempNode = Node(node.value)
		for child in node.child_list:
			tempNode.child_list.append(self.replace_node(child, arg_list))
		return tempNode
		
			
	def eval_func(self, node, table):
		'''
		evaluate a function
		Parameters:
			- node: the node with value of the function name
			- table: the look-up table of variable
		Return:
			- return value of the function
		'''
		## local-level symbol table		
		local_table = SymbolTable(table)

		## Get the function arguments (x,y,z,...) and function body
		fun_args , fun_body = table[node.value]
		## Build a dict for each arguments in order to replace node in function body
		#assert(len(fun_args) == len(fun_node.child_list[0]))
		for (i,args) in enumerate(fun_args):
			local_table[args.value] = self.eval_node(node.child_list[i], self.global_table)
		for fun_b in fun_body:
			if(fun_b.value=="define"):#local functions, register the function
				
				local_table[fun_b.child_list[0].value]=(fun_b.child_list[0].child_list,fun_b.child_list[1:])
			else:
				return self.eval_node(fun_b.copy(), local_table)
		assert(False)
	
	def eval_node(self,node, table):
		'''
		Parameters:
			- node: current node to be evaluated
			- table: symbol table for checking		
		'''
		#print (node.value)
		if isinstance(node,PrimNode):
			return node.eval_node()
			
		elif isinstance(node,OperNode):
			return node.eval_node([self.eval_node(child, table) for child in node.child_list])
			
				
		elif node.value in table:
			## Evaluate defined constants and functions
			if(type(table[node.value]) in [int,float]):#evaluated arguments
				return table[node.value]
			else:
				return self.eval_func(node, table)	
					
		
	def run(self):
		for node in self.eval_list:
			answer=self.eval_node(node, self.global_table)
			if (isinstance(answer,float)):
				yield str(round(answer,2))
			else:
				yield answer
	