"""comparisons"""
def max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def sameStr(string1, string2):
    if string1 == string2:
        return True
    else:
        return False

blue = False
is_tall = True

if blue and is_tall:
    print("it's blue! You tall, man")
elif is_tall and not(blue):
    print ("You're a short non-blue person")
else:
    print("It's not blue, or you're a shorypants")

print("max: " + str(max(3, 4, 5)))

print("same String: " + str(sameStr("green", "food")))

