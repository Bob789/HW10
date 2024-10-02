import random

print("Solution a")
print("create a list numbers between 95-105")
n_list: list[int] = [i for i in range(95,105+1)]
print(n_list)

print()
print("Solution b")
print("create a list of even numbers 10-20")
n_list: list[int] = [i for i in range(10, 20+1,2)]
print(n_list)


print()
print("Solution c")
print("Create a list of 5 random elements of False-True")
n_list: list[bool] = [random.choice([True,False]) for _ in range(5)]
print(n_list)


print()
print("Solution d")
print("Create a list of 10 random numbers between 1-100")
n_list: list[int] = [random.randint(1,100) for _ in range(10)]
print(n_list)


print()
print("Solution e")
print("Create a list of numbers greater then 50")
greater_then_50_list: list[int] = [numer for numer in n_list if 50 < numer]
print(greater_then_50_list)


print()
print("Solution f-> e+d")
print("Create a list of 10 random numbers between 1-100 + and show only numbers greater then 50")
greater_then_50_list: list[int] = [number for _ in range(10) if (number := random.randint(1,100)) > 50]
print(greater_then_50_list)


print()
print("Solution g")
print("Get strings from the user, create a list that contains all the letters the user entered, except for the letter 't' and spaces.")
letters: str = str(input("Enter string"))
letters_list: list[str] = [letter for letter in letters if " " != letter != "t"]
print(letters_list)


print("Solution h")
print("Create a list of 10 random numbers in the range 10-99, new list of units digit.")
numbers: list[str] = [str(random.randint(10,99)) for _ in range(10)]
unit_list: list[str] = [number[-1] for number in numbers]
print(f"List numbers {numbers}")
print(f"Unit_list {unit_list}")
