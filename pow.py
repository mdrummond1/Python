def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

user_base_num = int(input("enter a base number: "))
user_pow_num = int(input("enter an exponent number: "))

print(raise_to_power(user_base_num, user_pow_num))