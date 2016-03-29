# -*- coding: utf-8 -*-
import numpy as np

import pylab as pyl

import kostka


pocethodu = 100000
# inp = [0.3, 0.5, 0.2]
zaznam = np.zeros(6)
dom = np.arange(6) + 1
moje_kostka = kostka.Kostka(6)
for i in range(pocethodu):
    # ret = kostka.vyber(inp)
    # ret muze nabyvat 1..6 (vcetne)
    ret = moje_kostka.hodit()
    # zaznam ma indexy 0..5 (vcetne)
    zaznam[ret - 1] += 1
print(zaznam)

import scipy.stats
#ret = scipy.stats.binom_test(succ, trials, prob)

ret = scipy.stats.binom_test(zaznam[4], pocethodu, 1.0 / 6)

psti = np.zeros(6)
for strana in range(6):
    psti[strana] = scipy.stats.binom_test(zaznam[strana], pocethodu, 1.0 / 6)
    
print(psti)


fig, ax1 = pyl.subplots()

ax1.bar(dom, zaznam, align='center')
ax1.axhline(pocethodu / 6.0, color="black")

ax2 =  ax1.twinx()
ax2.plot(dom, psti * 100, 'o', color='red')
ax2.set_ylim(0, 100)
# práh pro dolních 5 procent
ax2.axhline(5, color="red")

pyl.show()