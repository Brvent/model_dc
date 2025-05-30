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

# ω(s)/V(s)
num_omega = [Ki]
den = [a2, a1, a0]
G_omega = ctrl.TransferFunction(num_omega, den)

# T(s)/V(s)
num_torque = [Ki * J, Ki * b]
G_torque = ctrl.TransferFunction(num_torque, den)

plt.figure(figsize=(8, 6))
ctrl.bode_plot(G_omega, dB=True, Hz=False, omega_limits=(1, 1e4), omega_num=1000)
plt.savefig('bode_w_v.png', dpi=100, bbox_inches='tight')

plt.figure(figsize=(8, 6))
ctrl.bode_plot(G_torque, dB=True, Hz=False, omega_limits=(1, 1e4), omega_num=1000)
plt.savefig('bode_T_v.png', dpi=100, bbox_inches='tight')
plt.show()
