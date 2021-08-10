#Includes continue and break
#Executes code so long as the expression evaluates to true
x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Solstice!")

questions = ['Tell me your name: ', 'People like colour, what\'s yours? ','Lightsaber or Master Sword. Pick: ']
i = 0

#Break
while True:
    print("Type q to quit")
    a = input(questions[i])
    if a == 'q':
        break
    i = (i+1) % 3

#Continue
for i in range(1,6):
    if i == 3:
        #There are no droids here, move along
        print('no droids')
        continue
    print(i)

#Nesting loops 
for i in range(1,3):
    print(i)
    for letter in ['a','b','c']:
        print(letter)