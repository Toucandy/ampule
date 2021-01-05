import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt
import sys
from ampule import Ampule, search_mask

ampule = Ampule(*sys.argv)

data, _ = ampule.load(f'dat/poly.dat')

plt.plot(data.x, data.f, label = r'$f(x)$')
plt.plot(data.x, data.g, label = r'$g(x)$')
plt.plot(data.x, data.h, label = r'$h(x)$')
plt.plot(data.x, data.f + data.g/2 + data.h/6, label = r'$(f + g/2 + h/6)(x)$')

plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.grid()
plt.legend()
plt.title('Linear scale')

ampule.savefig(plt, 'linear')
plt.clf()

###############################################################################

plt.plot(data.x, data.f, label = r'$f(x)$')
plt.plot(data.x, data.g, label = r'$g(x)$')
plt.plot(data.x, data.h, label = r'$h(x)$')

plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.loglog()
plt.grid()
plt.legend()
plt.title('Logarithmic scale')

ampule.savefig(plt, 'loglog')
plt.clf()

###############################################################################

ampule.flush_deps()
