# Administrador de Peticiones
## GENERAL:

Construir un Algoritmo (Python preferiblemente) que SIMULE la Administración de Peticiones
para recuperar los bloques (sectores) de un archivo de la unidad de almacenamiento secundaria.


## Supuestos:

- El archivo a Recuperar es Solo 1 (uno).
- La cantidad de sectores que lo componen es variable (1 a n).
- Los sectores están numerados, por cuestiones de la simulación de 1 a 1000) y su distribución es de ordenada de menor mayor (símil LBA=Logical Block Addressing)
- La lista de sectores que componen el archivo se entrega COMPLETA.


## Metodología:
 Recibe como parámetro una lista de sectores y el método de administración según este esquema (o similar)

    - 0 = FCFS: (FIRST COME, FIRTS SERVED) Servicio por orden de llegada similar a FIFO (First In, First Out) Primero en Entrar, Primero en Salir
    - 1 = SSTF: (SHORTEST SEEK TIME FIRST) El MAS CERCANO A LA POSICION ACTUAL (de la cabeza lectora) o algoritmo de tiempo de búsqueda más corto primero.
    - 2 = SCAN: (SCAN) también se conoce como algoritmo de elevador o de EXPLORACION.
    - 3 = C-SCAN: (CIRCULAR SCAN), variante de SCAN llamada EXPLORACION CIRCULAR


Devuelve como salida una cola con el orden de las peticiones.

  
  

## Restricción:
### **LA LISTA DE SECTORES DADA, NO DEBE SER ALTERADA EN NINGUN METODO**# CPU-RequestManager
