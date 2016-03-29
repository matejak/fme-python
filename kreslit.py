import numpy as np
import pylab as pyl

import kostka



inp = [0.3, 0.5, 0.2]
zaznam = np.zeros(len(inp))
dom = np.arange(len(inp))
for i in range(100):
    ret = kostka.vyber(inp)
    zaznam[ret] += 1
print(zaznam)

pyl.figure()
pyl.bar(dom, zaznam)
pyl.grid()
pyl.show()