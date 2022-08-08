import numpy as np
from odesolve import solveto


#Define the RHS of our ODE

def f(X,t):
    x, y = X
    dxdt = y
    dydt = -x
    return np.array([dxdt, dydt])

#Initial Conditions
t0 = 0
x0 = 1
y0 = 0

X0 = np.array([x0, y0])
h = 0.5
t1 = 1
X1 = solveto(f, X0, t0, t1, h)
print(X1)
