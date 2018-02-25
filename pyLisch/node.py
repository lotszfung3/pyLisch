from pyLisch.utils import split_str_to_list

operators=["+","*","-","if","<"]

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
		
	
class PrimNode(Node):
	def __init__(self,value):
		if("." in value):
			self.value=float(value)
		else:
			self.value=int(value)
		self.child_list=[]
	def eval_node(self):
		return self.value
	def isValidNode(string):
		return string.replace(".","",1).isdigit()
	
class OperNode(Node):
	def __init__(self,value):
		super().__init__(value)
	def eval_node(self,eval_ans):
		if(self.value=="+"):
			return sum(eval_ans)
		elif(self.value=="*"):
			tempPro=1
			for child in eval_ans:
				tempPro*=child
			return tempPro
		elif(self.value=="-"):
			assert(len(eval_ans)<3)	
			return eval_ans[0]-eval_ans[1] if len(eval_ans)==2 else -eval_ans[0]
		elif(self.value=="if"):
			if(eval_ans[0]!=0):# != 0 or True
				return eval_ans[1]
			else:
				return eval_ans[2]
		elif(self.value=="<"):
			assert(len(eval_ans)==2)
			return eval_ans[0]<eval_ans[1]
		raise NotImplementedError
	def isValidNode(string):
		return string in operators