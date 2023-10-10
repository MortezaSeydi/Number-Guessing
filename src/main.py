import random

number = round(random.random()*20)
score = 100
guesses = 3

first_input = f"""guess a number between 0 to 20 ==>:
you have {guesses} chances and your score is {score}'
"""
player_guess = int(input(first_input))

if player_guess == number:
    frist_correct = f"""congrats !!!
your guess was correct
your score is {score}
    """
    print(frist_correct)
    
    
elif player_guess != number:
    score -= 10
    guesses -= 1
    
    first_wrong_1 = f"""Your guess was wrong!
this is your first advice! :
***the number is an even number***
your score is {score}
try your next guess
you have {guesses} chance to guess
    """
    
    first_wrong_2 = f"""Your guess was wrong!
this is your first advice! :
***the number is an odd number***
your score is {score}
try your next guess
you have {guesses} chance to guess
    """
    
    if number % 2 == 0:
        print(first_wrong_1)
        
    elif number % 2 != 0:
        print(first_wrong_2)
        
    # secound guess
    player_guess = int(input('guess your secound chance ==>:'))
    
    diff = abs(player_guess-number)
    secound_correct = f"""congrats !!!
your guess was correct
your score is {score}'
    """
    score -= 10
    guesses -= 1
    
    secound_wrong = f"""your guess was wrong again !!
this is your secound advice!! :
***your guess is {diff} numbers greater or lower than the number!!***
your score is {score}
try your next guess
you have {guesses} chance to guess
    """
    
    if player_guess == number:
        print(secound_correct)
        
    elif player_guess != number:
        print(secound_wrong)
        
        player_guess = int(input('guess your last chance ==>:'))
        
        last_correct = f"""congrats you finaly did it !!!
your guess was correct
your score is {score}'
        """
        
        score = 0
        
        last_wrong = f"""your answer was wrong
you lost the game!!!
your score is {score}
the number was {number}
        """
        
        if player_guess == number:
            print(last_correct)
            
        elif player_guess != number:
            print(last_wrong)
