from odesolve import rk4


def f(x,t):
	return x

#Initial conditions for rk4 method
t0 = 1
x0 = 1
h = 0.5
t1 = t0 + h
x1 = rk4 ( f, x0, t0, h)

print('Solving the ODE dx/dt = x')
print('Initial condition x =', x0, 'when t =', t0)
print('One step of the RK4 method with a stepsize of h =', h)
print('Gives an estimate of x =', x1, 'when t =', t1)