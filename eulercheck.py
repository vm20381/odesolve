#eulercheck.py
from odesolve import euler

#Defines the RHS of our ODE

def f(x,t):
	return x

#Initial Conditions
t0 = 1
x0 = 1
h = 0.5
t1 = t0 + h
x1 = euler(f, x0, t0, h) 	# This gves us x1 = x0 +f(x,t)*h

print('Solving the ODE dx/dt = x')
print('Initial condition x =', x0, 'when t =', t0)
print('One step of the euler method with a stepsize of h =', h)
print('Gives an estimate of x =', x1, 'when t =', t1)
