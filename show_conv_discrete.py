import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors
import sys


x_name = sys.argv[1]
h_name = sys.argv[2]

def x(n, x_name):
    if x_name == "a":
        # Señal a
        condition1 = (n >= -5) & (n <= 5)
        x1 = n[condition1]
        x = np.zeros_like(n)
        x[condition1] = x1
    elif x_name == "b":
        # Señal b
        condition1 = (n >= -1) & (n <= 7)
        x1 = 1
        x = np.zeros_like(n)
        x[condition1] = x1
    elif x_name == "c":
        # Señal c
        condition1 = (n >= -3) & (n <= 3)
        x1 = 1
        x = np.zeros_like(n)
        x[condition1] = x1
    elif x_name == "d":
        # Señal d
        condition1 = (n >= 0) & (n <= 6)
        x1 = np.power(7/8, n[condition1])
        x = np.zeros(n.shape, dtype=float)
        x[condition1] = x1
    return x

def h(n, n0, h_name):
    if h_name == "a":
        # Señal a
        condition1 = (n >= -5+n0) & (n <= 5+n0)
        h1 = -n[condition1] + n0
        h = np.zeros_like(n)
        h[condition1] = h1
    elif h_name == "b":
        # Señal b
        condition1 = (n >= -7+n0) & (n <= 1+n0)
        h1 = 1
        h = np.zeros_like(n)
        h[condition1] = h1
    elif h_name == "c": 
        # Señal c
        condition1 = (n >= -3+n0) & (n <= 3+n0)
        h1 = 1
        h = np.zeros_like(n)
        h[condition1] = h1
    elif h_name == "d":
        # Señal d
        condition1 = (n >= -6+n0) & (n <= 0+n0)
        h1 = np.power(7/8, -n[condition1] + n0)
        h = np.zeros(n.shape, dtype=float)
        h[condition1] = h1
    return h

def n_axis_range(x_name):
    if x_name == "a":
        n_range = (-5, 5)
    elif x_name == "b":
        n_range = (-1, 7)
    elif x_name == "c":
        n_range = (-3, 3)
    elif x_name == "d":
        n_range = (0, 6)
    return n_range

n = np.arange(-20, 31, 1)  # Adjust the time range as needed
fig, (ax1, ax2) = plt.subplots(2, 1)

# Create the empty line object for the second subplot
line2, = ax2.plot([], [], color='red', label='h(-τ n)', linestyle='dashed')

# Create empty vectors for the convolution
n_conv = np.empty(0)
xh_conv = np.empty(0)

x_colors = {
    "a": "xkcd:red",
    "b": "xkcd:deep red",
    "c": "xkcd:blood red",
    "d": "xkcd:crimson",
}

h_colors = {
    "a": "xkcd:blue",
    "b": "xkcd:water blue",
    "c": "xkcd:nice blue",
    "d": "xkcd:denim",
}



# Define the animation function
def animate(frame):
    global n_conv, xh_conv

    n_range = n_axis_range(x_name)

    if frame <= 0:
        sign = "-"
    else:
        sign = "+"
    
    x_n = x(n, x_name)
    h_n = h(n, frame, h_name)

    conditions = [
        (h_n < x_n) & (x_n > 0) & (h_n < 0),
        (h_n < x_n) & (x_n > 0) & (h_n > 0),
        (h_n < x_n) & (x_n < 0) & (h_n < 0),
        (h_n == x_n),
        (h_n > x_n) & (x_n > 0) & (h_n > 0),
        (h_n > x_n) & (x_n < 0) & (h_n < 0),
        (h_n > x_n) & (x_n < 0) & (h_n > 0),
    ]
    for i in range(7):
        conditions[i] = conditions[i] & ((n_range[0] <= n) & (n <= n_range[1])) & (h_n != 0)

    x_c = x_colors.get(x_name)
    h_c = h_colors.get(h_name)

    # Clear the first subplot and plot x and h
    ax1.clear()
    ax1.stem(n, x_n, "b", label=f'{x_name}[k]', linefmt=x_c, markerfmt=x_c, basefmt=x_c)
    ax1.stem(n, h_n, "r", label=f'{h_name}[-k {sign} {abs(round(frame, 2))}]', linefmt=h_c, markerfmt=h_c, basefmt=h_c)
    
    # Customize plot colors
    fig.set_facecolor('#11001c')
    ax1.set_facecolor('#110e1b')
    ax2.set_facecolor('#110e1b')
    ax1.xaxis.label.set_color('#5c2446')
    ax1.yaxis.label.set_color('#5c2446')
    ax1.tick_params(axis='both', colors='#ffffff')
    ax2.xaxis.label.set_color('xkcd:deep purple')
    ax2.yaxis.label.set_color('#ffffff')
    ax2.tick_params(axis='both', colors='#ffffff')
    ax1.spines['bottom'].set_color('#5c2446')
    ax1.spines['top'].set_color('#5c2446')
    ax1.spines['left'].set_color('#5c2446')
    ax1.spines['right'].set_color('#5c2446')
    ax2.spines['bottom'].set_color('#5c2446')
    ax2.spines['top'].set_color('#5c2446')
    ax2.spines['left'].set_color('#5c2446')
    ax2.spines['right'].set_color('#5c2446')

    legend1 = ax1.legend()
    legend1.set_frame_on(True)
    legend1.get_frame().set_edgecolor('#5c2446')  # Legend border color
    legend1.get_frame().set_facecolor('#11001c')  # Legend background color
    legend1.get_texts()[0].set_color('#ffffff')  # Legend text color
    legend1.get_texts()[1].set_color('#ffffff')
    ax1.set_xlim(-15, 16)
    lower_limit = -6
    upper_limit = 6
    if x_name == "c" or x_name == "d" or h_name == "c" or h_name == "d":
        lower_limit = 0
        upper_limit = 1.1
    ax1.set_ylim(lower_limit, upper_limit)
    
    # Add elements to the convolution vectors
    n_conv = np.append(n_conv, frame)
    xh_conv = np.append(xh_conv, np.sum(x_n*h_n))

    # Clear the second subplot and plot the new vectors
    ax2.clear()
    ax2.stem(n_conv, xh_conv, "g", label=f"({x_name}∗{h_name})[n]", linefmt='xkcd:toxic green', markerfmt='xkcd:toxic green', basefmt='xkcd:toxic green')
    legend2 = ax2.legend()
    legend2.set_frame_on(True)
    legend2.get_frame().set_edgecolor('#5c2446')  # Legend border color
    legend2.get_frame().set_facecolor('#11001c')  # Legend background color
    legend2.get_texts()[0].set_color('#ffffff')  # Legend text color
    ax2.set_xlim(-15, 16)


    # Clear the plot if the animation has finished
    if frame == 30:
        n_conv = np.array([])
        xh_conv = np.array([])
    #ax2.set_ylim(-0.1, 2.5)

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.arange(-20, 31, 1), interval=300)

plt.show()