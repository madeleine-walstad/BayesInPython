from suite import suite

class CookieProblem(suite):

	def likelihood(self, data, bowl):
		for d in data:
			if d == CookieBowl.FLAVOR_CHOCOLATE:
				return bowl.getProbabilityChocolate()
			elif d == CookieBowl.FLAVOR_VANILLA:
				return bowl.getProbabilityVanilla()
			else:
				print("invalid flavor value")
				return None


class CookieBowl:

	FLAVOR_CHOCOLATE = "chocolate"
	FLAVOR_VANILLA = "vanilla"

	def __init__(self, name, num_chocolate, num_vanilla):
		self.name = name
		self.num_chocolate = num_chocolate
		self.num_vanilla = num_vanilla

	def __eq__(self, other):
		if isinstance(other, CookieBowl):
			return self.name == other.name
		return false

	def __str__(self):
		return self.name

	def getTotalCookies(self):
		return self.num_chocolate + self.num_vanilla

	def getProbabilityChocolate(self):
		return self.num_chocolate / self.getTotalCookies()

	def getProbabilityVanilla(self):
		return self.num_vanilla / self.getTotalCookies()




def main():
	bowl1 = CookieBowl('bowl1', 10, 30)
	bowl2 = CookieBowl('bowl2', 20, 20)

	pmf = CookieProblem([bowl1, bowl2])
	data = [CookieBowl.FLAVOR_VANILLA]
	pmf.update(data)

	pmf.print()



if __name__ == '__main__':
	main()