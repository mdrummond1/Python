people = {"John":32, "Rob": 23}

numbers = {
    1: "one",
    2: "two",
    3: "three"
}

print("one" in numbers)
print(people["John"])
print(people["Rob"])

print(people["John"])
print(people.get("ted", "not here"))

print(numbers.items())
find = numbers.pop(1)
print("found {}".format(find))
print(numbers.get(1, "not here"))