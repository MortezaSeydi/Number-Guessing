import random

number = round(random.random() * 20)
score = 100
guesses = 3

player_guess = int(
    input(
f'guess a number between 0 to 20 ==>:\n\
you have {guesses} chances and your score is {score}'
    )
)

if player_guess == number:
    print(
f'congrats !!!\n\
your guess was correct\n\
your score is {score}'
    )
    
elif player_guess != number:
    score -= 10
    guesses -= 1
    
    if number % 2 == 0:
        print(
f'this is your first advice! :\n\
***the number is an even number***\n\
your score is {score}\n\
try your next guess\n\
you have {guesses} chance to guess'
        )
        
    elif number % 2 != 0:
        print(
f'this is your first advice! :\n\
***the number is an odd number***\n\
your score is {score}\n\
try your next guess\n\
you have {guesses} chance to guess'
        )
        
    player_guess = int(
        input(
             'guess your secound chance ==>:'
        )
    )
    
    diff = abs(player_guess - number)
    
    if player_guess == number:
        print(
f'congrats !!!\n\
your guess was correct\n\
your score is {score}'
        )
        
    elif player_guess != number:
        score -= 10
        guesses -= 1
        print(
f'this is your secound advice!! :\n\
***your guess is {diff} numbers greater or lower than the number!!***\n\
your score is {score}\n\
try your next guess\n\
you have {guesses} chance to guess'
        )
        
        player_guess = int(
            input(
                'guess your last chance ==>:'
                )
            )
        if player_guess == number:
            print(
f'congrats !!!\n\
your guess was correct\n\
your score is {score}'
            )
            
        elif player_guess != number:
            score = 0
            print(
f'your answer was wrong\n\
you lost the game!!!\n\
your score is {score}\n\
the number was {number} '
                )
            
            
    