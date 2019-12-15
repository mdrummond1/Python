employee_file = open("employees.txt", "r+")

emp = employee_file.read()

print("emp: " + str(emp), end=" ")

employee_file.write("\nToby George, 74")

employee_file.close()