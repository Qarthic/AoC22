with open('Input_day_2.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

# a = Rock, 1
rps = {
    # key : [throw, tie, lose, win]
    'A': ["rock", 1, 3, 2],
    'B': ["paper", 2, 1, 3],
    'C': ["scissors", 3, 2, 1],
    'X': ["lose", 0],
    'Y': ["draw", 3],
    'Z': ["win", 6]
}
""" 
a,x = rock, 1
b,y = paper, 2
c,z = scissors, 3
"""

total_score = 0
round_result = 0
separate_games = []
for i in input_lines:
    separate_games.append(i.split())

test = [['A', 'X']]

for i in separate_games:
    opponent_throw = rps.get(i[0])
    my_guide = rps.get(i[1])

    if my_guide[0] == "lose":
        total_score += my_guide[1] + opponent_throw[2]
    elif my_guide[0] == "draw":
        total_score += my_guide[1] + opponent_throw[1]
    elif my_guide[0] == "win":
        total_score += my_guide[1] + opponent_throw[3]


print(total_score)
        

# for i in separate_games:
#     score = 0
#     opponent_throw = rps.get(i[0])
#     my_throw = rps.get(i[1])
#     if opponent_throw[0] == my_throw[0]: # tie
#         score = 3 + my_throw[1]
#         total_score += score
#     elif opponent_throw[0] == "rock" and my_throw[0] == "paper": #my rock beats paper
#         score = 6 + my_throw[1]
#         total_score += score
#     elif opponent_throw[0] == "rock" and my_throw[0] == "scissors":
#         score = 0 + my_throw[1]
#         total_score += score
#     elif opponent_throw[0] == "scissors" and my_throw[0] == "rock":
#         score = 6 + my_throw[1]
#         total_score += score
#     elif opponent_throw[0] == "scissors" and my_throw[0] == "paper":
#         score = 0 + my_throw[1]
#         total_score += score
#     elif opponent_throw[0] == "paper" and my_throw[0] == "scissors":
#         score = 6 + my_throw[1]
#         total_score += score
#     elif opponent_throw[0] == "paper" and my_throw[0] == "rock":
#         score = 0 +my_throw[1]
#         total_score += score
    
print(total_score)
    






