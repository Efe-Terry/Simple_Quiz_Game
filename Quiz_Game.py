name = input('Hello! What is your name: ')

print(f'Hello {name}! Welcome to my computer game!')

playing = input('Do you want to play my simple game? inpute y or n: ')

if playing.lower() != 'y':
    print(f'Ok {name} Bye!')
    quit()

print(f'Okey {name}! Here we go *_*')

score = 0

question1 = input('Is Nigeria in Africa? y or n ')
if question1.lower() == 'y':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

question2 = input('Is Kenya in Africa? y or n ')
if question2.lower() == 'y':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

question3 = input('Is Canada in Africa? y or n ')
if question3.lower() == 'n':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

question4 = input('Is Ghana in Africa? y or n ')
if question4.lower() == 'y':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(f'Hello {name} You got {score} quiz correctly!')
print(f'You scored a totall of {(score/4) * 100}%!')