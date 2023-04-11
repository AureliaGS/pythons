def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:    
        if guess.lower() == answer.lower():
            print('Correct answer')
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1

    if attempt == 3:
        print('The correct answer is ' + answer)

score = 0
print('Welcome to the Star Trek quiz!')
guess1 = input('What is Data\'s brother\'s name? ')
check_guess(guess1, 'Lore')
guess2 = input('What creature doesn\'t like Klingons?\n \
A)Vulcan\n B)Tribble\n C)Ferengi\n')
check_guess(guess2, 'B')
guess3 = input('In star trek next generation who is the captain? (His full name)')
check_guess(guess3, 'Jean Luc Picard')
guess4 = input('What is Worf\'s favorite drink ')
check_guess(guess4, 'prune juice')
guess5 = input('Data has a cat. True/False')
check_guess(guess5, 'True')
print('Your score is '+str(score))
