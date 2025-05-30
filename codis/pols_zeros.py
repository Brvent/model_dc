import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

L = 0.00085  
R = 5        
Kv = 0.083    
Ki = 0.083    
J = 2.5e-4    
b = 1.04e-3   

a2 = L * J
a1 = R * J + L * b
a0 = R * b + Kv * Ki

# Transferencia de velocidad angular
G_omega = ctrl.TransferFunction([Ki], [a2, a1, a0])

# Transferencia de torque
G_torque = ctrl.TransferFunction([Ki * J, Ki * b], [a2, a1, a0])

def plot_pz(sys, title, filename):
    zeros = ctrl.zeros(sys)
    poles = ctrl.poles(sys)
    plt.figure()
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='blue', label='Zeros')
    plt.scatter(np.real(poles), np.imag(poles), marker='x', color='red', label='Polos')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.savefig(filename, dpi=100, bbox_inches='tight')
    plt.show()

plot_pz(G_omega, "Polos y ceros de ω(s)/V(s)", "pz_w_v.png")
plot_pz(G_torque, "Polos y ceros de T(s)/V(s)", "pz_t_v.png")
