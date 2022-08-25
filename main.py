from metodosOrdenamiento import *
import random



class Cola:
    
    def __init__(self,listaSectores,ultimaLectura,metodoOrdenamiento,):
        self.cola = [] #cola de sectores vacia
        self.listaSectores = listaSectores  #Lista de los sectores a leer
        self.ultimaLectura = ultimaLectura #Ultima lectura del disco
        self.metodoOrdenamiento = metodoOrdenamiento #Metodo para ordenar la cola
        
    
    def encolar(self):
        self.metodo = self.metodoOrdenamiento
        if self.metodo == 0:
            self.cola = fcfs(self.ultimaLectura,self.listaSectores)
        elif self.metodo == 1:
            self.cola = sstf(self.ultimaLectura,self.listaSectores)
        elif self.metodo == 2:
            self.cola = scan(self.ultimaLectura,self.listaSectores)
        elif self.metodo == 3:
            self.cola = c_scan(self.ultimaLectura,self.listaSectores)
        else:
            raise Exception("El metodo de ordenamiento no existe")
    
    def desencolar(self):
        #Eliminar el priemr elemento de la cola
        try:
            return self.cola.pop(0)
        except:
            raise Exception("La cola esta vacia")
        
    
    def listarCola(self):
        if self.metodoOrdenamiento == 0:
            print("Metodo de ordenamiento: First Come First Served")
        elif self.metodoOrdenamiento == 1:
            print("Metodo de ordenamiento: Shortest Seek Time First")
        elif self.metodoOrdenamiento == 2:
            print("Metodo de ordenamiento: Scan")
        elif self.metodoOrdenamiento == 3:
            print("Metodo de ordenamiento: C-Scan")
        print("Ultima posicion del cabezal:",self.ultimaLectura)
        for indice in range(len(self.cola)):
            print(f'Sector N{indice+1} - {self.cola[indice]}')
    




if __name__ == '__main__':
    listaSectores = [10, 45, 20, 67, 12, 50, 90, 88]
    ultimaLectura = 18
    listaSectores2 = [45, 12, 89, 34, 26, 865, 25, 666, 432, 156]
    ultimaLectura2 = 69
    listaSectoresRandom = [random.randint(0,100) for i in range(10)]
    ultimaLecturaRandom = random.randint(0,100)
    
    # p_fcfs = Cola(listaSectores,18,0)
    # p_fcfs.encolar()
    # p_fcfs.listarCola()
    
    # p_sstf = Cola(listaSectoresRandom,ultimaLecturaRandom,1)
    # p_sstf.encolar()
    # p_sstf.desencolar() #Elimino la ultima lectura de la cola
    # p_sstf.listarCola()

    # p_scan = Cola(listaSectoresRandom,ultimaLecturaRandom,2)
    # p_scan.encolar()
    # p_scan.listarCola()
    
    # p_c_scan = Cola(listaSectoresRandom,ultimaLecturaRandom,3)
    # p_c_scan.encolar()
    # p_c_scan.listarCola()















        
        
        
