class SymbolTable:
	'''
	dicts of tuples in the variable looking-up table
	'''
	def __init__(self, prev=None):
		self.prev = prev
		self.curr = {}
	def __str__(self):
		ans=""
		for i in self.curr:
			ans+=(str(i)+"\n") if i else ""
		return ans
	def __contains__(self, key):
		return self[key] is not None
	
	def __getitem__(self, key):
		if key in self.curr:
			return self.curr[key]
		if self.prev:
			return self.prev[key]
		
	def __setitem__(self, key, value):
		assert(key not in self.curr)
		self.curr[key] = value
