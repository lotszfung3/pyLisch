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
			
			
	def run(self):
		for node in self.eval_list:
			answer=node.eval_node(self.global_table)
			if (isinstance(answer,float)):
				yield str(round(answer,2))
			else:
				yield answer
	