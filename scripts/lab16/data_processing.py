import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

alpha=[i*10 for i in range(0,10)]
I2=[2.43,2.40,2.23,1.90,1.52,1.12,0.70,0.36,0.12,0.01]
I2_calc=[2.43*np.cos(i*np.pi/180)**2 for i in alpha]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.plot(alpha,I2,label=r'$I_2$')
plt.plot(alpha,I2_calc,'-',label=r'$I_1cos^2\alpha$')
plt.legend()
plt.xlabel(r'相对角度/$^{\circ}$')
plt.ylabel(r'输出功率/$mW$')
plt.title('输出功率与夹角的关系')
plt.show()

U=[4+0.1*i for i in range(1,11)]
r=[95.18,95.18,94.58,93.98,93.37,89.76,83.73,63.86,50.60,41.57]

plt.plot(U,r)
plt.scatter(U,r)
# plt.legend()
plt.xlabel(r'电压/$V$')
plt.ylabel(r'透射率/$\%$')
plt.title('透射率与电压的关系')
plt.show()
