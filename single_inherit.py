class student:
    no_of_leaves = 8

    def __init__(self, aname, asection, aid):
        self.name = aname
        self.section = asection
        self.id = aid

    def printalldetail(self):
        return f"Name is {self.name}, section is {self.section}, id is {self.id}"

class Programmer(student):
    no_of_holiday = 56

    def __init__(self, aname, asection, aid, alanguages):
        self.name = aname
        self.section = asection
        self.id = aid
        self.languages = alanguages

    def printalldetail(self):
        return f"Name is {self.name}, section is {self.section}, id is {self.id}, language is {self.languages}"

obj1 = student("anwal", "A", 1,)
obj2 = student("arif", "B", 2,)

obj3 = Programmer("anwal", "A", 1, "Python")
obj4 = Programmer("arif", "B", 2, "Fastapi")
print(obj4.printalldetail())