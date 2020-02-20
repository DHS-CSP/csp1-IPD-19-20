####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Dolphins' # Only 10 chars displayed.
strategy_name = 'Half and Half unless betrayed in last 2 rounds'
strategy_description = 'This strategy has an equal chance to chose either betray or collude. However, if opposing team betrays within the last two rounds, our team will betray as well.'

import random

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    if 'b' in their_history[-2:]: # If the other player has betrayed within last 2 rounds, 
        return 'b'               # Betray.
    else:
        if random.random()<0.5: # 50% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'         # but 50% of the time collude

