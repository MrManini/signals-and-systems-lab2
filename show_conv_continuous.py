import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys

x_name = sys.argv[1]
h_name = sys.argv[2]

def x(t, x_name):
    if x_name == "a":
        # Señal a
        condition1 = (t >= -1) & (t < 1)
        x1 = 1
        x = np.zeros_like(t)
        x[condition1] = x1
    elif x_name == "b":
        # Señal b
        condition1 = (t >= 1) & (t < 3)
        condition2 = (t >= 3) & (t < 4)
        x1 = 1
        x2 = 2
        x = np.zeros_like(t)
        x[condition1] = x1
        x[condition2] = x2
    elif x_name == "c":
        # Señal c
        condition1 = (t >= -2) & (t < 0)
        condition2 = (t >= 0) & (t < 2)
        x1 = -1
        x2 = 1
        x = np.zeros_like(t)
        x[condition1] = x1
        x[condition2] = x2
    elif x_name == "d":
        # Señal d
        condition1 = (t >= -1) & (t < 1)
        x1 = t[condition1]
        x = np.zeros_like(t)
        x[condition1] = x1
    elif x_name == "e":
        # Señal e
        condition1 = (t >= -4) & (t < -2)
        condition2 = (t >= -2) & (t < 0)
        condition3 = (t >= 0) & (t < 1)
        x1 = 0.5*t[condition1] + 2
        x2 = 1
        x3 = -t[condition3] + 1 #x(t) = -t+1
        x = np.zeros_like(t)
        x[condition1] = x1
        x[condition2] = x2
        x[condition3] = x3
    elif x_name == "f":
        # Señal f
        condition1 = (t >= 0) & (t < 1)
        x1 = np.exp(-t[condition1])
        x = np.zeros_like(t)
        x[condition1] = x1
    return x

def h(t, t0, h_name):
    if h_name == "a":
        # Señal a
        condition1 = (t >= -1+t0) & (t < 1+t0)
        h1 = 1
        h = np.zeros_like(t)
        h[condition1] = h1
    elif h_name == "b":
        # Señal b
        condition1 = (t >= -4+t0) & (t < -3+t0)
        condition2 = (t >= -3+t0) & (t < -1+t0)
        h1 = 2
        h2 = 1
        h = np.zeros_like(t)
        h[condition1] = h1
        h[condition2] = h2
    elif h_name == "c": 
        # Señal c
        condition1 = (t >= -2+t0) & (t < 0+t0)
        condition2 = (t >= 0+t0) & (t < 2+t0)
        h1 = 1
        h2 = -1
        h = np.zeros_like(t)
        h[condition1] = h1
        h[condition2] = h2
    elif h_name == "d":
        # Señal d
        condition1 = (t >= -1+t0) & (t < 1+t0)
        h1 = -t[condition1] + t0
        h = np.zeros_like(t)
        h[condition1] = h1
    elif h_name == "e":
        # Señal e
        condition1 = (t >= -1+t0) & (t < 0+t0)
        condition2 = (t >= 0+t0) & (t < 2+t0)
        condition3 = (t >= 2+t0) & (t < 4+t0)
        h1 = t[condition1] + 1 - t0 #h(-tau) = tau+1-t0 
        h2 = 1
        h3 = -0.5*t[condition3] + 2 + t0/2
        h = np.zeros_like(t)
        h[condition1] = h1
        h[condition2] = h2
        h[condition3] = h3
    elif h_name == "f":
        # Señal f
        condition1 = (t >= -1+t0) & (t < 0+t0)
        h1 = np.exp(-((t0-t)[condition1]))
        h = np.zeros_like(t)
        h[condition1] = h1 
    return h

def t_axis_range(x_name):
    if x_name == "a":
        t_range = (-1, 1)
    elif x_name == "b":
        t_range = (1, 4)
    elif x_name == "c":
        t_range = (-2, 2)
    elif x_name == "d":
        t_range = (-1, 1)
    elif x_name == "e":
        t_range = (-4, 1)
    elif x_name == "f":
        t_range = (0, 1)
    return t_range

x_colors = {
    "a": "red",
    "b": "#FF0060",
    "c": "#d90429",
    "d": "#ff0a54",
    "e": "#691312",
    "f": "#7b0d1e",
}

h_colors = {
    "a": "blue",
    "b": "#0096c7",
    "c": "#06d6a0",
    "d": "#00607a",
    "e": "#00187a",
    "f": "#16697a"
}

t = np.arange(-9, 10.01, 0.01)  # Adjust the time range as needed
fig, (ax1, ax2) = plt.subplots(2, 1)

# Create the empty line object for the second subplot
line2, = ax2.plot([], [], color='red', label='h(-τ t)', linestyle='dashed')

