from suite import suite

class mnm(suite):

	def likelihood(self, data, hypothesis):
		bag_name, color = data
		mix = hypothesis.get_type_for_bag(bag_name)
		l = mix[color]
		return l

class hypothesis:

	BAG1_NAME = 'bag1'
	BAG2_NAME = 'bag2'

	def __init__(self, name, bag1_type, bag2_type):
		self.name = name
		self.bag1 = bag(bag1_type, self.BAG1_NAME)
		self.bag2 = bag(bag2_type, self.BAG2_NAME)

	def __eq__(self, other):
		if isinstance(other, bag):
			return self.name == other.name
		return false

	def __str__(self):
		return self.name

	def get_type_for_bag(self, bag_name):
		if self.bag1.name == bag_name:
			return self.bag1.type
		elif self.bag2.name == bag_name:
			return self.bag2.type
		else:
			print (bag_name + " does not match any bag names in this hypothesis.")
			return None


class bag:

	PRE_95_BAG = dict(brown = 30,
					  yellow = 20,
					  red = 20,
					  green = 10,
					  orange = 10,
					  tan = 10)

	POST_95_BAG = dict(blue = 24,
					   green = 20,
					   orange = 16,
					   yellow = 14,
					   red = 13,
					   brown = 13)

	def __init__(self, bag_type, name):
		self.type = bag_type
		self.name = name



def main():
	hypothesisA = hypothesis("A", bag.PRE_95_BAG, bag.POST_95_BAG)
	hypothesisB = hypothesis("B", bag.POST_95_BAG, bag.PRE_95_BAG)

	pmf = mnm([hypothesisA, hypothesisB])

	pmf.update((hypothesis.BAG1_NAME, 'yellow'))
	pmf.update((hypothesis.BAG2_NAME, 'green'))

	pmf.print()


if __name__ == '__main__':
	main()


