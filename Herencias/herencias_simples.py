import time #importacion del modulo time

#clase laptop (clase padre)
class laptop:
    def __init__(self, marca, modelo, procesador, ram, almacenamiento): #constructor
        #atributos
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
    #metodos de clase
    def encender(self):
        print(f"esta encendiendo tu laptop {self.marca} {self.modelo}")
    
    def apagar(self):
        print(f"esta apagandose tu laptop {self.marca} {self.modelo}")
        
class gamer(laptop): #clase gamer (clase hijo)
    #constructor
    def __init__(self, marca, modelo, procesador, ram, almacenamiento, tarjeta_grafica):
        #la funcion super() invoca los atributos de la clase padre sin tener que escribirlos manualmente
        super().__init__(marca, modelo, procesador, ram, almacenamiento) 
        #atributo
        self.tarjeta_grafica = tarjeta_grafica
    #metodo de clase
    def jugar(self):
        print(f'estas jugando con tu laptop {self.marca} {self.modelo}')
#creacion de objeto o instancia de clase

class workstation(laptop):
    def __init__(self, marca, modelo, procesador, ram, almacenamiento, tarjeta_grafica1):
        super().__init__(marca, modelo, procesador, ram, almacenamiento)
        self.tarjeta_grafica1 = tarjeta_grafica1
    
    def diseñar(self):
        print(f"estas diseñando en tu laptop {self. marca} {self.modelo}")

"""
laptop1 = gamer('Lenovo', 'Legion', 'Intel i7', 16, 320, 'NVIDIA GEFORCE 4060')
laptop1.encender()
time.sleep(5)
laptop1.jugar()
time.sleep(5)
laptop1.apagar()
"""
laptop2 = workstation('Dell', 'Inspiron', 'intel i9', 4, 320, 'NVIDIA GEFORCE 4060')
laptop2.encender()
time.sleep(3)
laptop2.diseñar()
time.sleep(3)
laptop2.apagar()