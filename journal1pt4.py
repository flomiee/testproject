import random
class Animal:
	def __init__(self, arm_len, leg_len, eyes, has_tail, is_furry):
		self.arm_len =float(arm_len) 
		self.leg_len = float(leg_len)
		self.eyes = int(eyes)
		self.has_tail = bool(has_tail)
		self.is_furry = bool(is_furry)
	def describe(self):
		print('Tiger Characteristics')
		print(f'Arm Length:{self.arm_len}cm')
		print(f'Leg Length:{self.leg_len}cm')
		print(f'Eyes:{self.eyes}')

		print(f"Has Tail:{'Yes'if self.has_tail else'No'}")
		print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")
my_animal = Animal(50.0,100,2,True,True)
my_animal.describe()