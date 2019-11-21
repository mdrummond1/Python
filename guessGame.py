secret_word = "giraffe"
guess = ""
count = 0
is_guessed = False

while guess != secret_word and count < 3 :
    guess = input("Enter guess: ")
    count += 1
    if guess == secret_word:
        is_guessed = True    

if is_guessed:
    print("You win!")
else:
    print("You lose!")