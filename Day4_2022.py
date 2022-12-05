with open('Input_day_4.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

responsibilities = []

for i in input_lines:
    responsibilities.append(i.split(','))
new_list = []
for j in responsibilities:
    new_list.append(j[0].split('-'))
    new_list.append(j[1].split('-'))

for n in range(len(new_list)):
    new_list[n][0] = int(new_list[n][0])
    new_list[n][1] = int(new_list[n][1])


answer = 0
for set in range(0, len(new_list), 2):
    current_set = new_list[set]
    compare = new_list[set+1]


    if current_set[0] in range(compare[0], compare[1]+1) or current_set[1] in range(compare[0], compare[1]+1):
        print(current_set)
        print(compare)
        answer += 1
        print(answer)
    elif compare[0] in range(current_set[0], current_set[1]+1) or compare[1] in range(current_set[0], current_set[1]+1):
        print(current_set)
        print(compare)
        answer += 1
        print(answer)
    else:
        pass
        
print(answer)



    # current = int(new_list[n]) + int(new_list[n+1])
    # new_list[n] = current

