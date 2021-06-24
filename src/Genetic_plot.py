import numpy as np
import pandas as pd
from matplotlib import cm
from matplotlib import pyplot as plt

df_graph = pd.read_csv("../graph/exam2_output.csv")
df_gen = pd.read_csv("../graph/genetic_algorithm_output.csv")

#Contour
X1 = df_graph["x1"]
X2 = df_graph["x2"]
Z = np.array(df_graph['z'])

X1_gen = df_gen["x1"]
X2_gen = df_gen["x2"]

plt.tricontour(X1, X2, Z, 15, linewidths=0.5, colors='k')
plt.tricontourf(X1, X2, Z, 15, cmap=cm.jet)
plt.scatter(X1_gen, X2_gen, color="#FF0000", label="genetic_algor")

plt.title("Exam2 contour plot")
plt.legend()
plt.show()
