from suite import suite
import numpy as np
import matplotlib.pyplot as mpl
from pmf import pmf
import sys

class Train(suite):

	def likelihood(self, data, hypothesis):
		if data > hypothesis:
			return 0
		else:
			return 1/hypothesis

	def mean(self, shouldPrint=False):
		total = 0
		for hypothesis in self.hypotheses:
			hypothesis_name = str(hypothesis)
			prob = super().prob(hypothesis)
			total += hypothesis * prob
		if shouldPrint:
			print(str(total))
		return total

	def plot(self):
		x = self.hypotheses
		y = []
		for i in x:
			name = str(i)
			y.append(super().prob(i))
		mpl.plot(x, y)
		mpl.show()

	def get_probability_distribution(self):
		y = []
		for h in self.hypotheses:
			name = str(h)
			y.append(super().prob(h))
		return y

	def percentile(self, percentage):
		""" percentile: returns the value of the specified percentile

			:param percentage: the percentile you wish to have the value for - so if you want the vaue of the
			95th percentile percentage should equal 95
		"""
		p = percentage / 100.0
		total = 0.0
		values = self.values()
		for value in sorted(values.keys()):
			prob = values[value]
			total += prob
			if total >= p:
				return value


class PowerTrain(Train):

	def __init__(self, hypotheses, alpha=1.0):
		pmf.__init__(self)
		self.hypotheses = hypotheses
		self.key_type = suite.TYPE_INT
		for hypothesis in hypotheses:
			self.set(hypothesis, hypothesis**(-alpha))
		self.normalize()


def plot(xs, ys, labels=[]):
	""" plot: plots several distributions on the same graph


		:param xs: an array of arrays giving the x coordinates for each distribution to plot
		:param ys: an array of arrays giving the y coordinates for each distribution to plot
	"""

	if len(xs) != len(ys):
		print('Invalid input. ' + str(len(xs)) + ' does not equal ' + str(len(ys)))

	if len(labels) != len(xs):
		print('Invalid labels. Autogenerating labels...')
		labels = []
		for index, x in enumerate(xs):
			labels.append(str(x))

	plots =[]

	for index, x_distribution in enumerate(xs):
		y_distribution = ys[index]
		plot, = (mpl.plot(x_distribution, y_distribution, label=labels[index]))
		plots.append(plot)
	mpl.legend(handles=plots)
	mpl.show()

def power_prior_function(x, alpha=1.0):
	return x ** (-alpha)


def main(showPlots='all'):

	### STRATEGY 1 - uniform
	hypotheses = range(1, 1000)
	train = Train(hypotheses)
	train.update(60)
	print("""A railroad numbers its trains in order 1...N. Given that we have just seen a train marked\
'60' and it is equally likely that the railroad has any number of trains 1...1000, how many trains\
does the railroad have?""")
	train.mean(shouldPrint=True)


	### STRATEGY 2 - power distrobution
	train2 = PowerTrain(hypotheses, )
	train2.update(60)
	print("""Using the power rule and given that we have just seen a train marked\
'60' and it is equally likely that the railroad has any number of trains 1...1000, how many trains\
does the railroad have?""")
	train2.mean(shouldPrint=True)

	xs = [hypotheses, hypotheses]
	ys = [train.get_probability_distribution(), train2.get_probability_distribution()]
	if showPlots == 'all':
		plot(xs, ys, ['uniform', 'power law'])


	### with more data the spread between the uniform and power distributions is smaller
	data = [30, 60, 90]
	train3 = Train(hypotheses)
	train4 = PowerTrain(hypotheses)
	for d in data:
		train3.update(d)
		train4.update(d)
	ys_more_data = [train3.get_probability_distribution(), train4.get_probability_distribution()]
	if showPlots == 'all':
		plot(xs, ys_more_data, ['uniform, more data', 'power law, more data']) 

	## plot both strategies together
	cumulative_xs = [hypotheses, hypotheses, hypotheses, hypotheses]
	cumulative_ys = [ys[0], ys[1], ys_more_data[0], ys_more_data[1]]
	if showPlots == 'final' or showPlots == 'all':
		plot(cumulative_xs, cumulative_ys, ['uniform', 'power law', 'uniform, more data', 'power law, more data'])


	### using percentile to analyze the data
	interval_train3 = train3.interval(5, 95)
	interval_train4 = train4.interval(5, 95)
	print("For train3 (uniform prior with 3 data points) there is a 90 percent chance that the actual value is in the interval " + str(interval_train3))
	print("For train4 (power distr prior with 3 data points) there is a 90 percent chance that the actual value is in the interval " + str(interval_train4))


if __name__ == '__main__':
	if len(sys.argv[1:]) > 0:
		showPlots = sys.argv[1]
		main(showPlots)
	else:
		main()
