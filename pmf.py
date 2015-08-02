from cdf import cdf

class pmf:

	def __init__(self):
		"""__init__: creates an empty dictionary
		"""
		self.valuesDict = {}


	def set(self, item, value):
		""" set: sets the value of item in dictionary to be value

        :param item: the item whose value is to be updated
        :param value: the new value of item
        """
		if item not in self.valuesDict:
			self.valuesDict[item] = value
		else:
			print("Item Already Exists")


	def incr(self, item, diff):
		""" incr: if an item with key equal to item exists in the dictionary then increment its value by diff, 
			otherwise create that entry in the dictionary and set its value to diff

		:param item: item whose value is to be incremented
		:param diff: amount the value should be incremented by
		"""
		if item in self.valuesDict:
			self.valuesDict[item] += diff
		else:
			self.valuesDict[item] = diff


	def mult(self, item, x):
		""" mult: if an item with key equal to item exists in the dictionary then multiply its value by x, otherwise 
			do nothing

		:param item: item whose value is to be scalled
		:param x: scaling factor for the item's value
		"""
		if item in self.valuesDict:
			self.valuesDict[item] *= x
		else:
			print("item does not exist")

	def normalize(self):
		""" normalize: normalizes the pmf so that the sum of all the values in the distrubution equals 1
		"""
		total = 0.0
		if len(self.valuesDict) > 0:
			for key, value in iter(self.valuesDict.items()):
				total += value
			for key, value in iter(self.valuesDict.items()):
				newValue = value/total
				self.valuesDict[key] = newValue

	def prob(self, item):
		""" prob: returns the value stored for the key equal to item, if the key exists in the dictionary

		:param item: key for the value to be returned
		"""
		if item in self.valuesDict:
			return self.valuesDict[item]
		else:
			print("Item does not exist")
			return None

	def values(self):
		""" values: returns the dictionary of values
		"""
		return self.valuesDict

	def makeCdf(self, name=None):
		""" makeCdf: builds a cumulative distribution function from the pmf

		:param (optional) name: a name for the new cdf, defaults to the name of this pmf if undefined
		"""
		if name == None:
			name = self.name
		xs = []
		counts = []
		running_total = 0
		for value, prob in sorted(self.values()):
			xs.append(value)
			counts.append(running_total)
		running_total = float(running_total)
		probs = [count / running_total for count in counts]
		return cdf(xs, probs, name)


	def interval(self, start, end):
		return self.percentile(5), self.percentile(95)


