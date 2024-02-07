number = 10

limit = 3

print(f"I'm thinking of a number... {limit} guesses left ")
guess = input("What number am I thinking of? ")
while True:
    
    if guess == str(number):
        print("Congratulations! You guessed the right number.")
        break
    elif guess == 'q':
        print('quit the game')
        break
    else:
        limit -= 1
        print(f"Sorry! Try again. {limit} guesses left")
        
        if limit == 0:
            print(f"OH NO MORE ATTEMPT, The correct number is {number}")
            break
        guess = int(guess)
        if guess > number:
            print(f"Sorry! Its too high.")
        else:
            print(f"Sorry! Its too low.")
    guess = input("What number am I thinking of? ")
