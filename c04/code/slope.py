# slope

"""
x_0:
	initial position

dt:
	dt float

iteration:
	integer
	
a:
	accerelation
	0 < a < 1

t:
	dt * iteration
	
"""

# class slope_field(object):
# 	"""docstring for slope_field"""
# 	def __init__(self, arg):
# 		super(slope_field, self).__init__()
# 		self.arg = arg
		

def slope(x_0, dt, iteration, a):
    x = np.array([x_0])
    t = np.array([0])
    
    for i in range(iteration):
        x_i = x[i]
        t_i = t[i]
        
        x_i = x_i + x_dot(x_i) * a
        t_i = t_i + dt
        
        x = np.append(x, np.array([x_i]))
        t = np.append(t, np.array([t_i]))
        
    return x, t