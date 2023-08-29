class student:
    no_of_leaves = 8
    pass

#create class objects
obj1 = student()
obj2 = student()
print(obj2, obj1)

#when we create an instance with values
obj1.name = "Anwal"
obj1.section = 1
obj1.id = 12
print(obj1.id, obj1.name, obj1.section)

obj2.name = "Mirza"
obj2.section = 2
obj2.id = 13
obj2.no_of_leaves = 9
print(student.no_of_leaves)

# dict function display all detail of the object/instance
print(obj2.__dict__)


# class k jitny b object bany hain un sab ka data show karwa dy ga
print(student.__dict__)
