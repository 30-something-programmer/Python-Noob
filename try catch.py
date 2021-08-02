x = input("Please type an integer: ")
try:
    x = int(x)
    print(x)
except ValueError:
    print("Please type an integer")