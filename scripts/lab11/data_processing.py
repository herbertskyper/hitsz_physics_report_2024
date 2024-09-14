import matplotlib.pyplot as plt

I=[i*0.25 for i in range(12)]

theta1=[9.8,8.1,7.5,4.5,3.4,2.3,0.6,-0.9,-3.5,-4.9,-6.8,-7.4]
delta_theta1=[]
delta_theta1.append(0)
for i in range(1,12):
    delta_theta1.append(theta1[i]-theta1[i-1])
print("delta_theta1:",delta_theta1)
# plt.figure(figsize=(8,8))
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.title("磁致旋光角与励磁电流大小的关系")
# plt.xlabel("电流大小/A")
# plt.ylabel("旋光角Δθ/°")
# plt.plot(I,delta_theta1)
# plt.show()

theta2=[328.5,326.5,324.8,323.4,321.8,320.4,317.5,316.5,315.7,314.3,312.8,310.0]
delta_theta2=[]
delta_theta2.append(0)
for i in range(1,12):
    delta_theta2.append(theta2[i]-theta2[i-1])
print("delta_theta2:",delta_theta2)
# plt.figure(figsize=(8,8))
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.title("磁致旋光角与励磁电流大小的关系")
# plt.xlabel("电流大小/A")
# plt.ylabel("旋光角Δθ/°")
# plt.plot(I,delta_theta2)
# plt.show()

theta3=[11.3,13.5,14.8,15.2,18.1,19.1,20.8,22.0,23.3,25.1,27.4,28.8]
delta_theta3=[]
delta_theta3.append(0)
for i in range(1,12):
    delta_theta3.append(theta3[i]-theta3[i-1])
print("delta_theta3:",delta_theta3)
# plt.figure(figsize=(8,8))
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# plt.title("磁致旋光角与励磁电流大小的关系")
# plt.xlabel("电流大小/A")
# plt.ylabel("旋光角Δθ/°")
# plt.plot(I,delta_theta3)
# plt.show()

