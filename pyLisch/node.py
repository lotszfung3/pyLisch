from pyLisch.utils import split_str_to_list
from pyLisch.SymbolTable import SymbolTable
operators=["+","*","-","=", "<", ">", "<=", ">=", "and", "or", "not"]
keywords = [ "if", "define"]

class Node:
	def __init__(self,value):#
		self.value=value
		self.eval_value=None
		self.child_list=[]
	def __len__(self):
		return len(self.child_list)
	def __str__(self):
		return "Node: "+str(self.value) + str(self.child_list)
	
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
		elif KeyNode.isValidNode(value):
			return KeyNode(value)
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
	
	def replace_node(self,env):	
		if self.value in env:
			new_node = Node.buildNode(str(env[self.value]))
			new_node.child_list = self.child_list
		else:
			new_node = self.copy()
		
		for i, child in enumerate(self.child_list):
			new_node.child_list[i] = child.replace_node(env)
		
		return new_node

	def eval_node(self,env):
		if(self.value in env):
			if(type(env[self.value]) in [int,float]):#evaluated arguments
				return env[self.value]
			else:#functions
				local_env = SymbolTable(env)
				## Get the function arguments (x,y,z,...) and function body
				fun_args , fun_body = env[self.value]
				
				d = {}			
				if any([len(env[child.value][0]) != len(child.child_list) for child in self.child_list if child.value in env]):				
					#if function is passed as argument, then replace node, build the tree and evaluate the expression			
					for (i,args) in enumerate(fun_args):
						d[args.value] = self.child_list[i].value 
				else:
					## Build a dict for each arguments in order to replace node in function body
					assert(len(fun_args) == len(self.child_list))
					for (i,args) in enumerate(fun_args):
						local_env[args.value] = self.child_list[i].eval_node(env)
						
				for fun_b in fun_body:
					if len(d) > 0:
						fun_b = fun_b.replace_node(d)
					result = fun_b.eval_node(local_env)
				return result

		raise NotImplementedError(self.value)
		
class KeyNode(Node):
	def __init__(self,value):
		super().__init__(value)
	
	def eval_node(self,env):
		if self.value == 'if':
			assert (2 <= len(self.child_list) <= 3)
			if(self.child_list[0].eval_node(env)!=0):# != 0 or True
				return self.child_list[1].eval_node(env)
			elif len(self.child_list) == 3:
				return self.child_list[2].eval_node(env)
		elif self.value == 'define':
			env[self.child_list[0].value]=(self.child_list[0].child_list,self.child_list[1:])
			
	
	def isValidNode(string):
		return string in keywords

class OperNode(Node):
	def __init__(self,value):
		super().__init__(value)
		
	def eval_node(self,env):
		if(self.value=="+"):
			return sum([child.eval_node(env) for child in self.child_list])
		elif(self.value=="*"):
			tempPro=1
			for child in self.child_list:
				tempPro*=child.eval_node(env)
			return tempPro
		elif(self.value=="-"):
			assert(len(self.child_list)> 0)	
			if len(self.child_list)==1:
				return -self.child_list[0].eval_node(env)
			else:
				return self.child_list[0].eval_node(env) - sum([child.eval_node(env) for child in self.child_list[1:]])
		
		elif (self.value == "not"):
			assert (len(self.child_list) == 1)
			return not(self.child_list[0].eval_node(env))
		
		elif (self.value == "and"):
			assert (len(self.child_list) >= 1)
			return all([child.eval_node(env) for child in self.child_list])

		elif (self.value == "or"):
			assert (len(self.child_list) >= 1)
			return any([child.eval_node(env) for child in self.child_list])
		
		elif(self.value=="<"):
			assert(len(self.child_list)>=2)
			res = [self.child_list[0].eval_node(env)]
			for i in range(len(self.child_list)-1):
				res.append(self.child_list[i+1].eval_node(env))
				if res[i] >= res[i+1]:
					return False
			return True
		
		elif(self.value=="<="):
			assert(len(self.child_list)>=2)
			res = [self.child_list[0].eval_node(env)]
			for i in range(len(self.child_list)-1):
				res.append(self.child_list[i+1].eval_node(env))
				if res[i] > res[i+1]:
					return False
			return True
				
		elif(self.value=="="):
			assert(len(self.child_list)>=2)
			res = [self.child_list[0].eval_node(env)]
			for i in range(len(self.child_list)-1):
				res.append(self.child_list[i+1].eval_node(env))
				if res[i] != res[i+1]:
					return False
			return True
			
		elif(self.value==">"):
			assert(len(self.child_list)>=2)
			res = [self.child_list[0].eval_node(env)]
			for i in range(len(self.child_list)-1):
				res.append(self.child_list[i+1].eval_node(env))
				if res[i] <= res[i+1]:
					return False
			return True
			
		elif(self.value==">="):
			assert(len(self.child_list)>=2)
			res = [self.child_list[0].eval_node(env)]
			for i in range(len(self.child_list)-1):
				res.append(self.child_list[i+1].eval_node(env))
				if res[i] < res[i+1]:
					return False
			return True

		raise NotImplementedError(self.value)
	def isValidNode(string):
		return string in operators
		
		
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