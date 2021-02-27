'''
Jacqueline Pezan 
NW Data Science Bootcamp
'''

# The list of candies to print to the screen
candy_list = [
    "Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
    "Skittles", "Hershey Bar", "Starbursts", "M&Ms"
]
# The amount of candy the user will be allowed to choose
allowance = 5
# The list used to store all of the candies selected inside of
candy_cart = []
# Print out options
print("hello user: pick five candies")
# print the list of candies
for x in range(allowance):
    c = 0
    for candy in candy_list:
        print(f"{c}: {candy}")
        c = c + 1
    # use input to get a candy
    choice = int(input("Select a candy?: "))
    # append candy to cart
    if choice >= 0 and choice < len(candy_list):
        candy_cart.append(candy_list[choice])
    else:
        print("bad choice; not in store")
# print cart
print()
print("Your cart contains:")
print(candy_cart)# The list of candies to print to the screen
candy_list = [
    "Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
    "Skittles", "Hershey Bar", "Starbursts", "M&Ms"
]
# The amount of candy the user will be allowed to choose
allowance = 5
# The list used to store all of the candies selected inside of
candy_cart = []
# Print out options
print("hello user: pick five candies")
# print the list of candies
for x in range(allowance):
    c = 0
    for candy in candy_list:
        print(f"{c}: {candy}")
        c = c + 1
    # use input to get a candy
    choice = int(input("Select a candy?: "))
    # append candy to cart
    if choice >= 0 and choice < len(candy_list):
        candy_cart.append(candy_list[choice])
    else:
        print("bad choice; not in store")
# print cart
print()
print("Your cart contains:")
print(candy_cart)