# Create empty vectors for the convolution
t_conv = np.empty(0)
xh_conv = np.empty(0)


# Define the animation function
def animate(frame):
    global t_conv, xh_conv

    t_range = t_axis_range(x_name)

    if frame <= 0:
        sign = "-"
    else:
        sign = "+"
    
    x_t = x(t, x_name)
    h_t = h(t, frame, h_name)

    conditions = [
        (h_t < x_t) & (x_t > 0) & (h_t < 0),
        (h_t < x_t) & (x_t > 0) & (h_t > 0),
        (h_t < x_t) & (x_t < 0) & (h_t < 0),
        (h_t == x_t) & (x_t > 0),
        (h_t == x_t) & (x_t < 0),
        (h_t > x_t) & (x_t > 0) & (h_t > 0),
        (h_t > x_t) & (x_t < 0) & (h_t < 0),
        (h_t > x_t) & (x_t < 0) & (h_t > 0),
    ]
    for i in range(7):
        conditions[i] = conditions[i] & ((t_range[0] <= t) & (t <= t_range[1])) & (h_t != 0)

    # Clear the first subplot and plot x and h
    ax1.clear()
    ax1.plot(t, x_t, label=f'{x_name}(τ)', color=x_colors.get(x_name))
    ax1.plot(t, h_t, label=f'{h_name}(-τ {sign} {abs(round(frame, 2))})', color=h_colors.get(h_name))
    

    # Fill between x and h in the first subplot
    ax1.fill_between(t, x_t, 0, where=conditions[0], color="xkcd:ocean blue", alpha=0.7)
    ax1.fill_between(t, h_t, 0, where=conditions[0], color="xkcd:cherry", alpha=0.7)
    ax1.fill_between(t, x_t, 0, where=conditions[7], color="xkcd:cherry", alpha=0.7)
    ax1.fill_between(t, h_t, 0, where=conditions[7], color="xkcd:ocean blue", alpha=0.7)
    ax1.fill_between(t, h_t, 0, where=conditions[1], color="xkcd:ocean blue", alpha=0.7)
    ax1.fill_between(t, h_t, 0, where=conditions[6], color="xkcd:cherry", alpha=0.7)
    ax1.fill_between(t, x_t, 0, where=conditions[2], color="xkcd:cherry", alpha=0.7)
    ax1.fill_between(t, x_t, 0, where=conditions[5], color="xkcd:ocean blue", alpha=0.7)
    ax1.fill_between(t, x_t, 0, where=conditions[3], color="xkcd:ocean blue", alpha=0.7)
    ax1.fill_between(t, x_t, 0, where=conditions[4], color="xkcd:cherry", alpha=0.7)

    # Customize plot colors
    fig.set_facecolor('#11001c')
    ax1.set_facecolor('#110e1b')
    ax2.set_facecolor('#110e1b')
    ax1.xaxis.label.set_color('#5c2446')
    ax1.yaxis.label.set_color('#5c2446')
    ax1.tick_params(axis='both', colors='#ffffff')
    ax2.xaxis.label.set_color('#ffffff')
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

    
    ax1.set_xlim(-9, 9)
    lower_limit = -0.1
    upper_limit = 2
    if x_name == "c" or x_name == "d" or h_name == "c" or h_name == "d":
        lower_limit = -1.5
    if x_name == "b" or h_name == "b":
        upper_limit = 2.5
    ax1.set_ylim(lower_limit, upper_limit)
    
    # Add elements to the convolution vectors
    t_conv = np.append(t_conv, frame)
    xh_conv = np.append(xh_conv, np.sum(x_t*h_t)*0.01)

    # Clear the second subplot and plot the new vectors
    ax2.clear()
    ax2.plot(t_conv, xh_conv, label=f"({x_name}∗{h_name})(t)", color="xkcd:toxic green")
    
    # Clear the plot if the animation has finished
    if frame > 10.9:
        t_conv = np.array([])
        xh_conv = np.array([])
        #ax2.clear()
        #ax2.plot([],[], label=f"{x_name}∗{h_name}(t)", color="#ccff33")
    legend2 = ax2.legend()
    legend2.set_frame_on(True)
    legend2.get_frame().set_edgecolor('#5c2446')  # Legend border color
    legend2.get_frame().set_facecolor('#11001c')  # Legend background color
    legend2.get_texts()[0].set_color('#ffffff')  # Legend text color
    ax2.set_xlim(-9, 9)
    fig.canvas.manager.set_window_title(f"Convolución en vivo de {x_name}(t)∗{h_name}(t)")

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.arange(-9, 11.1, 0.1), interval=0.05)
plt.show()