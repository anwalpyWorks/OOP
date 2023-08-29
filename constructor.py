
class Student:
    no_of_leaves = 8

# class ko arguments deny k method ko instructor kehtain hain us k liya init function create karna parta
    def __init__(self, aname, asection, aid):
        self.name = aname
        self.section = asection             #sel--> calling obj of class,  name-->inctance, aname-->argumrents
        self.id = aid

#use method or is self us ko kehtyn hain jis object ki baat ki ja rahi ho ya jis obj pr kam karna
    def printalldetail(self):
        return f"Name is {self.name}, section is {self.section}, id is {self.id}, no_of_leaves {self.no_of_leaves}"


# class method jo class b access kary or instance b access kar saky
    @classmethod
    def change_leaves(cls, newleave):
        cls.no_of_leaves = newleave

obj2 = Student("mirza", 12, "instructor", )
obj2.printalldetail()
obj2.change_leaves(34)

#create class objects
obj = Student("Anwal", 12, "instructor", )
print(obj.printalldetail())
print(obj.no_of_leaves)


