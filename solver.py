import numpy as np

def analytical_solver(a,b,c,d):
    if a == 0:
        if b == 0:
            if c == 0:
                roots = []
            else:
                roots = __analytic_linear_solver(c,d)
        else:
            roots = __analytic_quadratic_solver(b,c,d)
    else:
        roots = __analytic_cubic_solver(a,b,c,d)
    return roots

def __analytic_linear_solver(c,d):
    root = -d/c
    roots = [root]
    return roots

def __analytic_quadratic_solver(b,c,d):
    if c*c - 4*b*d == 0:
        root = -c/(2*b)
        roots = [root]
    elif c*c - 4*b*d < 0:
        roots = []
    else:
        root1 = (-c + np.sqrt(c*c - 4*b*d))/(2*b)
        root2 = (-c + np.sqrt(c*c - 4*b*d))/(2*b)
        roots = [root1, root2]
    return roots
    
def __analytic_cubic_solver(a,b,c,d):
    pass
    
def root_solver(self):
    pass

def newton_method(self):
    pass

