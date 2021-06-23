from CrackBox import Black_Box_Function
import numpy as np

crack = Black_Box_Function("input1.txt", "output1.txt", "6.exe")

def fx(x):
    f = crack.getFunction(x)
    return f

def dfx(x):
    step = 0.001
    diff = (fx(x+step)-fx(x-step))/(2*step)
    return diff

def dffx(x):
    step = 0.001
    diff = (fx(x+2*step)-2*fx(x+step)+fx(x))/(step**2)
    return diff

x = [4.75]
i = 0
ea = 100

print(fx(x[i]))

print("Iter\txi\tfx\tea")

while ea > 0.01:
    fpx = dfx(x[i])
    fppx = dffx(x[i])

    x.append(x[i]-fpx/fppx)
    fxx = fx(x[i])

    ea = np.abs((x[i+1]-x[i])/x[i+1]*100)

    print(f"{i+1}\t{x[i+1]:0.4f}\t{fxx:0.4f}\t{ea:0.4f}")

    i += 1

print(f"Answer is {x[i]:0.4f} and the minimum value is {fxx:0.4f}")
