import re

#r = raw string
pattern = r"eggs"

#match
if re.match(pattern, "baconeggseggs"):
    print("match!")
else:
    print("no match")

#search
if re.search(pattern, "baconeggseggsbacon"):
    print("match!")
else:
    print("no match")

#find all
print(re.findall(pattern, "baconeggseggsbacon"))

#find and replace
lis = "me nombre esta Juan. Hola yo estoy Juan"                
p1 = r"Juan"
newstring = re.sub(p1, "Rob", lis)
print(newstring)

def f_and_r(old, new, lis):
    pattern = r"{}".format(old)
    return re.sub(pattern, new, lis)
    
print(f_and_r("Rob", "Ted", newstring))
#. metacharacter = single placeholder
pattern = r"gr.y"
if re.match(pattern, "grny"):
    print("Match!")

#^ and $ metacharacters. ^ = start of string, $ = end of string
pattern = r"^gr.y$"
if re.match(pattern, "greyge"):
    print("Match!")

#character classes. ways to match a specific set of characters
pattern = r"[a-z][a-z][0-9]"
addr = "A4"
if re.match(pattern, addr.lower()):
    print("match!")

plate = r"[A-Z][A-Z][A-Z][0-9]"

if re.match(plate, "ABC123"):
    print("plate match")

#* metacharacter = any number of anything
pattern = r"eggs(bacon)*"

if re.match(pattern, "eggsbacon"):
    print("star match!")

#groups
group = r"bread(eggs)+bread"
if re.match(group, "breadeggsbread"):
    print("2 breads match!")
