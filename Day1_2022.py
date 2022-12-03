
with open('Input_day_1.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

elves_total_cal = 0
elves = [[]]

def elf_inventory(arr):
    switch = 0
    int_switch = 0  
    for line in arr:
        if line != '':
            elves[switch].insert(int_switch, int(line))
            int_switch += 1
        else:
            switch += 1
            int_switch = 0
            elves.insert(switch, [])
    return(elves)


def top_3_elf_cal(arr):
    elves = elf_inventory(arr)
    switch = 0
    for _ in elves:
        while switch < len(elves):
            elves[switch] = sum(elves[switch])
            switch += 1
    top_3 = []
    switch = 0
    
    elves.sort()
    for i in range(3):
        top_3.insert(switch, elves[-(switch+1)])
        switch += 1
    return(sum(top_3))

print(top_3_elf_cal(input_lines))

# def max_cal_elf(arr):
#     elves = elf_inventory(arr)
#     switch = 0
#     for _ in elves:
#         while switch < len(elves):
#             elves[switch] = sum(elves[switch])
#             switch += 1
#     return(max(elves))