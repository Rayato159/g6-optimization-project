import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import pandas as pd

df = pd.read_csv("./exam2_output.csv")

X_b1 = df['x1']
X_b2 = df['x2']

Z = np.array(df['z'])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Creating color map
my_cmap = plt.get_cmap('jet')
 
# Creating plot
sctt = ax.scatter3D(X_b1, X_b2, Z,
                    alpha = 0.8,
                    c = (X_b1 + X_b2 + Z),
                    cmap = my_cmap,
                    marker ='o')

plt.grid()
plt.legend()
plt.show()
