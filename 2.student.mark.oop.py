# ------------------------------ Student -------------------------------------
class Student:

    def __init__(self, name, std_id, dob):
        self._std_Name = name
        self._std_ID = std_id
        self._std_DoB = dob

    def set_std_name(self, name):
        self._std_Name = name

    def set_std_id(self, std_id):
        self._std_ID = std_id

    def set_std_dob(self, dob):
        self._std_DoB = dob

    def get_st_name(self):
        return self._std_Name

    def get_st_id(self):
        return self._std_ID

    def get_st_dob(self):
        return self._std_DoB

# ------------------------------ Course -------------------------------------
class Course:
    def __init__(self, name, c_id):
        self._name = name
        self._id = c_id

    def set_c_name(self, name):
        self._name = name

    def set_c_id(self, c_id):
        self._id = c_id

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

# ------------------------------ Student Management -------------------------------------
class StudentManagement:
    _st_Name = ""
    _crs_Inf = {}

    def __init__(self):
        pass

    def set_inf(self, name, course_inf):
        self._st_Name = name
        self._crs_Inf = course_inf

    def set_st_name(self, student_name):
        self._st_Name = student_name

    def get_st_name(self):
        return self._st_Name

    def set_crs_inf(self, dic_inf):
        self._crs_Inf = dic_inf

    def get_crs_inf(self):
        return self._crs_Inf


# ------------------------------ Database -------------------------------------
std_list = [Student("data", "data", "data")]
course_list = [Course("data", "data")]
stm_list = [StudentManagement()]

std_list.clear()
course_list.clear()
stm_list.clear()

count_smm = 0


# ------------------------------ Method -------------------------------------


def input_domain(value, min_value, max_value):
    while value < min_value or value > max_value:
        value = int(input("Your input is invalid! Enter again: "))
    return value


def exit_menu():
    global option
    print("---------------------End of this choice---------------------")
    option = int(input("Make other choice, 0 to exit: "))
    option = input_domain(option, 0, 6)
    if option == 0:
        print("You choose option exit!!!")


def option1():
    global i
    num_of_std = int(input("Input number of student in the class: "))
    for i in range(0, num_of_std):
        name = str(input("Student's Name: "))
        student_id = str(input("Student's ID: "))
        dob = str(input("Student's Date of Birth: "))
        std_list.append(Student(name, student_id, dob))


def option2():
    global i
    num_of_crs = int(input("Number of courses: "))
    for i in range(0, num_of_crs):
        c_name = str(input("Course's name: "))
        c_id = str(input("Course's ID: "))
        course_list.append(Course(c_name, c_id))


def option3():
    global option, i, count_smm
    name = str(input("Name of student you want to manage: "))
    cour_inf_lit = {}
    if CheckStudentList(name):
        stm_list.append(StudentManagement())
        stm_list[count_smm].set_st_name(name)
        num_of_course = int(input("Number of courses this student studied: "))
        for i in range(0, num_of_course):
            c_name = input("Name of course: ")
            if CheckCourseList(c_name):
                mark = int(input("Mark of this course: "))
                cour_inf_lit[c_name] = mark
                stm_list[count_smm].set_crs_inf(cour_inf_lit)
            else:
                print("Input course did not import.")
        count_smm += 1
    else:
        option = int(input("Input wrong ! Press 3 to do again, 0 to exit: !"))


def CheckStudentList(name):
    global i

    check = False
    for i in std_list:
        if name == i.get_st_name():
            check = True
    return check


def CheckCourseList(c_name):
    global i
    for i in course_list:
        if i.get_name() == c_name:
            return True


# ------------------------------ Menu -------------------------------------
print("Program started !!!")

def menu_option():
    print("""
============================================================================
Here are the menu option, please choose!!!!
    0. Exit
    1. Input information of students
    2. Input information of courses
    3. Input mark for students by courses
    4. Output information of students
    5. Output information of courses
    6. Output information for students course management """)  
menu_option()
option = int(input("Enter your choice: "))

while option != 0:
    if option == 1:
        option1()
        exit_menu()

    elif option == 2:
        option2()
        exit_menu()

    elif option == 3:
        option3()
        exit_menu()

    elif option == 4:
        print("All information of student in class: ")
        for i in std_list:
            print("Student's name = " + i.get_st_name(), end=". Student's ID = ")
            print(i.get_st_id(), end=". Date of Birth = " + i.get_st_dob())
            print()
        exit_menu()

    elif option == 5:
        print("All information of course: ")
        for i in course_list:
            print("Course's name = " + i.get_name(), end=". ID = ")
            print(i.get_id())
        exit_menu()

    elif option == 6:
        for i in stm_list:
            print("This is mark information of " + i.get_st_name() + ": ", end="")
            print(i.get_crs_inf())
        exit_menu()

    else:
        print("You choose option exit!!!")
        break