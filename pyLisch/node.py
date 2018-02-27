from pyLisch.utils import split_str_to_list
from pyLisch.SymbolTable import SymbolTable
operators=["+","*","-","if","<","="]

class Node:
	def __init__(self,value):#
		self.value=value
		self.eval_value=None
		self.child_list=[]
	def __len__(self):
		return len(self.child_list)
	def __str__(self):
		return "Node: "+str(self.value)
	def __repr__(self):
		return str(self)
		
	def add_child(self,node):
		self.child_list.append(node)
	def isValidNode(string):
		raise NotImplementedError()
	def buildNode(value):#single token
		if PrimNode.isValidNode(value):
			return PrimNode(value)
		elif OperNode.isValidNode(value):
			return OperNode(value)
		else:
			return Node(value)
	def buildTree(string):
		if (" " not in string):
			node=Node.buildNode(string)
			return node
		str_list=split_str_to_list(string)
		temp_node=Node.buildNode(str_list[0])
		for substr in str_list[1:]:
			temp_node.add_child(Node.buildTree(substr))
		return temp_node
	
	def copy(self):
		new_node = Node.buildNode(str(self.value))
		for child in self.child_list:
			new_node.child_list.append(child.copy())
		return new_node

	def eval_node(self,environment):
		if(self.value in environment):
			if(type(environment[self.value]) in [int,float]):#evaluated arguments
				return environment[self.value]
			else:#functions
				local_environment = SymbolTable(environment)
			## Get the function arguments (x,y,z,...) and function body
			fun_args , fun_body = environment[self.value]
			## Build a dict for each arguments in order to replace node in function body
			#assert(len(fun_args) == len(fun_node.child_list[0]))
			for (i,args) in enumerate(fun_args):
				local_environment[args.value] = self.child_list[i].eval_node(environment)
			for fun_b in fun_body:
				if(fun_b.value=="define"):#local functions, register the function
					local_environment[fun_b.child_list[0].value]=(fun_b.child_list[0].child_list,fun_b.child_list[1:])
				else:
					new_node=fun_b.copy()
			return new_node.eval_node(local_environment)

		raise NotImplementedError(self.value)

		
	
class PrimNode(Node):
	def __init__(self,value):
		if("." in value):
			self.value=float(value)
		else:
			self.value=int(value)
		self.child_list=[]
	def eval_node(self,*args):
		return self.value
	def isValidNode(string):
		temp_string=string.replace(".","",1)
		return temp_string.isdigit() or (temp_string[0]=='-' and temp_string[1:].isdigit())
	

class OperNode(Node):
	def __init__(self,value):
		super().__init__(value)
	def eval_node(self,environment):
		if(self.value=="+"):
			return sum([child.eval_node(environment) for child in self.child_list])
		elif(self.value=="*"):
			tempPro=1
			for child in self.child_list:
				tempPro*=child.eval_node(environment)
			return tempPro
		elif(self.value=="-"):
			assert(len(self.child_list)<3)	
			return self.child_list[0].eval_node(environment)-self.child_list[1].eval_node(environment) if len(self.child_list)==2 else -self.child_list[0].eval_node(environment)
		elif(self.value=="if"):
			if(self.child_list[0].eval_node(environment)!=0):# != 0 or True
				return self.child_list[1].eval_node(environment)
			else:
				return self.child_list[2].eval_node(environment)
		elif(self.value=="<"):
			assert(len(self.child_list)==2)
			return self.child_list[0].eval_node(environment)<self.child_list[1].eval_node(environment)
		elif(self.value=="="):
			assert(len(self.child_list)==2)
			return self.child_list[0].eval_node(environment)==self.child_list[1].eval_node(environment)

		raise NotImplementedError(self.value)
	def isValidNode(string):
		return string in operators