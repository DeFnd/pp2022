import curses
import math
import numpy as np

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