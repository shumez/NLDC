# pendulum

fig, axes = plt.subplots(ncols=4, nrows=2, figsize=(10, 5))

for i in range(4):
    x = xs[i]
    v = vs[i]
    
    axes[1, i].scatter(x, v, c=c[0], marker=m[0])
    #axes[1, i].plot(2*np.cos(np.linspace(-pi, pi, 100)), 2*np.sin(np.linspace(-pi, pi, 100)), c=c[0], linestyle=l[1], alpha=.5)
    axes[1, i].streamplot(x_stream, v_stream, x_dot(x_stream, v_stream), v_dot(x_stream, v_stream), 
                          color=speed(x_stream, v_stream), cmap='GnBu',
                          start_points=np.array([[x, v], [x/2, v/2], [x*3/2, v*3/2]]))
    
    axes[1, i].set_xlim(-3, 3)
    axes[1, i].set_ylim(-3, 3)
    axes[1, i].set(xlabel=r'$x$', ylabel=r'$v$')
    axes[1, i].set_xticks(np.arange(-3, 4, 1))
    axes[1, i].set_yticks(np.arange(-3, 4, 1))
    axes[1, i].grid(True)
    #axes[1, i].colorbar()
    
    axes[0, i].plot(np.sin(np.linspace(0, x+3, 100)*200/(x+3)/pi)*.1, np.linspace(-3, x, 100), c=c[0], linestyle=l[0])
    # m
    axes[0, i].scatter(0, x, c=c[0], marker=m[2])
    axes[0, i].plot(np.array([-1, -1]), np.array([x, x+v]), c=c[0], linestyle=l[0])
    axes[0, i].scatter(-1, x, c=c[0], marker='o')
    
    if v > 0:
        axes[0, i].scatter(-1, x+v, c=c[0], marker='v')
    elif v < 0:
        axes[0, i].scatter(-1, x+v, c=c[0], marker='^')
    
    axes[0, i].axhspan(-3.5, -3, facecolor=c[0], alpha=.5)
    axes[0, i].set(title=(r'$(x, v) = (%d, %d$)' % (x, v)))
    axes[0, i].set_xlim(-3, 2)
    axes[0, i].set_ylim(2.5, -3.5)
    axes[0, i].set_xticks([])
    axes[0, i].set_yticks(np.arange(-3, 3, 1))
    axes[0, i].grid(True)
        
plt.tight_layout()

# plt.savefig('img/fig_5_1_4.png', dpi=None, facecolor='w', edgecolor='w',
#             orientation='portrait', papertype=None, format='png',
#             transparent=False, bbox_inches=None, pad_inches=0.1,
#             frameon=None)

plt.show()
