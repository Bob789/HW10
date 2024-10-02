# a. The try except give us option to handle errors by prevent program to crush
from sys import exception

# b. If you catch the error you can decide how to handle the error so the program will not crush

# c. כתוב קטע קוד המחלק את ה מספר 88 ב- אפס, ואז עטוף אותו ב - except try

try:
    x = 88 / 0
except ZeroDivisionError as e:
    print(f"\033[31mTher was error {e} we should not divide by 0\033[0m")


print()
print("d. snippet raises an error")
while True:
    try:
        wrong_input: int = int(input("Enter negative number"))
        if  wrong_input > -1:
            raise ValueError(f"\033[91mYou do not type negative number {wrong_input}\033[0m")
        break
    except BaseException as e:
        print(f"Caught error: {e}")

print(f"well done you enter negative number {wrong_input}")



print()
print("e. Handle wrong input str/index error")
SENTINEL = -999
n_list: list[int] = [152, 264, 341, 789]

while True:
    try:
        index_input: int = int(input("Enter index number to show value contained: "))  # Corrected message
        if index_input == SENTINEL:
            break

        print(f"The value in the cell is: {n_list[index_input]}")  # Improved clarity

    except BaseException as e:
        print(f"Caught error: \033[91m{e}\033[0m")

print("Well done! The program ran successfully without crashing.")  # Corrected spelling and phrasing
