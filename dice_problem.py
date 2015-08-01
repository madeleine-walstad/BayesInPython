from suite import suite

class dice_problem(suite):

	def likelihood(self, data, hypothesis):
		if data > hypothesis:
			return 0
		elif data <= 0:
			return 0
		else:
			return 1/hypothesis


def main():

	suite = dice_problem([4, 6, 8, 12, 20])

	suite.update(6)

	print('Problem 1: Rolled a 6')
	suite.print()

	suite2 = dice_problem([4, 6, 8, 12, 20])
	for roll in [6, 8, 7, 7, 5, 4]:
		suite2.update(roll)
	print('Problem 2: Rolled 6, 8, 7, 7, 5, 4')
	suite2.print()

if __name__ == '__main__':
	main()