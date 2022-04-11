import curses
import math
import numpy as np
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