import numpy as np
import matplotlib.pyplot as plt

L = 0.00085   
R = 5         
Kv = 0.083    
J = 2.5e-4   
b = 1.04e-3   
T_load = 0.01 


def derivada_finita(y, t):
    dydt = np.zeros_like(y)
    for i in range(1, len(y)-1):
        dydt[i] = (y[i+1] - y[i-1]) / (t[i+1] - t[i-1])
    dydt[0] = (y[1] - y[0]) / (t[1] - t[0])
    dydt[-1] = (y[-1] - y[-2]) / (t[-1] - t[-2])
    return dydt

def calcular_omega(V, dIdt, I, L, R, Kv):
    return (V - L * dIdt - R * I) / Kv

def calcular_torque(omega, domega_dt, J, b, T_load):
    return J * domega_dt + b * omega + T_load


data = np.loadtxt("datos.txt", dtype=float, skiprows=1)
t = data[:, 0]
V = data[:, 1]
I = data[:, 2]

dIdt = derivada_finita(I, t)
omega = calcular_omega(V, dIdt, I, L, R, Kv)
domega_dt = derivada_finita(omega, t)
T = calcular_torque(omega, domega_dt, J, b, T_load)
#w(V)
plt.figure(figsize=(8, 6))
plt.plot(V, omega, '.', markersize=2)
plt.xlabel("Tensió V (V)", fontsize=18)
plt.ylabel("Velocitat angular ω (rad/s)", fontsize=18)
plt.grid()
plt.savefig('w_V.png', dpi=100, bbox_inches='tight')  
plt.show()

# T(V)
plt.figure(figsize=(8, 6))
plt.plot(V, T, '.', markersize=2)
plt.xlabel("Tensió V (V)", fontsize=18)
plt.ylabel("Torque T (Nm)", fontsize=18)
plt.ylim([-25, 25])  
plt.grid()
plt.savefig('T_V.png', dpi=100, bbox_inches='tight')  
plt.show()

# T(ω)
plt.figure(figsize=(8, 6))
plt.plot(omega, T, '.', markersize=2)
plt.xlabel("Velocidad angular w (rad/s)", fontsize=18)
plt.ylabel("Torque T (Nm)", fontsize=18)
plt.ylim([-25, 25])  
plt.grid()
plt.savefig('T_w.png', dpi=100, bbox_inches='tight')  
plt.show()
