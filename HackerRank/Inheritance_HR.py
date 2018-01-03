class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
    a = 0
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        a = sum(self.scores)/len(self.scores)
        if a<40:
        	return "T"
       	elif (a>=40) and (a<55):
       		return "D"
       	elif (a>=55) and (a<70):
       		return "P"
       	elif (a>=70) and (a<80):
       		return "A"
       	elif (a>=80) and (a<90):
       		return "E"
       	elif (a>=90) and (a<=100):
       		return "O"
       	else:
       		return ""


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())