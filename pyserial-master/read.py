import serial,time #conexion
import matplotlib as plt #graficar en python
from drawnow import *  #brinda caracteristas para redibujar el grafico
import atexit #para definir funciones con de limpieza registro y no registradas




valuesH = [] #arreglo
valuesT=[]
plt.ion() #modo iterativo, nuevas versiones no necesitan
cnt=0 #inicializamos una variable del tipo entero

serialArduino = serial.Serial('COM7',115200 ) 

def plotValues():
    plt.title('Serial value from Arduino')
    plt.grid(True)
    plt.ylabel('Valores del sensor ')
    plt.plot(valuesH, 'rx-', label='values')

    plt.legend(loc='upper right')


def doAtExit():
    serialArduino.close()
    print("Close serial")
    print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

atexit.register(doAtExit)

print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))


#pre-load dummy data
for i in range(0,26):
    valuesH.append(0)
while True:
    while (serialArduino.inWaiting()==0):
        pass
    valueRead = serialArduino.readline()
    print(valueRead)

    try:
        print (valueRead)
        valuesH.append(valueRead)
        valuesH.pop(0)
        drawnow(plotValues)
    except ValueError:
        print ("Invalid! cannot cast")
       # valuesH.clear()

