import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import pandas as pd

#Contour
df = pd.read_csv("./exam2_output.csv")

X1 = df["x1"]
X2 = df["x2"]
Z = np.array(df['z'])

plt.tricontour(X1, X2, Z, 50, linewidths=0.5, colors='k')
plt.tricontourf(X1, X2, Z, 50, cmap=cm.jet)

plt.title("Exam2 contour plot")
plt.show()

#3D
X_b1 = df['x1']
X_b2 = df['x2']

Z = np.array(df['z'])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

my_cmap = plt.get_cmap('jet')

sctt = ax.scatter3D(X_b1, X_b2, Z, c = Z, cmap = my_cmap, marker ='o')

plt.title("Exam2 3D scatter plot")
plt.legend()
plt.show()
