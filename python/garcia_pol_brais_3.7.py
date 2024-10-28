class StudentGroup:
    
    def __init__(self, id, groupName, studentList):
        self.id = id
        self.groupName = groupName
        self.studentList = [self.Student()]

    def __str__(self):
        f"{self.id} {self.groupName} {self.students}"   

    class Student:
    
        def __init__(self, id, Person, degree):
            self.id = id
            self.person = self.Person()
            self.degree = degree

        def __str__(self):
            return f" person : {self.person.__str__()} student id: {self.id}  degree :{self.degree} "
    
        class Person:
    
            def __init__(self, id, name, age):
                self.id = id
                self.name = name
                self.age = age

            def __str__(self):
                return f"Name: {self.name}  id: {self.id} age: {self.age} "
    

    
    
student1 = StudentGroup.Student(1,StudentGroup.Student.Person(10,"John",23),"psychology")
student2 = StudentGroup.Student(2,StudentGroup.Student.Person(20,"Marth",18),"computer science")
student3 = StudentGroup.Student(3,StudentGroup.Student.Person(30,"Claire",23),"philosophy")

print(student1)
print(student2)
print(student3)

studentList = [student1,student2, student3]

studentG = StudentGroup(1, "GroupName", studentList)

print(studentG)
