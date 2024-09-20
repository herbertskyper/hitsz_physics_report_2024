import matplotlib.pyplot as plt
import numpy as np


v=[8.216,7.410,6.882,5.492,5.196]
# v=[v*1e14 for v in v]

U1=[-1.940,-1.332,-1.127,-0.745,-0.620]
U2=[-2.029,-1.525,-1.315,-0.863,-0.774]
U3=[-2.024,-1.573,-1.383,-0.890,-0.810]



A = np.vstack([v, np.ones(len(v))]).T
k, b = np.linalg.lstsq(A, U3, rcond=None)[0]

print(f"斜率 (k): {k}")
print(f"截距 (b): {b}")

e = -1.602e-19
h0=6.626e-34
h=e*k*1e-14
print(f"普朗克常数 (h): {h}")
print(f"相对误差",abs(h-h0)/h0)
# v = np.array(v)
# U = np.array(U3)

# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.scatter(v, U3, color='blue', label='数据点')
# plt.plot(v, k * v + b, color='red', label='拟合直线')
# plt.xlabel('频率 (Hz)')
# plt.ylabel('电压 (V)')
# plt.title('直径为4mm时电压与频率的关系')
# plt.legend()
# plt.show()