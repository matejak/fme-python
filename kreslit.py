# -*- coding: utf-8 -*-

import argparse as ap
import numpy as np

import pylab as pyl

import kostka

parser = ap.ArgumentParser()
parser.add_argument("--number", "-n", type=int, default=100, help=u"Počet hodů kostkou")
parser.add_argument("--pocetstran", type=int, default=6, help=u"Počet stran kostky")
parser.add_argument("--vahy", "-w", help=u"Váhy jednotlivých stran odd. čárkou (toto přebíjí --pocetrstran)")
parser.add_argument("output", nargs="?", default="fig.pdf", help=u"Výstupní soubor")

args = parser.parse_args()

pocethodu = args.number
nazev = args.output
pocetstran = args.pocetstran
vahy = args.vahy

if vahy is not None:
    vahy_str = vahy.split(",")
    vahy = [str(vaha_str) for vaha_str in vahy_str]
    pocetstran = len(vahy)

# inp = [0.3, 0.5, 0.2]
zaznam = np.zeros(pocetstran)
dom = np.arange(pocetstran) + 1

moje_kostka = kostka.Kostka(pocetstran, vahy)
for i in range(pocethodu):
    # ret = kostka.vyber(inp)
    # ret muze nabyvat 1..pocetstran (vcetne)
    ret = moje_kostka.hodit()
    # zaznam ma indexy 0..(pocetstran - 1) (vcetne)
    zaznam[ret - 1] += 1

import scipy.stats
#ret = scipy.stats.binom_test(succ, trials, prob)

psti = np.zeros(pocetstran)

# Spodní verze cyklu je vice Pythonovská
# for strana in range(pocetstran):
#     psti[strana] = scipy.stats.binom_test(zaznam[strana], pocethodu, 1.0 / pocetstran)

for index, kolikrat_padlo in enumerate(zaznam):
    psti[index] = scipy.stats.binom_test(kolikrat_padlo, pocethodu, 1.0 / pocetstran)    

fig, ax1 = pyl.subplots()

ax1.bar(dom, zaznam, align='center')
ax1.axhline(pocethodu / float(pocetstran), color="black")

ax2 =  ax1.twinx()
ax2.plot(dom, psti * 100, 'o', color='red')
ax2.set_ylim(0, 100)
# práh pro dolních 5 procent
ax2.axhline(5, color="red")

fig.savefig(nazev)
fig.clear()