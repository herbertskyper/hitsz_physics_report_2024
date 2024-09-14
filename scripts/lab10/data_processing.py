D_left=[26.651,26.588,26.539,26.472,26.410,26.351,26.289,26.230,26.159,26.087,26.003,25.944,25.880,25.806,25.730,25.659,25.585,25.496,25.420,25.339,25.241,25.146]#31~30

D_right=[18.067,18.103,18.192,18.260,18.323,18.387,18.461,18.527,18.602,18.670,18.748,18.829,18.889,18.971,19.059,19.141,19.221,19.302,19.393,19.486,19.580,19.711]

delta_Dm2=[(D_left[i]-D_right[i])**2 for i in range(11)]
delta_Dn2=[(D_left[i]-D_right[i])**2 for i in range(11,22)]
delta_D=[delta_Dm2[i]-delta_Dn2[i] for i in range(11)]
print("平均数D：",sum(delta_D)/11)

lambda1=589.3*1e-6
print("曲率半径R：",sum(delta_D)/11/4/lambda1/11)

l1=[34.398,33.749,33.121,32.449,31.589]
l2=[28.642,27.493,26.620,26.011,26.209]
print("平均数l：",sum([l1[i]-l2[i] for i in range(5)])/5)