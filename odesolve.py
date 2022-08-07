# odesolve.py
#
# Author: <Nicholas Saremi>
# Date:   <01/08/2022>
# Description: <Using Numerical Methods (Euler and Runge Kutta) to solve Ordinary Differential Equations>
#
# You should fill out the code for the functions below so that they pass the
# tests in test_odesolve.py

def euler(f, x, t, h):
    return x + f(x , t )*h
    pass


def rk4(f, x, t, h):
    k1 = f(x, t)
    k2 = f(x + k1*(h/2), t + (h/2))
    k3 = f(x + k2*(h/2), t + (h/2))
    k4 = f(x + k3*h, t + h)
    return x + (k1 + 2*k2+ 2*k3 + k4)*(h/6)

	
	
    pass

def solveto(f, x0, t1, t2, hmax):      #, method=euler
    for i in range (0,_total_jumps):           
        x0= euler(f, x0, t1, hmax)
        t1 = t1 + hmax
        x1=x0
        #print(i)
    
        if i ==_total_jumps - 2 :
            hmax = hmin
        if t1 == t2:
            #print(x1)
            break
    return x1
    pass

solveto(f, x0, t1, t2, hmax)   



"""Use many steps of method to get from x1,t1 to x2,t2"""
    pass


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
    pass
