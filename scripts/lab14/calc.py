from math import cos, pi, sin

# -------------change these values----------------
d = 1/300
green = (((123, 45), (67, 12), (89, 34), (45, 56)),
         ((234, 23), (56, 45), (78, 12), (90, 34)),
         ((345, 12), (23, 45), (67, 56), (12, 34)))

yellow1 = (((123, 34), (56, 12), (78, 45), (90, 23)),
           ((234, 45), (67, 12), (89, 34), (45, 56)),
           ((345, 23), (56, 45), (78, 12), (90, 34)))

yellow2 = (((123, 12), (45, 34), (67, 56), (12, 23)),
           ((234, 45), (67, 12), (89, 34), (45, 56)),
           ((345, 23), (56, 45), (78, 12), (90, 34)))
# -----------------------------------------------

def decimal_deg(deg):
    return deg[0] + deg[1]/60

def psi_k(theta1, theta1_, theta2, theta2_):
    return 0.25*((theta1 - theta1_) + (theta2 - theta2_))

def lambda_(d, k, psi_k):
    return 1000000*(d*sin(pi*psi_k/180))/k

def relative_error(lambda_, lambda_0):
    return abs(lambda_ - lambda_0)/lambda_0

def d_k(d, k, psi_k):
    return k/(d*cos(pi*psi_k/180))

def calc1(data, theory_length):
    """计算问题一lambda的平均值，以及相对误差

    Args:
        data (tuple): 对应颜色光的测量数据
        theory_length (float): 对应颜色的光的波长标准值
    """    
    lambda_k_list = []
    for k in range(1,4):
        theta1, theta2, theta1_, theta2_ = [decimal_deg(deg_tuple) for deg_tuple in data[k-1]]
        # print(f'theta1 = {theta1}, theta2 = {theta2}, theta1_ = {theta1_}, theta2_ = {theta2_}')
        psi_k_ = psi_k(theta1, theta1_, theta2, theta2_)
        lambda_k = lambda_(d, k, psi_k_)
        lambda_k_list.append(lambda_k)
        print(f'k = {k}, psi_k = {psi_k_:.2f}, lambda_k = {lambda_k}')

    avg_lambda_k = sum(lambda_k_list)/3
    print(f'Average lambda_k = {avg_lambda_k:.2f}, Relative error = {100*relative_error(avg_lambda_k, theory_length):.4f}%')

def calc2(data):
    """计算角色散率

    Args:
        data (tuple): 对应颜色光的测量数据
    """    
    for k in range(1,4):
        theta1, theta2, theta1_, theta2_ = [decimal_deg(deg_tuple) for deg_tuple in data[k-1]]
        psi_k_ = psi_k(theta1, theta1_, theta2, theta2_)
        d_k_ = d_k(d, k, psi_k_)
        print(f'k = {k}, psi_k = {psi_k_:.2f}, d_k = {d_k_:.2f}')


calc1(green, 546.1)
calc1(yellow1, 577.0)
calc1(yellow2, 579.1)

calc2(yellow1)
calc2(yellow2)