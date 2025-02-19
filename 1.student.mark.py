# arrays containing info
students_id_list = []
students_info_list = []
courses_list = []
courses_id_list = []
marks = []

def NumOfStds():
    while True:
        num_of_students = int(input("Input number of students: "))
        if (num_of_students < 0):
            print("Invalid!")
        else:
            break
    return num_of_students

    # dictionary for student info
def CreateStudentDict(student_id, name, dob):
    aboutStudent = {
        "id": student_id,
        "name": name,
        "dob": dob
    }
    students_info_list.append(aboutStudent)
    students_id_list.append(student_id)

def NumOfCourses():
    while True:
        num_of_courses = int(input("Total number of courses: "))
        if num_of_courses < 0:
            print("Invalid!")
        else:
            break
    return num_of_courses

    # create a dictionary for course info
def CreateCourseDict(course_id, name):
    aboutCourse = {
        "id": course_id,
        "name": name
    }
    courses_list.append(aboutCourse)
    courses_id_list.append(course_id)

    # create a dictionary for marks
def CreateMarkDict(student_id, course_id, value):
    aboutMark = {
        "sid": student_id,
        "cid": course_id,
        "value": value
    }
    marks.append(aboutMark)

def StudentInfoQuery():
    while True:
        sid = input("Enter student ID: ")
        if len(sid) == 0 or sid is None:
            print("Invalid!")
        else:
            break
    if sid in students_id_list:
        print("Student ID already exists")
        exit()
    else:
        while True:
            name = input("Enter student name: ")
            if len(name) == 0 or name is None:
                print("Invalid!")
            else:
                break
        while True:
            dob = input("Enter student date of birth: ")
            if len(dob) == 0 or dob is None:
                print("Invalid!")
            else:
                break
        print(f"Student {name} successfully added!")
        CreateStudentDict(sid, name, dob)

def GetCourseInfo():
    while True:
        cid = input("Enter course ID: ")
        if len(cid) == 0 or cid is None:
            print("Invalid!")
        else:
            break
    if cid in courses_id_list:
        print("Invalid!")
        exit()
    else:
        while True:
            name = input("Enter course name: ")
            if len(name) == 0 or name is None:
                print("Invalid")
            else:
                break
        print(f"Successfully added course: {name}")
        CreateCourseDict(cid, name)

def GetCourseMarks(cid):
    for s in students_info_list:
        sid = s['id']
        while True:
            value = float(input(f"Enter marks for {s['name']}: "))
            if value < 0:
                print("Invalid")
            else:
                break
        CreateMarkDict(sid, cid, value)


def GetMarks():
    while True:
        cid = input("Enter Course ID for which you want to input marks: ")
        if cid in courses_id_list:
            if len(marks) > 0:
                marked = False
                for m in marks:
                    if m['cid'] == cid:
                        print("You have already input marks for this course")
                        marked = True
                        break
                if not marked:
                    GetCourseMarks(cid)
            else:
                GetCourseMarks(cid)
            break
        elif len(cid) == 0 or cid is None:
            print("Invalid!")
        else:
            print("No course found for the input ID")
            return -1


def PrintCourses():
    print("List of all Courses:")
    for c in courses_list:
        print("%s %s" % (c['id'], c['name']))

    print()


def PrintStudents():
    print("All Students in class:")
    for s in students_info_list:
        print("%s %s %s" % (s['id'], s['name'], s['dob']))

    print()


def PrintCourseMarks(cid):
    for m in marks:
        if m['cid'] == cid:
            sid = m['sid']
            for s in students_info_list:
                if s['id'] == sid:
                    print("%s %s %s" % (s['id'], s['name'], m['value']))


# Ask the user for the course ID whose mark should be listed, then invoke the PrintCourseMarks() function
def PrintMarks():
    while True:
        cid = input("Enter the course ID for which you want to see marks: ")
        if len(cid) == 0 or cid is None:
            print("Invalid!")
        else:
            break
    if cid in courses_id_list:
        PrintCourseMarks(cid)
    else:
        print("No course exists for the input ID")
        return -1


def main():
    print("1 = Input information students")
    print("2 = Input information courses")
    print("3 = Exit")
    print()
    myChoice = int(input("Enter your choice: "))
    while True:
        if myChoice == 1:
            num_of_stds = NumOfStds()
            for i in range(num_of_stds):
                print(f"-Student {i + 1}-")
                StudentInfoQuery()
            while len(courses_list) == 0:
                print("1 = Input courses' details")
                print("2 = Exit")
                myChoice2 = int(input("Enter your choice: "))
                if myChoice2 == 1:
                    num_of_courses = NumOfCourses()
                    for i in range(num_of_courses):
                        print(f"Course {i + 1}:")
                        GetCourseInfo()
                    break
                elif myChoice2 == 2:
                    exit()
                else:
                    print("Invalid choice!")
            break
        elif myChoice == 2:
            num_of_courses = NumOfCourses()
            for i in range(num_of_courses):
                print(f"Course {i + 1}:")
                GetCourseInfo()
            while len(students_info_list) == 0:
                print("1 = Input students' details: ")
                print("2 = Exit")
                myChoice2 = int(input("Enter your choice: "))
                if myChoice2 == 1:
                    num_of_stds = NumOfStds()
                    for i in range(num_of_stds):
                        print(f"Student {i + 1}:")
                        StudentInfoQuery()
                    break
                elif myChoice2 == 2:
                    exit()
                else:
                    print("Invalid choice!")
                    break
            break
        elif myChoice == 3:
            exit()
        else:
            print("Invalid choice!")
            exit()
    while len(marks) < len(students_info_list) * len(courses_list):
        print("1 = Input mark for a course")
        print("2 = Print students")
        print("3 = Print courses")
        print("4 = Exit")
        print()
        myChoice3 = int(input("Enter your choice: "))
        if myChoice3 == 1:
            GetMarks()
        elif myChoice3 == 2:
            PrintStudents()
        elif myChoice3 == 3:
            PrintCourses()
        elif myChoice3 == 4:
            exit()
        else:
            print("Invalid choice!")
    while True:
        print("1 = Print students")
        print("2 = Print courses")
        print("3 = Print marks of a course")
        print("4 = Exit")
        myChoice3 = int(input("Your choice: "))
        if myChoice3 == 1:
            PrintStudents()
        elif myChoice3 == 2:
            PrintCourses()
        elif myChoice3 == 3:
            PrintMarks()
        elif myChoice3 == 4:
            print("Exit")
            exit()
        else:
            print("Invalid choice!")

    # invoke main function
main()
