# 3 types - list/tuple/dictionary
# Lists are ITERABLE (can put them in a loop) and MUTABLE (can add/remove)

# List examples
empty = []
fruit = ["apple","banana", "pear","pop"]
# fruit[0] would retrieve apple
# Replace pear with lemon
fruit[2] = "lemon" 
# Remove the last item in the list, put it into variable
pop = fruit.pop 

# int/float/boo/str
types = [1,1.0,True,"string"]       

# Add an item
fruit.append("dragonfruit") 

# Add 2 lists
combined = fruit + types

# Check if an item is in a list
"apple" in combined
"strawberry" not in combined

# Find the size of the list
len(combined)


## Minigame!
##
colours = ["black","magenta","red","green"]
if input("Guess a colour: ") in colours:
    print("yup! Thats in my list")
else:
    print("no, go home loser")

artists=['a','b','c','d','e']
artists[4] = 'John Lennon'
artists.append('Paul Mccartney')