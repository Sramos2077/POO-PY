#la clase es un contenedor donde podemos agregar funciones y atributos por ejemplo: 
# clase carro(marca, color):
#    carro.color
#    carro.marca
#funciones:
#carro.drive()
#carro.stop()

#el objeto es un una instancia de la clase donde se asignan el nombre, los atributos y poder ejecutar las funciones
#   carro mi_carro = new carro('ford', 'rojo')
#   mi_carro.drive()

class Car: 
    #el metodo o funcion init sirve para inicializar el constructor de la clase y self representa la misma clase
    def __init__(self, brand, model, age): 
        self.brand = brand
        self.model = model
        self.age = age
#<----instancias de clase o mejor dicho objetos ------>
first_car = Car('Ford', 'Fiesta', 2024)
second_car = Car('Chevrolet', 'Camaro', 2012)
third_car = Car('BMW', 'M3 GTR', 2005)
fourth_car = Car('Toyota', 'Supra 2021', 2021)

print(f'el objeto es: {first_car.brand}, {first_car.model}, {first_car.age}')
print(f'el objeto es: {second_car.brand}, {second_car.model}, {second_car.age}')
print(f'el objeto es: {third_car.brand}, {third_car.model}, {third_car.age}')
print(f'el objeto es: {fourth_car.brand}, {fourth_car.model}, {fourth_car.age}')

   