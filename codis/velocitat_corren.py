import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("datos.txt", dtype=float, skiprows=1)
t = data[:, 0]
V = data[:, 1]
I = data[:, 2]

plt.figure(figsize=(8, 6))
plt.plot(t, V, '-', markersize=2)
plt.xlabel("temps (s)", fontsize=18)
plt.ylabel("Tensió V (V)", fontsize=18)
plt.grid()
plt.savefig('velocitat.png', dpi=100, bbox_inches='tight')  
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(t, I, '-', markersize=2)
plt.xlabel("temps (s)", fontsize=18)
plt.ylabel("Corrent sI(A)", fontsize=18)
plt.grid()
plt.savefig('corrent.png', dpi=100, bbox_inches='tight')  
plt.show()

