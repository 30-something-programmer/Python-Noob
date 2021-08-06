#A for-loop is known as iterating (going through line by line)
name = "Bish AFC"

#Goes through each character
for char in name:
    print(char)

#Goes through each item in the list - same for tuples
shows = ["GOT","DBZ","The Witcher"]
for show in shows:
    print(show)

#See what it does with dictionaries
people = {"GOT":"Denyrys","DBZ":"Goku","The Witcher":"Geralt"}
for show in people:
    print(show)

#How to manipulate lists in a for loop
i = 0
for show in shows:
    shows[i] = show.upper()
    print(shows[i])
    i += 1

#creating a range
i = 0
for i in range (1,11):
    print(i)