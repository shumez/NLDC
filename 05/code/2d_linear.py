# 2d linear

A = np.array([[2, 1],
              [3, 4]])

def x_dot(x, y, A):
    x_ = A[0,0]*x + A[0,1]*y
    return x_

def y_dot(x, y, A):
    y_ = A[1,0]*x + A[1,1]*y
    return y_

def speed(x, y, A): 
    s = x_dot(x, y, A)**2 + y_dot(x, y, A)**2
    s = np.sqrt(s)
    return s