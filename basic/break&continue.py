import random
n = random.randrange(1,50)
# print(n)
i = 9

print("* - * - *  Start Game to press Enter  * - * - *\n")
print("Enter the number in 1 to 50 \n")
while True:
    if i >= 0:
        guess = int(input("Enter a number :-"))
        if guess:
            if n > guess:
                print("Please Try & Enter", guess, "Too high")
            elif n < guess:
                print("Please Try & Enter", guess, "Too low")
            else:
                print("you win...")
                print("Cong. you  complet", 10-i, "step")
                break
            print("you left chance", i, "\n")
            i -= 1
            continue
    else:
        print(" Game Over ")
        break