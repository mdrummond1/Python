vowels = "aeiou"
def translate(phrase):
    translation = ""
    for letter in phrase:
        sub = "g"
        if letter.lower() in vowels:
            if letter.isupper():
                sub = "G"
            translation = translation + sub
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
