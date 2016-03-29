# -*- coding: utf-8 -*-
import random

modul = "kostka"

def def2prob(pocet):
    ret = [1 / float(pocet)] * pocet
    return ret
    
  
def vyber(inp):
    kumulativni = []
    soucasny = 0
    for prvek in inp:
        soucasny += prvek
        kumulativni.append(soucasny)
    kumulativni.reverse()
    # soucet_inp = sum(inp)
    soucet_inp = kumulativni[0]
    if soucet_inp <= 0:
        raise ValueError(u"Součet pravděpodobností musí být větší jak 0")
    ret = len(inp)
    rand = random.random() * soucet_inp
    for prvek in kumulativni:
        if prvek > rand:
            ret -= 1
        else:
            return ret
    return 0

      
def factory(inp):
    def vyrobek():
        ret = vyber(inp)
        return ret
    return vyrobek
    
          
class Kostka(object):
    def __init__(self, kolik):
        self._def_obor = range(1, kolik + 1)
        self._pravdepodobnosti = def2prob(kolik)
        
        self._generator = factory(self._pravdepodobnosti)
        
    def hodit(self):
        idx = self._generator()
        ret = self._def_obor[idx]
        # zfalsovani kostky
        if ret == 2:
            ret = 6
        return ret	
        

        