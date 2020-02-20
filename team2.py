####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Wolves' # Only 10 chars displayed.
strategy_name = 'If collude, then collude. If betray, then betray twice'
strategy_description = 'One where if the opponent colludes, then this player will collude for the next turn. If the opponent betrays, this player will betray for the next 2 turns. This dependence on the opponent’s turn will be reset at the collude or the 2nd betrayal of this player. Betrayal is first turn'

def move(my_history, their_history, my_score, their_score):
  '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
  '''
  if len(my_history) == 0:
    return 'b'
  elif their_history[-1] == 'c':
    return 'c'
  elif their_history[-1] == 'b' or their_history[-2] == 'b':
    return 'b'
  else:
    return 'c'


