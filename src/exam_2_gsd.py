from CrackBox import Black_Box_Function
import numpy as np

crack = Black_Box_Function("input2.txt", "output2.txt", "2-6.exe")

def f(x):
    return crack.getFunction(x[0], x[1])

def gradient_f(x):
    step_size = 0.0001
    g_f = np.array([0.0, 0.0])

    for i in range(0, 2, 1):
        x_i = x.copy()
        x_i[i] += step_size
        g_f[i] = (f(x_i) - f(x))/step_size
    
    return g_f

if __name__ == "__main__":
    x = np.array([0.00784, -0.99608])
    
    k = 0
    error = np.matrix([1.0, 1.0])
    final_error = np.matrix([0.01, 0.01])
    gramma = 0.5

    hf = []

    hf.append(f(x))

    while (error.getA()[0][0] > final_error.getA()[0][0]):
        t = 1.0 #step_size
        dir = -1*gradient_f(x)

        error = np.matrix(dir)*np.matrix(dir).T

        norm_d = np.sqrt((np.matrix(dir)*np.matrix(dir).T))
        beta = gramma*norm_d**2

        phi_0 = f(x)
        x_old = x.copy()
        x = x_old + t*dir
        phi = f(x)
        
        while (phi > phi_0-t*beta):
            t /= 2.0
            x = x_old + t*dir
            phi = f(x)

        k += 1

        hf.append(f(x))

        print(f"iter: {k}\tdir: {-1*dir}\tx1: {x[0]:0.7f}\tx2: {x[1]:0.7f}\tf: {hf[k]:0.7f}")
