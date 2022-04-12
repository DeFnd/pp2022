class Student:
    def __init__(self,name="",id="",dob=""):
        self.__name=name
        self.__id=id
        self.__dob=dob
    def getName(self):
        return self.__name
    
    def getId(self):
        return self.__id
    
    def getdob(self):
        return self.__dob
    
    def __str__(self):
        return f"Student's name is: {self.__name}, Student's id is: {self.__id}, Student's dob is: {self.__dob}"
    
    def describe(self):
        print( self.__str__())

    def input(self):
        self.__name=input("Student's name:")
        self.__id=input("Student's id:")
        self.__dob=input("Student's dob:")

class Course:
    def __init__(self,name="",id=""):
        self.__name=name
        self.__id=id
        
    def getName(self):
        return self.__name
    
    def getId(self):
        return self.__id
    
    def __str__(self):
        return f"Course's name is: {self.__name}, Course's id is: {self.__id}"
    
    def describe(self):
        print( self.__str__())

    def input(self):
        self.__name=input("Course's name:")
        self.__id=input("Course's id:")
        
class Mark:
    def __init__(self,student,course,mark=""):
        self.__student=student
        self.__course=course
        self.__mark=mark
        
    def getStudent(self):
        return self.__student
    
    def getCourse(self):
        return self.__course
    
    def getMark(self):
        return self.__mark
    
    def __str__(self):
        return f"Student name: {self.__name} - Course's id is: {self.__id}- has mark:{self.__mark}"
    
    def describe(self):
        print( self.__str__())

    def input(self):
        self.__mark=input("Enter mark of student name: {self.__student.getName},course {self.__course.getName}:")
        

class Management:
    def list(self):
        pass
    
    def input(self):
        pass

class StudentManagement(Management):
    def __init__(self):
        self.__stds=[]
        self.__cours=[]
        self.__marks=[]
        
    def getStudent(self,idx):
        return self.__stds[idx]
    
    def getCourse(self,idx):
        return self.__cours[idx]
    
    def getMark(self,idx):
        return self.__marks[idx]
    
    def inputStudent(self):
        s=Student()
        s.input()
        self.__stds+=[s]
    
    def inputCourse(self):
        c=Course()
        c.input()
        self.__cours+=[c]
    
    def inputMark(self):
        for i in range(len(self.__stds)):
            m0=[]
            for j in range (len(self.__cours)):
                c=int(input(f"Enter mark of student name {self.__stds[i].getName()} - course {self.__cours[j].getName()}"))
                m0+=[c]
            self.__marks+=[m0]
    
        
    def listMark(self):
        for i in range(len(self.__stds)):
            for j in range (len(self.__cours)):
                print (f"Mark of student name {self.__stds[i].getName()} - course {self.__cours[j].getName()} is :{self.__marks[i][j]}")
    def list(self):
        for i in self.__stds:
            i.describe()


NumberOfStd=int(input("\nHow many students are there?"))
studentmanagement=StudentManagement()
for i in range(NumberOfStd):
    studentmanagement.inputStudent()
NumberOfCour=int(input("\nHow many courses are there?"))
for j in range(NumberOfCour):
    studentmanagement.inputCourse()
studentmanagement.inputMark()
studentmanagement.listMark()