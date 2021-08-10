import random
guess = 0
while guess != 'q':
    guess = input('Enter a number (0-99) to guess or type q to quit: ')
    random_no = random.randint(1,100)
    if  guess == random_no:
        print('Correct! It was',guess )
        break
    else:
        print('No, it wasn\'t ',guess,' it was ',random_no,', please try again' )
