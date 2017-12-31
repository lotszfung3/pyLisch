from .node import Node
from . import utils
class Program:
    def __init__(self,string):
        self.program_str=utils.strip_str(string)
        self.rootNode=Node.build(string)
    def procedures_len(self):
        return len(self.self.rootNode)    
    def run(self):
        self.rootNode.eval()