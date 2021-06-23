from CrackBox import Black_Box_Function
import numpy as np

def f(decode_x1, decode_x2):
    return crack.getFunction(decode_x1, decode_x2)

def getObjective(chromosome):
    lb_x = -2
    ub_x = 2
    len_x = len(chromosome)//2
    precision_x = (ub_x - lb_x)/(2**len_x - 1)

    z = 0
    t = 1
    x_bit = 0
    x1_bit_sum = 0

    for i in range(len(chromosome)//2):
        x_bit = chromosome[-t]*(2**z)
        x1_bit_sum += x_bit
        z += 1
        t += 1
    
    z = 0
    t = 1 + len(chromosome)//2
    x_bit = 0
    x2_bit_sum = 0

    for i in range(len(chromosome)//2):
        x_bit = chromosome[-t]*(2**z)
        x2_bit_sum += x_bit
        z += 1
        t += 1

    decode_x1 = (x1_bit_sum) * precision_x + lb_x
    decode_x2 = (x2_bit_sum) * precision_x + lb_x

    return (decode_x1, decode_x2, f(decode_x1, decode_x2))

crack = Black_Box_Function("input2.txt", "output2.txt", "2-6.exe")

#bit >> [0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0]
chromosome = np.random.randint(high=2, low=0, size=16)

population = 16
all_solution = np.empty((0, len(chromosome)))

for i in range(population):
    np.random.shuffle(chromosome)
    all_solution = np.vstack((all_solution, chromosome))

print(all_solution, end="\n\n")

#Tournament selection
parents = np.empty((0, np.size(all_solution, 1)))

for i in range(2):
    indices_list = np.random.choice(len(all_solution), 3, replace=False)

    print(f"round {i+1}# {indices_list}", end="\n\n")

    posb_parent_1 = all_solution[indices_list[0]]
    posb_parent_2 = all_solution[indices_list[1]]
    posb_parent_3 = all_solution[indices_list[2]]

    print(posb_parent_1)
    print(posb_parent_2)
    print(posb_parent_3)
    print()

    obj_func_parent_1 = getObjective(posb_parent_1)[2]
    obj_func_parent_2 = getObjective(posb_parent_2)[2]
    obj_func_parent_3 = getObjective(posb_parent_3)[2]

    print(obj_func_parent_1)
    print(obj_func_parent_2)
    print(obj_func_parent_3)
    print()

    min_obj_func = min(obj_func_parent_1, obj_func_parent_2, obj_func_parent_3)

    if min_obj_func == obj_func_parent_1:
        selected_parent = posb_parent_1
    elif min_obj_func == obj_func_parent_2:
        selected_parent = posb_parent_2
    else:
        selected_parent = posb_parent_3
        
    print(f"winner is {selected_parent}")
    print(f"minimum value is {min_obj_func}")

    parents = np.vstack((parents, selected_parent)) 
