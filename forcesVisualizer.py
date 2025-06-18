import matplotlib.pyplot as plt
import numpy as np
import re

times = []
fx_total = []
px_total = []
vx_total = []

with open("C:/Users/Vedant/Documents/BreakingWaves-Cylinder/postProcessing/forces1/0/force.dat", 'r') as file:
    for line in file:
        if line.startswith('#') or not line.strip():
            continue 

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
                vx_total.append(vx)
                
            except ValueError:
                print(f"Error parsing line: {line.strip()}")

# Optional: preview result
print("Sample times:", times[:5])
print("Sample total fx values:", fx_total[:5])


# make data
x = times
y = fx_total
print(fx_total[-1])

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=1.3)

ax.set(xlim=(0, 60), xticks=np.arange(0, 60, 10),
       ylim=(-1000, 2000), yticks=np.arange(-1000, 2000, 500))

plt.show()

min = []
min_indice = []
window = 20

def minIdentify(input_list):
    input_list = np.array(input_list)
    print(type(input_list))
    for i in range(window, len(input_list) - window):
        # Check if the point is smaller than the 5 points to its left and right
        left_neighbors = input_list[i - window:i]
        right_neighbors = input_list[i + 1:i + window + 1]
        
        # Check if the current point is smaller than all its neighbors
        if input_list[i] < np.min(left_neighbors) and input_list[i] < np.min(right_neighbors):
            min_indice.append(i)
            min.append(input_list[i])        
        
minIdentify(fx_total)
print(min)