import numpy as np
from function1 import Equation

def fx(x):
    coef = Equation().coef
    intercept = Equation().intercept

    sum = 0
    for i, j in enumerate(coef):
        if(i >= 1):
            sum += x**i*j
    sum += intercept

    return sum

def dfx(x):
    step=0.001
    diff=(fx(x+step)-fx(x-step))/(2*step)
    return diff

def dffx(x):
    step=0.001
    diff=(fx(x+2*step)-2*fx(x+step)+fx(x))/(step**2)
    return diff

x=[4.75]
i=0
ea=100

print('Iter\txi\t\tfx\t\tea')

while ea>0.01:
    fpx=dfx(x[i])
    fppx=dffx(x[i])

    x.append(x[i]-fpx/fppx)
    fxx=fx(x[i])

    ea=np.abs((x[i+1]-x[i])/x[i+1]*100)

    print('%d\t%.4f\t%.4f\t%.4f'%(i+1,x[i+1],fxx,ea))

    i=i+1

print('Answer is x=%.4f and the minimum Value is %.4f'%(x[i],fxx))
