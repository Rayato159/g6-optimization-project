from CrackBox import Black_Box_Function
import numpy as np

crack = Black_Box_Function("input2.txt", "output2.txt", "2-6.exe")

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

#bit >> [0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0]
chromosome = np.random.randint(high=2, low=0, size=16)

print(f"x1 = {getObjective(chromosome)[0]:0.4f}, x2 = {getObjective(chromosome)[1]:0.4f}, f(x1,x2) = {getObjective(chromosome)[2]:0.4f}")
