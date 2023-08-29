class student:
    no_of_leaves = 8

#use method or is self us ko kehtyn hain jis object ki baat ki ja rahi ho ya jis obj pr kam karna
    def printalldetail(self):
        return f"Name is {self.name}, section is {self.section}, id is {self.id}"



#create class objects
obj1 = student()
obj2 = student()
print(obj2, obj1)

#when we create an instance with values
obj1.name = "Anwal"
obj1.section = 1
obj1.id = 12

obj2.name = "Mirza"
obj2.section = 2
obj2.id = 13
print(obj1.id, obj1.name, obj1.section)
# print all values of class obj using class method 
print(obj1.printalldetail())
