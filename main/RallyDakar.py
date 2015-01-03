'''
Created on 3/1/2015

@author: myhay
'''

class Piloto(object):
    '''
    Examn 2014 UJI Informatica
    '''
    def __init__(self, nombre,categoria):
        self.nombre = nombre
        self.categoria = categoria
    
    def getCategoria(self):
        return self.categoria
    
    def getPiloto(self):
        return self.nombre
    
    def getRally(self):
        return (self.nombre, self.categoria)