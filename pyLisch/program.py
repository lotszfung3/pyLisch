from pyLisch.node import Node,PrimNode,OperNode
from pyLisch.SymbolTable import SymbolTable
from pyLisch.parser import Parser


class Program:
	def __init__(self,string):
		self.parser = Parser(string)
		self.eval_list= self.parser.parse_program()
		self.global_table = SymbolTable()

			
	def run(self):
		for node in self.eval_list:
			answer=node.eval_node(self.global_table)
			if answer is not None:
				if (isinstance(answer,float)):
					yield round(answer,2)
				else:
					yield answer
		