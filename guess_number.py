number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")
while True:
    
    if guess == str(number):
        print("Congratulations! You guessed the right number.")
        break
    elif guess == 'q':
        print('quit the game')
        break
    else:
        print(f"Sorry! Try again.")
    guess = input("What number am I thinking of? ")
