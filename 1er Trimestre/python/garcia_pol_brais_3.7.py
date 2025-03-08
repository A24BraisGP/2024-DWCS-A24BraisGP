# class StudentGroup:
    
#     def __init__(self, id, groupName, studentList):
#         self.id = id
#         self.groupName = groupName
#         self.studentList = studentList

#     def __str__(self):
#         for item in self.studentList:
#             print(f"{item}")  
            
#         return f"That was group {self.id} {self.groupName}" 

#     class Student:
    
#         def __init__(self, id, person, degree):
#             self.id = id
#             self.person = person
#             self.degree = degree

#         def __str__(self):
#             return f" person : {self.person.__str__()} student id: {self.id}  degree :{self.degree} "
    
#         class Person:
    
#             def __init__(self, id, name, age):
#                 self.id = id
#                 self.name = name
#                 self.age = age

#             def __str__(self):
#                 return f"Name: {self.name}  id: {self.id} age: {self.age} "
    

    
    
# student1 = StudentGroup.Student(1,StudentGroup.Student.Person(10,"John",23),"psychology")
# student2 = StudentGroup.Student(2,StudentGroup.Student.Person(20,"Marth",18),"computer science")
# student3 = StudentGroup.Student(3,StudentGroup.Student.Person(30,"Claire",23),"philosophy")

# print(student1)
# print(student2)
# print(student3)



# studentList = [student1,student2, student3]

# studentG = StudentGroup(1, "GroupOne", studentList)

# print(studentG)


# studentList.remove(student2)
# print(studentG)


# studentList.append(StudentGroup.Student(4,StudentGroup.Student.Person(40,"Marth",18),"computer science"))
# print(studentG)


class Person: 
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    
    def __str__(self):
        return f" --- {self.id} {self.name} {self.age} --- "
    
class Student:
    def __init__(self,id, person, degree):
        self.id = id 
        self.person = person
        self.degree = degree
    
    def __str__(self):
        return f"{self.id} {self.person} {self.degree}"
        
class StudentGroup:
    def __init__(self, id, groupName, students):
        self.id = id
        self.groupName = groupName
        self.students = students
    
    def __str__(self):
        res = "["+self.groupName+"]: - {\n"
        for student in self.students:
            res += "\t"+str(student)+" ,\n"
        res += " }"
        return str(res)
    
    
person1 = Person("1","Marta",23)
person2 = Person("2","Alicia",24)
person3 = Person("3","Lara",26)

student1 = Student("10",person1,"Philosophy")
student2 = Student("20",person2,"Computer Sciense")
student3 = Student("30",person3, "Musicology")

studentList = [student1,student2,student3]

studentGroup1 = StudentGroup("100","Group 1", studentList)

print(studentGroup1)