from pmf import pmf

class suite(pmf):

	TYPE_INT = 'integer'
	TYPE_CUSTOM = 'custom'

	def basic_prior_function(self, hypothesis):
		return 1

	def __init__(self, hypotheses=tuple(), prior_function=None):
		""" __init__: initializes the suite object and sets the pmf to hold the priors of each hypothesis

			:param hypotheses: a tuple of objects that are strings or can be cast to strings and are comparable
		"""
		super().__init__()
		self.hypotheses = hypotheses

		if prior_function == None:
			prior_function = self.basic_prior_function

		if type(hypotheses[0]) == int:
			self.key_type = self.TYPE_INT
		else:
			self.key_type = self.TYPE_CUSTOM

		for hypothesis in hypotheses:
			if self.key_type == self.TYPE_INT:
				super().set(hypothesis, prior_function(hypothesis))
			else:
				hypothesis_name = str(hypothesis)
				super().set(hypothesis_name, prior_function(hypothesis))
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
			if self.key_type == self.TYPE_INT:
				hypothesis_name = hypothesis
			else:
				hypothesis_name = str(hypothesis)
			super().mult(hypothesis_name, l)
		super().normalize()


	def print(self):
		""" print: print out each hypothesis and its corresponding probability in the pmf
		"""
		for hypothesis in self.hypotheses:
			if self.key_type == self.TYPE_INT:
				hypothesis_name = hypothesis
			else:
				hypothesis_name = str(hypothesis)
			prob = super().prob(hypothesis_name)
			print(hypothesis_name, prob)


	def makeCdf(self):
		return super().makeCdf()


	def mean(self, shouldPrint=False):
		"""
			returns the mean of the probabilities in this suite
			if optional parameter shouldPrint is True it will print this value
		"""
		total = 0
		for hypothesis in self.hypotheses:
			if self.key_type == self.TYPE_INT:
				hypothesis_name = hypothesis
			else:
				hypothesis_name = str(hypothesis)
			prob = super().prob(hypothesis)
			total += hypothesis_name * prob
		if shouldPrint:
			print(str(total))
		return total


	def get_probability_distribution(self):
		"""
			only works for suites with integer hypothesis names
			returns a list of probabilities sorted by their corresponding hypothesis
		"""
		if self.key_type == self.TYPE_INT:
			y = []
			for h in sorted(self.hypotheses):
				y.append(super().prob(h))
			return y
		else:
			print("Calling this function on a suite with non-integer hypotheses is probably a bad idea.")
			return None;


