#solvetocheck.py
from odesolve import euler, rk4, solveto


#Defines the RHS of our ODE

def f(x,t):
	return x


#Asking the user for input values for the initial conditions and maximun stepsize for teh ODE

x0 = float(input("Please enter an initial value for x0: "))
hmax = float(input("Please enter a maximum stepsize to be used: "))
t0 = float(input("Please enter an intial value for t0: "))
t1 = float(input("Please enter a final t value: "))
method = euler

#Asking the user to specify which method to use for the solution approximation

inp = input("Enter 1 for Euler Method, or 2 for for Runge-Kutta: ")
if inp == "1":
    print("You chose Euler")
    method = euler
elif inp == "2":
    print("You chose rk4")
    method = rk4
else:
    print("You must choose between 1 or 2")


x1 = solveto(f, x0, t0, t1, hmax, method)

print('Solving the ODE dx/dt = x')
print('Initial condition x =', x0, 'when t =', t0)
print(method, 'method with a stepsize of h =', hmax, 'until t = ', t1)
print('Gives an estimate of x =', x1, 'when t =', t1)