employee_file = open("employees.txt", 'r+')
#could also use 'w', 'r', 'a' for write, read, append
#append doesn't affect previously written lines in file

emp = employee_file.read()

print("emp: " + str(emp))

employee_file.write("\nToby George, 74")

employee_file.close()