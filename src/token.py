from .utils import T_type
class Token:
    def __init__(self,args):
        self.t_type=args["type"]
        self.value=args["value"]
        self.eval=args["eval"]
    def __str__(self):
        return str(self.t_type)+": "+str(self.value)
    def __eq__(self,other):
        if isinstance(other,str):
            return self.value==other
        elif isinstance(other,Token):
            return self==other
        raise Exception("can't compare with token")
    def eval(self,args):
        return self.eval(args) if args else self.eval()
        
'''
eval function for defined tokens
@param args: list of the nodes of all children
@return: result after the evaluation 
'''
def plus(args):
    assert(len(args)>1)
    return sum([i.eval() for i in args])
def minus(args):
    assert(len(args)==2)
    return args[0].eval()-args[1].eval()
def multiply(args):
    assert(len(args)>1)
    res=1
    for i in args:
        res=res*i.eval()
    return res
def divide(args):
    assert(len(args)==2)
    return args[0].eval()/args[1].eval()
def equal(args):
    assert(len(args)==2)
    return args[0].eval()==args[1].eval()
def greater(args):
    assert(len(args)==2)
    return args[0].eval()>args[1].eval()
def lesser(args):
    assert(len(args)==2)
    return args[0].eval()<args[1].eval()
def root_eval(args):
    for arg in args:
        if(not arg.token.t_type==T_type.denf):
            print("result:" +str(arg.eval()))        
def if_func(args):
    assert(len(args)>1 and len(args)<4)
    return args[1].eval() if args[0].eval() else args[2].eval() if len(args)==3 else None
def eval_func(args):
    assert(len(args)==2)
    return args[1].eval()
class TokenBuilder:
    token_dict={
            "+":(T_type.oper,"+",plus),
            "-":(T_type.oper,"-",minus),
            "*":(T_type.oper,"*",multiply),
            "/":(T_type.oper,"/",divide),
            "=":(T_type.oper,"=",equal),
            ">":(T_type.oper,">",greater),
            "<":(T_type.oper,"<",lesser),
            "if":(T_type.oper,"if",if_func),
            "root":(T_type.root,"root",root_eval),
            "define":(T_type.denf,"define",eval_func)
            }
    def build_dict(args):
        return {"type":args[0],"value":args[1],"eval":args[2]}
    def build_token(value,rootNode):
        if(value in TokenBuilder.token_dict):
            return Token(TokenBuilder.build_dict(TokenBuilder.token_dict[value]))
        elif (value.replace('.','',1).isdigit()):#is number
            value=float(value) if "." in value else int(value)
            return Token(TokenBuilder.build_dict([T_type.prim,value,lambda :value]))
        else:#self-defined variable or function
            #value is the define node of the same name
            assert (value[0].isalpha())
            if(rootNode):
                def_node=rootNode.get_var_node(value)
                return Token(TokenBuilder.build_dict([T_type.var,value,lambda:def_node.eval()]))
            else:
                return Token(TokenBuilder.build_dict([T_type.var,value,lambda:value]))
            
