def fcfs(ultimaLectura,lisSectores): #recibe una lista de Sectores
    return lisSectores

# Shotest Seek Time First
def sstf(ultimaLectura,lisSectores):  #recibe una lista de Sectores y la ultima lectura del disco
    cabezal = ultimaLectura
    busquedaSecuencia = []
    buscarSector = 0
    busquedaSecuencia.append(cabezal)
    for i in range(len(lisSectores)):
        sectorMasCercano = lisSectores[min(range(len(lisSectores)), key=lambda i: abs(lisSectores[i] - cabezal))] #busca el sector mas cercano al cabezal
        if cabezal >=sectorMasCercano or cabezal<= sectorMasCercano: #si el cabezal esta en el rango del sector mas cercano
            difference = cabezal - sectorMasCercano #calcula la diferencia entre el cabezal y el sector mas cercano
            buscarSector += difference #suma la diferencia al contador de operaciones
            cabezal = sectorMasCercano #cambia el cabezal al sector mas cercano
        lisSectores.remove(sectorMasCercano) #elimina el sector mas cercano de la lista de sectores
        busquedaSecuencia.append(sectorMasCercano) #agrega el sector mas cercano a la lista de sectores buscados
    return busquedaSecuencia

# Scan, elevador o por exploracion
def scan(ultimaLectura,lisSectores):  #recibe una lista de sectores y la ultima lectura del disco
    cabezal = ultimaLectura
    busquedaSecuencia = []
    buscarSectores = 0
    for i in lisSectores: #Agrego los sectores de mayor numeracion cercanos al cabezal
        if cabezal <= i:   
            cabezal = i
            busquedaSecuencia.append(i)
    for i in range(len(lisSectores)):
            sectorMasCercano = lisSectores[min(range(len(lisSectores)), key=lambda i: abs(lisSectores[i] - cabezal))] #busca el sector mas cercano al cabezal
            if cabezal >=sectorMasCercano or cabezal<= sectorMasCercano: #si el cabezal esta en el rango del sector mas cercano
                difference = cabezal - sectorMasCercano #calcula la diferencia entre el cabezal y el sector mas cercano
                buscarSectores += difference #suma la diferencia al contador de operaciones
                cabezal = sectorMasCercano #cambia el cabezal al sector mas cercano
            lisSectores.remove(sectorMasCercano) #elimina el sector mas cercano de la lista de sectores
            if sectorMasCercano not in busquedaSecuencia: #si el sector mas cercano no esta en la lista de sectores buscados
                busquedaSecuencia.append(sectorMasCercano) #agrega el sector mas cercano a la lista de sectores buscados
    return busquedaSecuencia

#C-Scan  o por exploración  circular

def c_scan(ultimaLectura,lisSectores):  #recibe una lista de sectores y la ultima lectura del disco
    cabezal = ultimaLectura
    sectores = sorted(lisSectores) #ordena los sectores de menor a mayor
    busquedaSecuencia = []
    for i in sectores: #Agrego los sector de mayor numeracion cercanos al cabezal
        if cabezal <= i:   
            cabezal = i
            busquedaSecuencia.append(i)
    cabezal = 0 #el cabezal vuelve a cero y se vuelve a buscar desde el principio
    for i in sectores: #agrego el resto de sectores a la lista
        if cabezal <= i and i not in busquedaSecuencia:   
            cabezal = i
            busquedaSecuencia.append(i)
    return busquedaSecuencia
