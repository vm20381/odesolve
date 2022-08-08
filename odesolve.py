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

def solveto(f, x0, t0, t1, hmax, method = euler):    # method is originally set to euler, so if no method is chosen by the user, the default will be euler methdp


    _num_jumps = int((t1-t0)/hmax) # number of initial jumps if the step size divides equally into t2-t1
    hmin = 0

    if (t1-t0)/hmax > _num_jumps:  #Compare _num_jumps to its actual float value to see if it diides equally
    
        hmin = (t1-((hmax*_num_jumps) + t0)) #The size of the final smaller stepsize, required for the last jump   

    _total_jumps = _num_jumps + 1

    if method == rk4:
        for i in range (0,_total_jumps):         # iterating throught the step sizes  
            x0= rk4(f, x0, t0, hmax)
            t0 = t0 + hmax
            x1=x0
	      
            if i ==_total_jumps - 2:
                hmax = hmin			# changing the stepsize value so that t1 is reached
            if t0 == t1:
                print(x1)
	    
                break
        return x1
        pass
    else:

        for i in range (0,_total_jumps):           
            x0= euler(f, x0, t0, hmax)
            t0 = t0 + hmax
            x1=x0
                
            if i ==_total_jumps - 2 :
                hmax = hmin
            if t0 == t1:
                print(x1)
	    
                break
        return x1
        pass

  

   

def odesolve(f, X0, t, hmax, method=euler):

    solveto(f, X0, t0, t0+hmax,     



    """Compute the solution at different values of t"""
    pass
