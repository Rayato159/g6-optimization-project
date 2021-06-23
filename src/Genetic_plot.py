import numpy as np
import pandas as pd
from matplotlib import cm
from matplotlib import pyplot as plt

df_graph = pd.read_csv("../graph/exam2_output.csv")
df_gen = pd.read_csv("./Genetic_result.csv")

#Contour
X1 = df_graph["x1"]
X2 = df_graph["x2"]
Z = np.array(df['z'])

X1_gen = df_gen["x1"]
X2_gen = df_gen["x2"]
Z_gen = df_gen["z"]  

plt.scatter(X1_gen, X2_gen, Z_gen, color="#FF0000", label="genetic_algor")
plt.tricontour(X1, X2, Z, 15, linewidths=0.5, colors='k')
plt.tricontourf(X1, X2, Z, 15, cmap=cm.jet)

plt.title("Exam2 contour plot")
plt.show()