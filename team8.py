####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Cash'
strategy_name = 'Make decision if there are more betrays then colludes'
strategy_description = 'This function will give b and c a value of 0 and if their history has a value that is higher then the value of collude, it will return likewise.' 

import random
    
def move(my_history, their_history, my_score, their_score):
    b = 0 
    c = 0
    for letter in their_history:
      if letter == 'b':
        b += 1
    for letter in their_history:
      if letter == 'c':
       c += 1
    if b > c:
      return 'b'
    else:
      return 'c'

