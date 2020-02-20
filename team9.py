####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'DrunkPig$s' # Only 10 chars displayed.
strategy_name = 'Collude first 20 rounds then based on opponents history decide what to do'
strategy_description = 'Collude first 20 rounds. Then if the opponenet has betrayed once during the 20 turns, check every move and retaliate based on their moves.'
     
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
    

def move_1(my_history, their_history, my_score, their_score):
  #Collude all the time till the 20th round
  if len(their_history)!=20:
    return c
  # If the betrayed in first 20 rounds, betray them
  if len(their_history)==20:
    if 'b' in their_history:
      return 'b'
      #After turn 20, check eery move and either retaliate or keep colluding.
      if len(their_history)>20:
        if their_history[-1]=='b':
          return 'b'
        else:
          return 'c'
    #If the opponent doesnt betray in first 20 turns collude until turn 100 then move depending on the opponents previous move.
    else:
      return 'c'
      if my_history==100:
        if their_history[-1]=='b':
          return 'b'
        else:
          return 'c'
