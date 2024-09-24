import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


L_1=0.130
N1_1=150
R1_1=6.8
N2_1=150
S_1=1.24*1e-4
R2_1=68*1e3
C_1=6.8*1e-6

Ux1_1=[349,259,186,113,42.7,-30.7,-90.7,-121,-184,-337]
Uy1_1=[11.4,10.6,10.2,8.6,6.2,2.0,-2.80,-5.00,-8.00,-12.2]

Ux1_2=[-337,-257,-151,-34.0,29.3,72.7,126,179,246,293,339,349]
Uy1_2=[-12.1,-11.8,-10.6,-6.8,-3.4,-0.00,4.00,6.08,8.80,10.2,11.0,11.4]

Ux1_0=[349,313,273,246,209,166,126,103,86,42.7,0]
Uy1_0=[11.4,10.2,9.6,8.8,7.6,6.2,4.8,3.4,2.2,0.8,0]



H1_1=[Ux1_1*N1_1/L_1/R1_1*1e-3 for Ux1_1 in Ux1_1]
B1_1=[Uy1_1*R2_1*C_1/S_1/N2_1*1e-3 for Uy1_1 in Uy1_1]
H1_2=[Ux1_2*N1_1/L_1/R1_1*1e-3 for Ux1_2 in Ux1_2]
B1_2=[Uy1_2*R2_1*C_1/S_1/N2_1*1e-3 for Uy1_2 in Uy1_2]
H1_0=[Ux1_0*N1_1/L_1/R1_1*1e-3 for Ux1_0 in Ux1_0]
B1_0=[Uy1_0*R2_1*C_1/S_1/N2_1*1e-3 for Uy1_0 in Uy1_0]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建插值函数
interp1_1 = interp1d(H1_1, B1_1, kind='cubic')
interp1_2 = interp1d(H1_2, B1_2, kind='cubic')
interp1_0 = interp1d(H1_0, B1_0, kind='cubic')

# 生成插值点
H1_1_new = np.linspace(min(H1_1), max(H1_1), 500)
B1_1_new = interp1_1(H1_1_new)

H1_2_new = np.linspace(min(H1_2), max(H1_2), 500)
B1_2_new = interp1_2(H1_2_new)

H1_0_new = np.linspace(min(H1_0), max(H1_0), 500)
B1_0_new = interp1_0(H1_0_new)

# 绘制插值曲线
plt.figure(figsize=(12, 8))

plt.plot(H1_1_new, B1_1_new, label='曲线 1_1', color='blue')
plt.plot(H1_2_new, B1_2_new, label='曲线 1_2', color='blue')
plt.plot(H1_0_new, B1_0_new, label='曲线 1_0', color='red')

# 添加数据点
plt.scatter(H1_1, B1_1, color='blue', s=10)
plt.scatter(H1_2, B1_2, color='blue', s=10)
plt.scatter(H1_0, B1_0, color='red', s=10)

plt.xlabel('H(A/m)')
plt.ylabel('B(T)')
plt.title('样品1')
plt.show()


L_1=0.075
N1_1=150
R1_1=6.8
N2_1=150
S_1=1.20*1e-4
R2_1=68*1e3
C_1=8.8*1e-6


Ux2_1=[645,532,219,92,-81.3,-235,-315,-415,-481,-628]
Uy2_1=[17.8,17.4,15.4,13.6,10.8,5.80,1.40,-5.6,-10.4,-18.6]

Ux2_2=[-628,-275,-54.7,132,239,305,359,405,459,519,599,645]
Uy2_2=[-18.6,-16.8,-14.6,-10.8,-7.20,-3.60,0,3.4,7.00,11.4,15.0,17.8]

Ux2_0=[645,585,532,485,452,392,345,305,259,205,0]
Uy2_0=[17.8,16.6,15.4,13.4,12.6,11.0,8.80,7.00,5.00,3.20,0]

H2_1=[Ux2_1*N1_1/L_1/R1_1*1e-3 for Ux2_1 in Ux2_1]
B2_1=[Uy2_1*R2_1*C_1/S_1/N2_1*1e-3 for Uy2_1 in Uy2_1]
H2_2=[Ux2_2*N1_1/L_1/R1_1*1e-3 for Ux2_2 in Ux2_2]
B2_2=[Uy2_2*R2_1*C_1/S_1/N2_1*1e-3 for Uy2_2 in Uy2_2]
H2_0=[Ux2_0*N1_1/L_1/R1_1*1e-3 for Ux2_0 in Ux2_0]
B2_0=[Uy2_0*R2_1*C_1/S_1/N2_1*1e-3 for Uy2_0 in Uy2_0]

interp2_1 = interp1d(H2_1, B2_1, kind='cubic')
interp2_2 = interp1d(H2_2, B2_2, kind='cubic')
interp2_0 = interp1d(H2_0, B2_0, kind='cubic')

H2_1_new = np.linspace(min(H2_1), max(H2_1), 500)
B2_1_new = interp2_1(H2_1_new)

H2_2_new = np.linspace(min(H2_2), max(H2_2), 500)
B2_2_new = interp2_2(H2_2_new)

H2_0_new = np.linspace(min(H2_0), max(H2_0), 500)
B2_0_new = interp2_0(H2_0_new)

# 绘制插值曲线
plt.figure(figsize=(12, 8))

plt.plot(H2_1_new, B2_1_new, label='曲线 1_1', color='blue')
plt.plot(H2_2_new, B2_2_new, label='曲线 1_2', color='blue')
plt.plot(H2_0_new, B2_0_new, label='曲线 1_0', color='red')

# 添加数据点
plt.scatter(H2_1, B2_1, color='blue', s=10)
plt.scatter(H2_2, B2_2, color='blue', s=10)
plt.scatter(H2_0, B2_0, color='red', s=10)

plt.xlabel('H(A/m)')
plt.ylabel('B(T)')
plt.title('样品2')
plt.show()



