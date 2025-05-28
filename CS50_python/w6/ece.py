# Your future ECE project starter code? 😉
import numpy as np
import matplotlib.pyplot as plt

# Plot a signal (just for fun)
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 5 * t)  # 5Hz sine wave
plt.plot(t, signal)
plt.title("ECE Vibes")
plt.show()  
