from person import Person
from manager import Manager

class Department:
	def __init__(self, *args):
		self.members = list(args)
	def addMember(self, person):
		self.members.append(person)
	def giveRaises(self, percent):
		for person in self.members:
			person.giveRaise(percent)
	def showAll(self):
		for person in self.members:
			print(person)

if __name__ == '__main__':
	bob = Person('Bob Smith')
	sue = Person('Sue Jones', job='dev', pay=100000)
	tom = Manager('Tom Jones', 'mgr', 50000)
	development = Department(bob, sue)
	development.addMember(tom)
	development.giveRaises(.10)
	development.showAll()
