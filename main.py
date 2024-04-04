from lib import *
import threading
import time 


"""def timeMaker():
    print("haciendo tiempo...")
    time.sleep(2) #segundos
    print("tiempo hecho")    
# timeMaker() pruebita 


t0 = time.time()
listaHilos = []
for i in range(4):
    t = threading.Thread(target = timeMaker)
    listaHilos.append(t)
    t.start()

for t in listaHilos:
    t.join()
    
tf = time.time() - t0
print(f' Tiempototal de ejecución: {tf}') 

print("Hilo principal o 1 hilo")
print()

def contador(inicio, fin):
    arrayNum = []
    for i in range(inicio, fin+1, 1):
        arrayNum.append(i)
        time.sleep(0.01)
    return arrayNum

t0 = time.time()
listaNumeros = contador(1,100)
tf = time.time() - t0
print(f'Tiempo de ejecución: {tf}')
print(listaNumeros)
print("-----------------------------------------")

print("Usando 2 hilos")
print()

globalArrayNum = []

def contadorDos(inicio, fin):
    for i in range(inicio, fin+1, 1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0
    


t0 = time.time()
listaHilos = []

t = threading.Thread(target = contadorDos, args = (1,50))
listaHilos.append(t)
t.start()

t = threading.Thread(target = contadorDos, args = (51,100))
listaHilos.append(t)
t.start()

for t in listaHilos:
    t.join() #unir hilos al principal
tf = time.time() -t0

print(f'Tiempo de ejecución: {tf}')
print(globalArrayNum)"""


print("-----------------------------------------")

#globalArrayNum.sort()
print("-----------------------------------------")

print("Usando 4 hilos")
print()

globalArrayNum = []

def contadorDos(inicio, fin):
    for i in range(inicio, fin+1, 1):
        globalArrayNum.append(i)
        time.sleep(0.01)
    return 0
    


t0 = time.time()
listaHilos = []


t = threading.Thread(target = contadorDos, args = (1,25))
listaHilos.append(t)
t.start()

t = threading.Thread(target = contadorDos, args = (26,50))
listaHilos.append(t)
t.start()

t = threading.Thread(target = contadorDos, args = (51,75))
listaHilos.append(t)
t.start()

t = threading.Thread(target = contadorDos, args = (76,100))
listaHilos.append(t)
t.start()

for t in listaHilos:
    t.join() #unir hilos al principal
tf = time.time() -t0

print(f'Tiempo de ejecución: {tf}')
print(globalArrayNum)


print("-----------------------------------------")