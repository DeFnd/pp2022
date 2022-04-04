import curses
import math
import numpy as np

#--------------------------------curses--------------------------------------------------------------------------------
print("preparing to initialize screen...")
screen = curses.initscr()
print("Screen initialized.")
screen.refresh()
curses.napms(2000)
curses.endwin()
print("window ended.")

#---------------------------------student------------------------------------------------------------------------------

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
        self.__name=input("Enter student's name:")
        self.__id=input("Enter student's id:")
        self.__dob=input("Enter student's dob:")
#------------------------------------course-----------------------------------------------------------------------------
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
        self.__name=input("Enter Course's name:")
        self.__id=input("Enter Course's id:")
#-------------------------------------mark---------------------------------------------------------------------------
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

#----------------------------------student management-----------------------------------------------------------------------------
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
        self.__credits=[]
        self.__gpa=[]

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
                c=int(input(f"Enter mark of student's name: {self.__stds[i].getName()} - course {self.__cours[j].getName()}"))
                m0+=[c]
            self.__marks+=[m0]

    def inputCredit(self):
        for i in range (len(self.__cours)):
            credit=int(input(f"Enter number of credit for course: {self.__cours[i].getName()}"))
            self.__credits+=[credit]

    def averageGPA(self):
        print("\n\n")
        mark=np.array(self.__marks)
        credit=np.array(self.__credits)

        sumCredit=0
        for i in range (len(self.__credits)):
            sumCredit+=self.__credits[i]
        GPA=(mark@credit)/sumCredit
        for i in range(len(GPA)):
            a=GPA[i]
            self.__gpa+=[a]

    def listGPA(self):
        print("\n\n")
        print(np.array(self.__gpa))
        for i in range(len(self.__stds)):
            print (f"Average GPA of student name {self.__stds[i].getName()}  is :{self.__gpa[i]}")

    def listFloorGPA(self):
        print("\n\nAfter rounded down, GPA are:")
        for i in range(len(self.__stds)):
            print (f"Average GPA of student name {self.__stds[i].getName()}  is :{math.floor(self.__gpa[i])}")

    def softStudentGPA(self):
        studentList=[]
        for n in range (len(self.__stds)):
            c=self.__stds[n].getName()
            studentList+=[c]

        st=np.array(studentList)
        gpa=np.array(self.__gpa)
        temp1=0
        temp2=0
        i=0
        j=i+1
        for i in range(len(gpa)):
            for j in range(len(gpa)):
                if gpa[i]>gpa[j]:
                    temp1=gpa[i]
                    gpa[i]=gpa[j]
                    gpa[j]=temp1

                    temp2=st[i]
                    st[i]=st[j]
                    st[j]=temp2
        print(st)
        print(gpa)
        for k in range(len(gpa)):
            print(f" \n\nStudent name {st[k]} has average GPA: {gpa[k]}")


    def listMark(self):
        print("\n\n")
        for i in range(len(self.__stds)):
            for j in range (len(self.__cours)):
                print (f"Mark of student name {self.__stds[i].getName()} - course {self.__cours[j].getName()} is :{self.__marks[i][j]}")


    def listStudentGPA(self):
        print("\n\n")
        for i in self.__stds:
            i.describe()


NumberOfStd=int(input("\nEnter number of students: "))
studentmanagement=StudentManagement()
for i in range(NumberOfStd):
    studentmanagement.inputStudent()
NumberOfCour = int(input("\nEnter number of course: "))
for j in range(NumberOfCour):
    studentmanagement.inputCourse()
    studentmanagement.inputMark()
    studentmanagement.listMark()
    studentmanagement.inputCredit()
    studentmanagement.averageGPA()
    studentmanagement.listGPA()
    studentmanagement.listFloorGPA()
    studentmanagement.softStudentGPA()