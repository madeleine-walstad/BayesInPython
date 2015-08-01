from suite import suite

class monty_hall(suite):

	def likelihood(self, guess, door):
		if door.name == guess:
			return 0
		elif door.name == door.DOOR_A:
			return 0.5
		else:
			return 1

class door:

	DOOR_A = "A"
	DOOR_B = "B"
	DOOR_C = "C"

	def __init__(self, name):
		self.name = name

	def __eq__(self, other):
		if isinstance(other, door):
			return self.name == other.name
		return False

	def __str__(self):
		return self.name

def main():

	door_a = door(door.DOOR_A)
	door_b = door(door.DOOR_B)
	door_c = door(door.DOOR_C)

	mh = monty_hall([door_a, door_b, door_c])

	mh.update(door.DOOR_B)

	mh.print()


if __name__ == '__main__':
	main()