# interact pendulum

%matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np

omega = 1
pi = np.pi

def x_dot(x, v):
    x_ = v
    return x_

def v_dot(x, v):
    v_ = - omega**2 * x
    return v_

def speed(x, v):
    s = np.sqrt(x_dot(x, v)**2 + v_dot(x, v)**2)
    return s

xs = np.array([-2, 0, 2, 0])
vs = np.array([0, 2, 0, -2])

x_stream, v_stream = np.linspace(-3, 4, 10), np.linspace(-3, 4, 10)
x_stream, v_stream = np.meshgrid(x_stream, v_stream)


def plot_spring(t, k):
    
    x = np.cos(t*(-pi)) * (k)
    v = np.sin(t*(-pi)) * (k)
    
    fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
    
    axes[1].scatter(x, v, c=c[0], marker=m[0])
    #axes[1].plot(2*np.cos(np.linspace(-pi, pi, 100)), 2*np.sin(np.linspace(-pi, pi, 100)), c=c[0], linestyle=l[1], alpha=.5)

    axes[1].streamplot(x_stream, v_stream, x_dot(x_stream, v_stream), v_dot(x_stream, v_stream), 
                       color=speed(x_stream, v_stream), cmap='GnBu', 
                       density=.5)
    
    axes[1].set_xlim(-3, 3)
    axes[1].set_ylim(-3, 3)
    axes[1].set(xlabel=r'$x$', ylabel=r'$v$')
    axes[1].set_xticks(np.arange(-3, 4, 1))
    axes[1].set_yticks(np.arange(-3, 4, 1))
    axes[1].grid(True)
    
    axes[0].plot(np.sin(np.linspace(0, x+3, 100)*200/(x+3)/pi)*.1-1, np.linspace(-3, x, 100), c=c[0], linestyle=l[0])
    # m
    axes[0].scatter(-1, x, c=c[0], marker=m[2])
    axes[0].text(-1.1, x, (r'$x = %.2f$' % x), horizontalalignment='right', verticalalignment='center')
    axes[0].plot(np.array([0, 0]), np.array([x, x+v]), c=c[0], linestyle=l[0])
    axes[0].text(.1, x+v/2, (r'$v = %.2f$' % v), horizontalalignment='left', verticalalignment='center')
    axes[0].scatter(0, x, c=c[0], marker='o')
    
    if v > 0:
        axes[0].scatter(0, x+v, c=c[0], marker='v')
    elif v < 0:
        axes[0].scatter(0, x+v, c=c[0], marker='^')
    
    axes[0].text(-1.1, x/2 - 1.5, (r'$k = %.2f$' % k), horizontalalignment='right', verticalalignment='center')
    
    axes[0].text(1.5, 3, (r'$t = %.2f$' % t), horizontalalignment='left', verticalalignment='bottom')
    axes[0].axhspan(-3.5, -3, facecolor=c[0], alpha=.5)
    axes[0].set(title=(r'$(x, v) = (%.2f, %.2f$)' % (x, v)))
    axes[0].set_xlim(-3, 2)
    axes[0].set_ylim(3.5, -3.5)
    axes[0].set_xticks([])
    axes[0].set_yticks(np.arange(-3, 4, 1))
    axes[0].grid(True)
    
    plt.tight_layout()
    plt.show()

# plot_spring(2, 0)

interactive_plot = interactive(plot_spring, t=(0, 4, 0.1), k=(0, 2, 0.1))
output = interactive_plot.children[-1]
output.layout.height = '350px'
interactive_plot
