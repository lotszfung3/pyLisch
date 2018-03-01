from pyLisch.node import Node,PrimNode,OperNode
from pyLisch.utils import split_str_to_list
from pyLisch.SymbolTable import SymbolTable


class Program:
	def __init__(self,string):
		self.eval_list=[]
		self.def_list=[]
		self.global_table = SymbolTable()
		for substr in split_str_to_list(string):
			node=Node.buildTree(substr)
			self.eval_list.append(node)

			
	def run(self):
		for node in self.eval_list:
			answer=node.eval_node(self.global_table)
			if answer is not None:
				if (isinstance(answer,float)):
					yield round(answer,2)
				else:
					yield answer
		