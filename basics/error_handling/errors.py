try:
    num = int(input("Enter a number: "))
    value = 10/num
    print(value)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

finally:
    print("this script is finally over!!")

