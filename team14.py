####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
team_name = 'Pencils' # Only 10 chars displayed.
strategy_name = 'Get you reward'
strategy_description = 'One Betrays while the other colludes, so they get a reward, + 100 points, since the first person to decide chooses betray and next collude, which is the right combo to get off clean and get a reward.'

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
    if 'b' in their_history:
      return 'c'
    elif their_score == 100:
      return 'c'
    else:
      return 'b'
