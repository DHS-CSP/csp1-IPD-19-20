####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The Betrayals' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    history
    their_history: a string of the same length as history, possibly empty. 

    The most recent round is my_history
    
 will betray only 20% of the time 
    '''

    if 'b' in their_history[-10:]: #players version history  
        return 'b'             
    else:
        if random.random()<0.2: 
            return 'b'         
        else:
            return 'c'

 

