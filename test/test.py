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

tiempos = [[125, 115, 122, 118, 121],
           [180, 175, 171, 172, None],
           [150, 151, 149, 150, None],
           [119, 117, 118, None, None],
           [185, 182, 186, None, None],
           [116, 115, 114, None, None]]

def ganador_etapa(matrizTiempos, listaPilotos, categoria, e):
        min = -1
        indicePiloto = -1
        for i in range(len(listaPilotos)):
            if categoria == listaPilotos[i].getCategoria():
                if min == -1:
                    if matrizTiempos[e][i] != None:
                        min = matrizTiempos[e][i]
                        indicePiloto = i
                else:
                    if matrizTiempos[e][i] != None:
                        if min >= matrizTiempos[e][i]:
                            min = matrizTiempos[e][i]
                            indicePiloto = i
        if min == -1:
            return "Fracaso de carrera."
        else:
            return listaPilotos[indicePiloto].getPiloto()

def mas_etapas_consecutivas(matrizTiempos, listaPilotos,categoria):
    lista = []
    for e in range(len(matrizTiempos[0])):
        lista.append(ganador_etapa(matrizTiempos, listaPilotos, categoria, e))
    #print lista
    contador = 0
    max_cont = 0
    max_piloto = "Error"
    for piloto in range(len(lista)):
        if piloto < len(lista)-1:
            if lista[piloto] == lista[piloto+1]:
                contador+=1
            else:
                if contador > max_cont:
                    max_cont = contador
                    max_piloto = lista[piloto]
                contador = 0
    return max_piloto

def lider_provisional(matrizTiempos, listaPilotos, categoria, e):
    lista_tiempos_pilotos = []
    for j in range(len(listaPilotos)):
        suma = 0
        for i in range(e+1): # el +1 viene porque dado el ejemplo la etapa es literal
            if categoria == listaPilotos[j].getCategoria():
                if matrizTiempos[i][j] == None:
                    suma = -2
                else:
                    suma += matrizTiempos[i][j]      
            else:
                suma = -1
        lista_tiempos_pilotos.append(suma)
    #print lista_tiempos_pilotos
    
    min = -1
    index_piloto = -1
    for i in range(len(lista_tiempos_pilotos)):
        if lista_tiempos_pilotos[i] > 0:
            if min == -1:
                min = lista_tiempos_pilotos[i]
                index_piloto = i
            elif min > lista_tiempos_pilotos[i]:
                min = lista_tiempos_pilotos[i]
                index_piloto = i
    if min == -1:
        return "error"
    else:
        return listaPilotos[index_piloto].getPiloto()
            
def generarListaPilotos():
    lista = []
    lista.append(Piloto("Peterhansel","coches"))
    lista.append(Piloto("Coma","motos"))
    lista.append(Piloto("Roma","coches"))
    lista.append(Piloto("Sainz","coches"))
    lista.append(Piloto("Ortiz","motos"))
    return lista

if __name__ == '__main__':
    lista_pilotos = generarListaPilotos()   
    print ganador_etapa(tiempos, lista_pilotos, "coches", 3)
    print mas_etapas_consecutivas(tiempos, lista_pilotos, "coches")
    print lider_provisional(tiempos, lista_pilotos, "coches", 3)
    