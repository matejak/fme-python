# -*- coding: utf-8 -*-

modul = "kostka"

def def2prob(pocet):
    ret = [1 / float(pocet)] * pocet
    return ret
    

class Kostka(object):
    def __init__(self, kolik):
        self._def_obor = range(1, kolik + 1)
        self._pravdepodobnosti = def2prob(kolik)
        
    def hodit(self):
        return 6	
        

        