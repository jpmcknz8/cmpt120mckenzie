# guessing-game.py
animal = 'jaguar'
finish = 'quit'
while animal != 'animal_guess':
    print('I am thinking of an animal. Guess which animal')
    animal_guess = input()
    if (animal_guess.lower() != animal and animal_guess.lower()[0]!=finish [0]):
        print("Incorrect animal, try again.type quit to give up")
    elif animal_guess.lower()[0] == finish[0]:
        print('Adios!')
        break
    else:
        print("Correct animal")
        break
