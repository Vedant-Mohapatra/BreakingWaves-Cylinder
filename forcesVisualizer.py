import matplotlib.pyplot as plt
import numpy as np
import re

times = []
fx_total = []
px_total = []
vx_total = []

with open("C:/Users/Vedant/Downloads/postProcessing/postProcessing/forces1/0/force.dat", 'r') as file:
    for line in file:
        if line.startswith('#') or not line.strip():
            continue  # skip comments and blank lines

        parts = line.strip().split()
        if len(parts) >= 2:
            try:
                time = float(parts[0])
                fx = float(parts[1]) #total force-x
                px = float(parts[4]) #total pressure-x
                vx = float(parts[7]) #total viscous-x
                times.append(time)
                fx_total.append(fx)
                px_total.append(px)
                
            except ValueError:
                print(f"Error parsing line: {line.strip()}")

# Optional: preview result
print("Sample times:", times[:5])
print("Sample total fx values:", fx_total[:5])



# plt.style.use('_mpl-gallery')

# make data
x = np.linspace(times[0], times[len(times)-1])
y = np.linspace(fx_total[0], fx_total[len(fx_total)-1])


# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 50), xticks=np.arange(1, 8),
       ylim=(-2000, 2000), yticks=np.arange(1, 8))

# plt.xlim([0, 50])
# plt.ylim([-2000, 2000])
plt.show()