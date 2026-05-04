#BZ 1st Rock Paper Scissors
import random as r
from gui import gui
choices = ['There was an error!','rock','paper','scissors']
choice_map = {'Rock':1,'Paper':2,'Scissors':3}
choices_strings = ['There was an error!','Rock','Paper','Scissors']
actions = ['There was an error!',' smashed ',' smothered ',' snipped ',' consumed ']
rock_choices = ['rock','r','stone','smash','rock smash','destroy','obliterate']
scissors_choices = ['scissors','s','cut','snippy snip','snip']
paper_choices = ['paper','p','flap','flimsy','cover','papercut']
exit = True
score = 0
bot_score = 0
while True:
    try:
        choice = choice_map[gui(['### ROCK PAPER SCISSORS ###',f'You: {score}   Opponent: {bot_score}','[Rock','[Paper','[Scissors','[Exit'])]
    except:
        break
    computer_choice = r.randint(1,3)


    if choice - 1 == computer_choice:
        win_message = f'Your {choices[choice]}{actions[choice]}their {choices[computer_choice]}!'
        score += 1
    elif computer_choice - 1 == choice:
        win_message = f'Their {choices[computer_choice]}{actions[computer_choice]}your {choices[choice]}!'
        bot_score += 1
    elif computer_choice == 1 and choice == 3:
        win_message = f'Their {choices[computer_choice]}{actions[computer_choice]}your {choices[choice]}!'
        bot_score += 1
    elif choice == 1 and computer_choice == 3:
        win_message = f'Your {choices[choice]}{actions[choice]}their {choices[computer_choice]}!'
        score += 1
    elif choice == computer_choice:
        win_message = 'It\'s a tie!'
    else:
        win_message = 'The game bugged out. What kind of arcade is this?'
    gui([f'{choices[choice]} vs. {choices[computer_choice]}',win_message,'[Continue'])