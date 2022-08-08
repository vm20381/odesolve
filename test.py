import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
##%matplotlib inline

# Define parameters
f = lambda t, x: np.exp(-t) # ODE
h = 0.1 # Step size
t = np.arange(0, 1 + h, h) # Numerical grid
x0 = -1 # Initial Condition

# Explicit Euler Method
x = np.zeros(len(t))
x[0] = x0

for i in range(0, len(t) - 1):
    x[i + 1] = x[i] + h*f(t[i], x[i])

plt.figure(figsize = (12, 8))
plt.plot(t, x, 'bo--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()