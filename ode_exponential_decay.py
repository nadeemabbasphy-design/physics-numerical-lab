import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def exponential_decay(t, x):
    return -x

# Time interval
t_span = (0, 5)
t_eval = np.linspace(0, 5, 300)

# Initial condition
x0 = [1.0]

# Solve ODE
solution = solve_ivp(exponential_decay, t_span, x0, t_eval=t_eval)

# Plot the result
plt.plot(solution.t, solution.y[0])
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.title("Exponential Decay: dx/dt = -x")
plt.grid(True)
plt.show()
