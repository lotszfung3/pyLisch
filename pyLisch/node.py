from pyLisch.utils import split_str_to_list
class Node:
    def __init__(self,value,program):#
        self.value=value
        self.child_list=[]
        self.program=program
    def __len__(self):
        return len(self.child_list)
    def eval_node(self):
        return self.program.eval_node(self)
    def __str__(self):
        return str(self.value)    
    def add_child(self,node):
        self.child_list.append(node)
    def isValidNode(string):
        raise NotImplementedError()
    def buildNode(name,program):#single token
        if PrimNode.isValidNode(name):
            return PrimNode(name,program)
        elif OperNode.isValidNode(name):
            return OperNode(name,program)
        else:
            return Node(name,program)
    def buildTree(string,program):
        if (" " not in string):
            node=Node.buildNode(string,program)
            return node
        str_list=split_str_to_list(string)
        temp_node=Node.buildNode(str_list[0],program)
        for substr in str_list[1:]:
            temp_node.add_child(Node.buildTree(substr,program))
        return temp_node
            
class PrimNode(Node):
    def __init__(self,value,program):
        self.value=int(value)
        self.child_list=[]
        self.program=program
    def eval_node(self):
        return self.value
    def isValidNode(string):
        return string.isdigit()
    
class OperNode(Node):
    definedList=["+","*"]
    def __init__(self,value,program):
        super().__init__(value,program)
    def eval_node(self):
        if(self.value=="+"):
            return sum([x.eval_node() for x in self.child_list])
        elif(self.value=="*"):
            tempPro=1
            for child in self.child_list:
                tempPro*=child.eval_node()
            return tempPro
    def isValidNode(string):
        return string in OperNode.definedList