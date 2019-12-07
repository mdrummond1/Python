from student import Student

s1 = Student("Fred", "CS", 3.65, False)

s2 = Student("Pam", "Art", 2.5, True)

print(s1.gpa)
eprint(s2.gpa)

course = [s1, s2]

for student in course:
    print("name: " + student.name)
    print("major: " + student.major)
    print("gpa: "  + str(student.gpa))
    print("on probation: " + str(student.is_on_probation))
    print("\n")
