import random
secret_number = random.randint(1, 10)
attempts = 3
print('Welcome to the Number Guessing Game! \n Guess a number between 1 and 10. \n You have 3 attempts.' )

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess < 1 or guess > 10:
        print("Invalid guess! Enter a number between 1 and 10.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        break

    elif guess > secret_number:
        print("Your guess is too high!")

    else:
        print("Your guess is too low!")

    attempts -= 1
    print("Attempts remaining:", attempts)

else:
    print("Better luck next time!")
    print("The secret number was:", secret_number)


# Multiplication Table Generator

number = int(input('Enter a number: '))
for i in range (1, 11):
    result= number * i
    print (number, "x", i, "=", result)


# BMI Calculator
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in meters '))
bmi = calculate_bmi(weight, height)
print("Your BMI is:", round(bmi, 2))