####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team 0'
strategy_name = 'collude but retaliate in odd way'
strategy_description = 'collude but if betrayed wait 1 turn then betray'

def move(my_history, their_history, my_score, their_score): 
  if my_history == 0:
    return 'c'
  elif my_history[-1]=='c' and their_history[-1]=='b':
    return 'c' 
  elif my_history[-1]== 'c'and their_history[-1]== 'c':
    return 'c'
  else:
    return 'b'