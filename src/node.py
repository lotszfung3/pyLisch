from .token import Token,TokenBuilder
from .utils import split_str_to_list, T_type
from .exceptions import variableNotFoundException
'''

'''
class Node:
    def __init__(self,token):
        assert isinstance(token,Token)
        self.child_list=[]
        self.token=token
    def __len__(self):
        return len(self.child_list)
    def __str__(self):
        return str(self.token)
    def add_child(self,child):
        if(type(child)==list):
            for i in child:
                assert isinstance(i,Node)                
                self.child_list.append(i)
        else:
            assert isinstance(child,Node)
            self.child_list.append(child)
    def get_var_node(self,name):
        for i in self.child_list:
            if (i.token=="define" and i.child_list[0].token==name):
                return i.child_list[0]
        raise variableNotFoundException(name)
                
        
    def eval(self):
        if(len(self.child_list)>0):
            return self.token.eval(self.child_list)
        else:
            return self.token.eval()
    '''
    build the whole tree starting from the node
    recursively using the whole program string
    '''
    def build(string):
        rootNode=Node(TokenBuilder.build_token("root",""))
        for i in split_str_to_list(string):  
            rootNode.add_child(Node.build_recur(i,rootNode,True))
        
        return rootNode
    '''
    @param: "+ 3 (+ 3 3)"
    @return: a plus node with 2 children
    '''
    def build_recur(string,rootNode,isExpand):
        if(" " not in string):
            return Node(TokenBuilder.build_token(string,rootNode if isExpand else None))
        else:
            i=split_str_to_list(string)#["+","3","3"]
            res_node= Node(TokenBuilder.build_token(i[0],rootNode if isExpand else None))
            res_node.add_child([Node.build_recur(j,rootNode,res_node.token.t_type!=T_type.denf) for j in i[1:] ])
            return res_node

            
    
