# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_scored0 = 'Ruud Gullit'
player_scored1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_scored0 + ' ' + str(goal_0) + ', ' + player_scored1 + ' ' + str(goal_1)
print(scorers)

report = f'{player_scored0} scored in the {goal_0}nd minute\n{player_scored1} scored in the {goal_1}th minute'

player = 'Ronald Koeman'
first_name = player[:player.find(' ')]

last_name = player[(player.find('K')):len(player)]
last_name_len = len(player[player.find('K'):])

name_short = player[0] + '. ' + last_name

chant =  ((first_name + '! ') * len(first_name)).rstrip()
good_chant = chant[-1] != ' '




