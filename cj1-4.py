# Brent Brison
# Doctor Aguiche
# ASTR 19
# 9 January 2023

# Coding Journal Week 1 PROMPT 4:

'''
This Python program declares a class describing my favorite animal (a dog). 
Have the data members of the class represent the following physical parameters of the animal: 
-	length of the arms (float)
- 	length of the legs (float)
-	number of eyes (int)
-	does it have a tail? (bool) 
-	is it furry? (bool). 

Write an initialization function that sets the values of the data members when an instance of the class is created. 
Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
'''

class Dog:
	def __init__(self, armLength: int, legLength: int, numEyes: int, hasTail: bool, isFurry: bool):
		self.armLength = armLength
		self.legLength = legLength
		self.numEyes = numEyes
		self.hasTail = hasTail
		self.isFurry = isFurry
	
	def printAnimalData(self):
		print("The length of this animal\'s arm(s) is:", self.armLength, "feet")
		print("The length of this animal\'s leg(s) is:", self.legLength, "feet")
		print("This animal has", self.numEyes, "eyes")
		
		if (self.hasTail == True):
			print("This animal has a tail")
		else: print("This animal does not have a tail")

		if (self.isFurry == True):
			print("This animal is furry")
		else: print("This animal is not furry")


def main():
	mansBestFriend = Dog(3, 3, 2, True, True)
	mansBestFriend.printAnimalData()


if __name__ == "__main__":
	main()
	print("Exiting program...")