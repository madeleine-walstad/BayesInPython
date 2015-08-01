from pmf import pmf

class suite(pmf):

	def __init__(self, hypotheses=tuple()):
		""" __init__: initializes the suite object and sets the pmf to hold the priors of each hypothesis

			:param hypotheses: a tuple of objects that are strings or can be cast to strings and are comparable
		"""
		super().__init__()
		self.hypotheses = hypotheses
		for hypothesis in hypotheses:
			hypothesis_name = str(hypothesis)
			super().set(hypothesis_name, 1)
		super().normalize()


	def likelihood(self, data, hypothesis):
		""" likelihood: calculates the likelihood [ p(D|H) ] for a given data and hypothesis, this is an abstract
			method and must be implemented by a subclass

			:param data: the available data set for the question we are trying to answer
			:param hypothesis: the hypothesis we are trying to calculate the likelihood for
		"""
		return


	def update(self, data):
		""" update: update the pmf to take into account the likelihood of each hypothesis

			:param data: the available data set for the question we are trying to answer
		"""
		for hypothesis in self.hypotheses:
			l = self.likelihood(data, hypothesis)
			hypothesis_name = str(hypothesis)
			super().mult(hypothesis_name, l)
		super().normalize()


	def print(self):
		""" print: print out each hypothesis and its corresponding probability in the pmf
		"""
		for hypothesis in self.hypotheses:
			hypothesis_name = str(hypothesis)
			prob = super().prob(hypothesis_name)
			print(hypothesis_name, prob)

