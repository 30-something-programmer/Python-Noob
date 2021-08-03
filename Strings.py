#Strings are IMMUTABLE - to modify it you need to replace them entirely

#Manipulation & concatination
string = "here "
string = string + "is a string"
print(string)
string_times_three = string * 3
print(string_times_three)

#Adding strings into another string using format
n1 = "noun"
v = "verb"
adj = "adj"
n2 = "noun"

r = """The {} {} the {} {}""".format(n1,v,adj,n2)
print(r)

#Splitting a string
sentences = "Here is a string. It has short sentences. And 3 full stops."
sentence1 = sentences.split(".")[0]
sentence2 = sentences.split(".")[1]

print(sentence1)
print(sentence2)

#Change cases
UPPERstring = string.upper()
LOWERstring = string.lower()
Capitalise_first_letter = string.capitalize()

#Joining a string another way
words = ["The", "fox", "jumped", "over","the","fence","."]
sentence = " ".join(words)  #Be sure to add the space/whatever to join

#Stripping gets rid of white space
s = "   HI   ".strip()
print(s)


#Strings are split into each character when using the square brackets:
print(string[0])   #will give "h" from "here is a string"
print(string[-1])  #will give "g" from "here is a string"


#If a string is more than one line, triple quotes are required
long_string = """Here is a string
on more than one line
works ok if you ask me"""

print(long_string)