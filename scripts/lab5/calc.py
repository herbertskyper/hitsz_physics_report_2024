'''
考虑 L，H，D，Δ𝑚 ,Δx的A类不确定度，
d,Δx的AB类不确定度
'''

import pandas as pd
from math import sqrt
df = pd.read_excel("data.xlsx")

# Constants
g = 9.8
pi = 3.1415926
delta_m = 5

# values -----填这些值及同目录下data.xlsx-----
d0 = 0.002
L = 728.5
H = 687.4
D = 39.50

# code
df = df.fillna(d0)
print(df)

avg_d = (df['d'][0:6] - d0).sum()/6
print(f"avg_d = {avg_d}")
delta_x = df['x'][5:10].reset_index(drop=True) - df['x'][0:5].reset_index(drop=True)
avg_delta_x = delta_x.sum()/5
print(f'avg_delta_x = {avg_delta_x}')
# print((df['x'][5:10].reset_index(drop=True) - df['x'][0:5].reset_index(drop=True)).sum())
def E(delta_m, L, H, D, avg_d):
    return( 8*delta_m*g*L*H)/(pi*D*(avg_d**2)*avg_delta_x)

U_L = 0.8/sqrt(3)
E_L = U_L/L
print(f'E_L = {E_L}')
U_H = 0.8/sqrt(3)
E_H = U_H/H
print(f'E_H = {E_H}')
U_D = 0.02/sqrt(3)
E_D = U_D/D
print(f'E_D = {E_D}')
print(f"U_L = {U_L}\nU_H = {U_H}\nU_D = {U_D}")
# U_delta_m = 0.005/sqrt(3)
U_delta_x = 0.5/sqrt(3)

U_dA = sqrt(((df['d'][0:6]-d0-avg_d)**2).sum()/(6*(6-1)))
print(f'U_dA = {U_dA}')
U_db = 0.004/sqrt(3)
print(f'U_db = {U_db}')
U_d = sqrt(U_dA**2+U_db**2)
print(f'U_d = {U_d}')
E_d = U_d / avg_d
print(f'E_d = {E_d}')

U_xA = sqrt((((delta_x-avg_delta_x)**2).sum())/(5*4))
print(f'U_xA = {U_xA}')
U_xB = 0.5/sqrt(3)*sqrt(2)
print(f'U_xB = {U_xB}')
U_x = sqrt(U_xA**2+U_xB**2)
print(f'U_delta_x = {U_x}')
E_delta_x = U_x / avg_delta_x
print(f'E_delta_x = {E_delta_x}')

# print(f"U_L**2/L**2 = {(U_L**2)/(L**2)}")
E_res = 1000000 * E(delta_m, L, H, D, avg_d)
E_u = sqrt(U_L**2/L**2+U_H**2/H**2+U_D**2/D**2+(4*(U_d**2))/avg_d**2+U_x**2/avg_delta_x**2)
# print(f"U_delta_m = {U_delta_m}\n")
print(f"E = {E_res}")
print(f"E_u = {E_u}")
print(f"delta_uncertain_E = {E_res*E_u}")