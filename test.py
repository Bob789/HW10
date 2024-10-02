import random

# # comprehension
# print("create a list of even numbers 2,4,6...20")
# n_list: list[int] = [i for i in range(2, 20+1,2)]
# print(n_list)
#
# print()
# print("create a list of numbers 99,96,93...60")
# n_list: list[int] = [i for i in range(99, 59,-3)]
# print(n_list)
#
# print()
# print("create a list of 10 random numbers between 1-100")
# n_list: list[int] = [random.randint(1,100) for i in range(10)]
# print(n_list)
#
# print()
# print ("insert 3 numbers of the users")
# numbers_user: list[int] = [int(input("Enter number :")) for _ in range(3)]
# print(numbers_user)

# print()
# print(" A. Create a list of 10 random numbers between -50 to  +50")
# n_list: list[int] = [random.randint(-50,50) for i in range(10)]
# print(n_list)
#
# print()
# print(" B. Create a list from the list you created in ->a only with the even numbers")
# even_number_list: list[int] = [even_number for even_number in n_list if even_number % 2 == 0]
# print(even_number_list)
#
# print()
# print(" C. Create a list from the list you created in ->a only the positive numbers")
# positive_number_list: list[int] = [positive_number for positive_number in n_list if positive_number >= 0]
# print(positive_number_list)

# raise AttributeError(" big number")

# x: int = None
#
# while True:
#
#     try:
#         x = int(input("Enter number"))
#         break
#     except:
#         print("The number was Not ok ")
#
# print(f"After try .. the good number is {x}")


# height: float = 0
# while True:
#     try:
#         height = float(input("Enter numer :"))
#         if 1.4 <= height <= 3:
#             break
#         print("height not in range :")
#     except:
#         print("wrong height number, or range :")
#
# print(f"height is {height}")

print()
print("e. Handel wrong input str/index error")
SENTINEL = -999
n_list: list[int] = [152, 264, 341, 789]
while True:
    try:
        index_input: int = int(input("Enter index number number to show value contain "))
        if index_input == SENTINEL:
            break

        print(f"The value cell is: {n_list[index_input]}")

    except BaseException as e:
        print(f"Caught error: \033[91m{e}\033[0m")

print(f"well done the program run successful with out crushing")
