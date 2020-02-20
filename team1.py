####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'LostCauses' # Only 10 chars displayed.
strategy_name = '75-25'
strategy_description = '75% betray, 25% collude'
    
def move(my_history, their_history, my_score, their_score):
  '''This function makes it a 75% betray, 25% collude situation/strategy =, ir betrays to lower opponents score.'''
  opponent_b = 0 
  for decision in their_history:
    if decision == 'b':
      opponent_b+=1
  if len(their_history)==0:
    return "c"
  else:
    if opponent_b/len(their_history)>0.25 or their_score > my_score:
      return 'b'
    else:
      return 'c'
  print(opponent_b)

