xmin, xmax, ymin, ymax = -1, 1, -1, 1

x, y = np.linspace(xmin, xmax), np.linspace(ymin, ymax)

xlim(xmin, xmax)
ylim(ymin, ymax)

plt.text(, , r'$$', 
         horizontalalignment='center', verticalalignment='center', 
         bbox=dict(fc=(1, 1, 1, .7), ec='none'))

figname = ''
plt.savefig(('img/fig_%s.png' % figname), dpi=None, facecolor='w', edgecolor='w',
            orientation='portrait', papertype=None, format='png',
            transparent=False, bbox_inches=None, pad_inches=0.1,
            frameon=None)

"""
$$\begin{align*}
& \quad\quad (6..)
\end{align*}$$
"""