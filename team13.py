####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Rest Stop @ I=580'# Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
  '''Has a variable that is true. If it is ever set to false by abin their history, we will betray them unconditionally. ''' 
  trust = True
  for check in their_history: 
    if check != "c": 
      trust = False 
  if trust == False: 
    return "b" 
  else: 
    return "c"

