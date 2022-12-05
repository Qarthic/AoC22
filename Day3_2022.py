import string

with open('Input_day_3.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

rucksacks = []

for i in input_lines:
    rucksacks.append(i.split())
priority = list(string.ascii_lowercase)
priority_upper = list(string.ascii_uppercase)

for i in priority_upper:
    priority.append(i)


groups = [input_lines[x:x+3] for x in range(0, len(input_lines), 3)]

answer = 0

for x in groups:
    for y in x[0]:
        if y in x[1] and y in x[2]:
            answer += 1
            answer += priority.index(y)
            break

print(answer)

# Answer to part 1
#  for i in input_lines:    
#     firstpart, secondpart = i[:int(len(i)/2)], i[int(len(i)/2):]

#     for x in firstpart:
#         if x in secondpart:
#             answer += 1
#             answer += priority.index(x)
#             break

# print(answer)
