



with open('input_day_5.txt') as f:
    # create an empty list to store the sublists
    instructions = []
    for line in f:
        words = line.split()
        sublist = []
        for word in words:
            # try to convert the word to an integer
            try:
                integer = int(word)
                # if the conversion succeeds, add the integer to the sublist
                sublist.append(integer)
            except ValueError:
                # if the conversion fails, do nothing
                pass
        instructions.append(sublist)


# define the data as a list
original_stacks = [
    ['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'],
    ['N', 'V', 'G', 'P', 'H', 'W', 'B'],
    ['F', 'W', 'B', 'J', 'G'],
    ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'],
    ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'],
    ['B', 'C', 'W', 'G', 'F', 'S'],
    ['H', 'T', 'P', 'M', 'Q', 'B', 'W'],
    ['F', 'S', 'W', 'T'],
    ['N', 'C', 'R']
    ]


def print_data(data):
    for j in data:
        print(f"{j}")

def move_crate(o_stacks, i_list):
    
    for instruction in i_list: 
        quantity, from_stack, to_stack = instruction
        
        loader = []
        if quantity > len(o_stacks[from_stack-1]):
            quantity = len(o_stacks[from_stack-1])
            loader = []
            for _ in range(quantity):
                if len(o_stacks[from_stack-1]) != 0:
                    crate = o_stacks[from_stack-1].pop()
                    loader.append(crate)
                else:   
                    pass
            
            for _ in range(len(loader)):
                if (len(loader)) != 0:
                    crate = loader.pop()
                    o_stacks[to_stack-1].append(crate) 
                else:
                    pass
        else: 
            loader = []
            for _ in range(quantity):
                if len(o_stacks[from_stack-1]) != 0:

                    crate = o_stacks[from_stack-1].pop()
                    loader.append(crate)
                else:   
                    pass
            for _ in range(len(loader)):
                if (len(loader)) != 0:

                    crate = loader.pop()
                    o_stacks[to_stack-1].append(crate)
                else:
                    pass
        
        
        
    print(print_data(o_stacks))
# def move_crate(o_stacks, i_list):
    
    
    # for instruction in i_list: 
    #     quantity, from_stack, to_stack = instruction
    #     for _ in range(quantity):
    #         if o_stacks[from_stack-1] != []:
    #             crate = o_stacks[from_stack-1].pop()
    #             o_stacks[to_stack-1].append(crate)
    #         else:
    #             pass
        
    # print(print_data(o_stacks))

move_crate(original_stacks, instructions)
# # A class to represent a crate in a linked list
# class Crate:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
        
# # A class to represent a stack of crates as a linked list
# class Stack:
#     def __init__(self):
#         self.top = None
        
#     def push(self, data):
#         self.top = Crate(data, self.top)
        
#     def pop(self):
#         if self.top is None:
#             return None
#         else:
#             data = self.top.data
#             self.top = self.top.next
#             return data
        
#     def peek(self):
#         if self.top is None:
#             return None
#         else:
#             return self.top.data

# # Function to simulate the movement of crates between linked lists
# # according to a given set of instructions
# def simulate_crates(og_data, instruct):
#     # The stacks of crates, initially empty
#     stacks = [Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack()]
    
#     # Add the starting crates to the stacks
#     for index, stack in enumerate(og_data):
#         for char in stack:
#             stacks[index].push(char)


#     for current, i in enumerate(instruct):
#         quantity, from_stack, to_stack = i
#         # if quantity > 10:
#             # print(f'quantity: {quantity}')
#             # print(f'from_stack: {from_stack}')
#             # print(f'to_stack: {to_stack}')


#         # for m in range(len(stacks)):
#         #     print(stacks[m].peek())
#         # print("--------")

        
#         # Move the specified number of crates from the from_stack to the to_stack

#         for _ in range(quantity):
#             # Remove the top crate from the from_stack and push it onto the to_stack

#             crate = stacks[from_stack-1].pop()
#             # if quantity > 10:
#                 # print(f"moving {crate} from stack {from_stack} to stack {to_stack}")
#             stacks[to_stack-1].push(crate)
#         # if quantity > 10:
#         #     print(f"from_stack {from_stack} is now {stacks[from_stack-1].peek()}\nto_stack {to_stack} is now {stacks[to_stack-1].peek()}")
    

#     for m in range(len(stacks)):
#             print(stacks[m].peek())
        



# # Simulate the movement of crates
# simulate_crates(original_stacks, instructions)