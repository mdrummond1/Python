"""while loop"""
i = 1
while i <=10:
    print(i)
    i += 1

print("finished while loop")

"""for loops"""
friends = ["Jim", "Brittany", "mom", "dad", "Sam"]
print("first loop\n")
for friend in friends:
    print(friend)

nums = [0]
print("second loop\n")
for i in range(11):
    nums.append(i)
    print(i)

print("third loop")

for i in range(len(nums)):
    print(nums[i])

print("fourth loop\n")

for index in range(len(friends)):
    print(friends[index])