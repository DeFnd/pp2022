import curses
import math
import numpy as np
class Student:

    def input(self):
        self.__name=input("Enter student's name:")
        self.__id=input("Enter student's id:")
        self.__dob=input("Enter student's dob:")
class Course:

    def input(self):
        self.__name=input("Enter Course's name:")
        self.__id=input("Enter Course's id:")
class Mark:
    def input(self):
        self.__mark=input("Enter mark of student name: {self.__student.getName},course {self.__course.getName}:")

class Management:
    def list(self):
        pass

    def input(self):
        pass

class StudentManagement(Management):
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