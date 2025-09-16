import numpy as np
import matplotlib.pyplot as plt
#%%matplotlib inline

x = np.linspace(-40,40,100)
# print(x)

y = np.sin(x)
# print(y)

plt.plot(x,y)
plt.title("Sine Wave")