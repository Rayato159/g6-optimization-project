import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import pandas as pd

df = pd.read_csv("./exam1_output.csv")

x = df['X']
y = df['Y']

fig,ax = plt.subplots()

scatt = ax.scatter(x, y, c=y, cmap='hot')
ax.plot(x, y, color="#000000")

plt.title("Exam_1_graph")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
