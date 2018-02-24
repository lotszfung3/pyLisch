from pyLisch.utils import split_str_to_list



class Node:
	def __init__(self,value):#
		self.value=value
		self.eval_value=None
		self.child_list=[]
	def __len__(self):
		return len(self.child_list)
	def __str__(self):
		return str(self.value)

		
	def add_child(self,node):
		self.child_list.append(node)
	def isValidNode(string):
		raise NotImplementedError()
	def buildNode(value):#single token
		return Node(value)
		if PrimNode.isValidNode(value):
			return PrimNode(value)
		elif OperNode.isValidNode(value):
			return OperNode(value)
		elif KeywordNode.isValidNode(value):
			return KeywordNode(value)
		else:
			return Node(value)
	def buildTree(string):
		if " " not in string:
			node=Node.buildNode(string)
			return node
		str_list=split_str_to_list(string)
		#print (str_list)
		temp_node=Node.buildTree(str_list[0])
		for substr in str_list[1:]:
			if '(' in substr:
				c = split_str_to_list(substr)
			else:
				c = [substr]
			for x in c:
				temp_node.add_child(Node.buildTree(x))
		return temp_node
	
	def copy(self):
		new_node = Node(self.value)
		for child in self.child_list:
			new_node.child_list.append(child.copy())
		return new_node
		
	
'''
def eval_node(self):
return 0
def copyTree(self,ctx):
'''
'''
copy every single nodes in the tree
'''
'''
new_root=Node.buildNode(self.value)
new_root.add_child([i.copyTree(ctx) for i in self.child_list])
return self
'''

'''

class PrimNode(Node):
	def __init__(self,value):
		self.value=int(value)
		self.child_list=[]
	def eval_node(self):
		return self.value
	def isValidNode(string):
		try: 
			int(string)
			return True
		except ValueError:
			return False
	
class OperNode(Node):
	def __init__(self,value):
		super().__init__(value)
	def eval_node(self):
		if(self.value=="+"):
			return sum([x.eval_node() for x in self.child_list])
		elif(self.value=="*"):
			tempPro=1
			for child in self.child_list:
				tempPro*=child.eval_node()
			return tempPro
	def isValidNode(string):
		return string in operators
'''