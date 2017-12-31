from enum import Enum
import re
class T_type(Enum):
    root=1
    oper=2
    denf=3
    var=4
    prim=5
def split_str_to_list(string):
    string=string.strip(" \n\t")
    string=re.sub(" +"," ",string)
    if("(" not in string):
        return string.split()
    res_list=[]
    prev_idx=-1
    bracket_counter=0
    for i in range(len(string)):
        if(bracket_counter==0 and string[i]==" " and prev_idx<i):
            res_list.append(string[prev_idx+1:i])
            prev_idx=i
        elif string[i]=="(":
            bracket_counter+=1
            if(bracket_counter==1):#start of next procedure
                prev_idx=i
        elif string[i]==")":
            bracket_counter-=1
            if(bracket_counter==0):#end of this procedure
                res_list.append(string[prev_idx+1:i])
                prev_idx=i+1
        elif (i==len(string)-1 and prev_idx<i):
            res_list.append(string[prev_idx+1:])
        assert(bracket_counter>=0)
    assert(bracket_counter==0)
    return res_list
def strip_str(string):
    return string.strip(" \n\t").replace("\n"," ")
    