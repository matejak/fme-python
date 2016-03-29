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
    ret = len(inp)
    rand = random.random()
    for prvek in kumulativni:
        if prvek > rand:
            ret -= 1
        else:
            return ret
    return 0
      

class Kostka(object):
    def __init__(self, kolik):
        self._def_obor = range(1, kolik + 1)
        self._pravdepodobnosti = def2prob(kolik)
        
    def hodit(self):
        return 6	
        

        