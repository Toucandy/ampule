import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt
import sys
from ampule import Ampule, search_mask

ampule = Ampule(*sys.argv)

plt.ylim(-10, 10)

for path, k in search_mask('dat/hermite/H_', '.dat'):
    data, meta = ampule.load(path)
    formula = meta.f.replace('**', '^').replace('*', '')
    label = rf'$H_{k} = {formula}$'
    plt.plot(data.x, data.H, label = label)

plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.grid()
plt.legend()
plt.title('Hermite Polynomials')

ampule.savefig(plt, 'hermite')
plt.clf()

###############################################################################

ampule.flush_deps()
