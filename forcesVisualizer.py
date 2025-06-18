import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

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
print(len(times))
print(len(fx_total))

def graph(x_axis, y_axis):
# make data
    x = x_axis
    y = y_axis

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
    graph(times, input_list)
    # print("Length of timlen(times))
    print("Length of original list:", len(input_list))
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
    print(min)
    print(min_indice)
    cleaner(input_list)

threshold = 7

def cleaner(input_list):
    last_index = min_indice[-1]
    for i in range(len(min_indice)):
        if abs(input_list[min_indice[i]] - input_list[last_index]) > threshold:
            start_garbage = min_indice[i]
            clean_index = i
    # min_indice = min_indice[clean_index:-1]

    #count how many periods


    # split = np.split(input_list, [start_garbage, last_index])
    # input_list = split[1]
    # fx_total = split[1]
    clean = input_list[start_garbage:last_index+1]
    # return clean

    times2 = times[start_garbage:last_index+1]
    # del times[0:start_garbage+1]
    # del times[last_index:len(input_list)]
    
    print(len(times2))
    print(len(clean))
    
    graph(times2, clean)
    # avgProfile(input_list)

# def avgProfile(input_list):
#     timeX1 = times[min_indice[0]:min_indice[1]]
#     dataX1 = input_list[min_indice[0]:min_indice[1]]

#     timeX2 = times[min_indice[1]:min_indice[2]]
#     dataX2 = input_list[min_indice[1]:min_indice[2]]

#     common_time = np.sort(np.unique(np.concatenate([timeX1, timeX2])))

#     interp_func1 = interp1d(timeX1, dataX1, kind='linear', fill_value="extrapolate")
#     interp_func2 = interp1d(timeX2, dataX2, kind='linear', fill_value="extrapolate")

#     data1_common = interp_func1(common_time)
#     data2_common = interp_func2(common_time)

#     averaged_data = (data1_common + data2_common) / 2

#     graph(common_time, averaged_data)


minIdentify(fx_total)
minIdentify(px_total)
minIdentify(vx_total)

