
import numpy as np
import matplotlib.pyplot as plt

t0=300
tau=[t0+i*30 for i in range(20)]
S1=[0.063,0.074,0.087,0.099,0.112,0.124,0.137,0.149,0.161,0.173,0.186,0.198,0.211,0.223,0.236,0.248,0.260,0.272,0.284,0.296] #mv
S2=[0.265,0.277,0.291,0.304,0.316,0.329,0.341,0.354,0.365,0.378,0.391,0.403,0.416,0.428,0.441,0.453,0.465,0.477,0.489,0.500] #mv

S=0.04
Vt=[abs(S1[i]-S2[i]) for i in range(20)]

S2=[S2[i]/S for i in range(20)]
Vt=[Vt[i]/S for i in range(20)]
print("Vt的平均值为：",np.mean(Vt))
print("dT/dt为：",S1[-1]-S1[0]/(0.04*5*60))
plt.figure(figsize=(8,8))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体


# plt.plot(tau,Vt)
# plt.xlim(t0-30,t0+600)
# plt.ylim(0,8)
# plt.title('ΔT-τ曲线（有机玻璃）')
# plt.xlabel('加热时间τ/s')
# plt.ylabel('温差ΔT/K')
# plt.show()

plt.plot(tau,S2)
plt.xlim(t0-30,t0+600)
plt.ylim(0,20)
plt.title('T-τ曲线（有机玻璃）')
plt.xlabel('加热时间τ/s')
plt.ylabel('中心面温度T/K')
plt.show()

