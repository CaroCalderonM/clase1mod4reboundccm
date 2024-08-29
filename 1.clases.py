'''
Se requiere: 
Diseñar una clase que represente a un animal. Un animal tiene las siguientes características comunes:
nombre, raza, edad y peso. 
Generar las acciones para cuando cada Animal puede comer, caminar, dormir.
Se debe representar a dos objetos que pertenecen a la clase animal, cuyos objetos son un gato y un perro con ciertas características particulares:

'''

# Defino la clase Animal con nombre, raza, edad, peso.
class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

# A continuación, defino las funciones comer, caminar, dormir.
    def comer(self):
        return f"Hola, soy {self.nombre} y me gusta la comida."
        print(f"Nosotros los de raza {self.raza} comemos 3 veces al día")

    def caminar(self):
        return f"Camino a diario y ya estoy pesando {self.peso} kilogramos."

    def dormir(self):
        return f"Aunque tengo {self.edad} años, me gusta dormir mucho."


# Creo el objeto perro
perro_brando = Animal("Brando", "San Bernardo", 3, 30)
print(f"Perro:\n Nombre: {perro_brando.nombre}\n Raza: {perro_brando.raza}\n Edad: {perro_brando.edad} años\n Peso: {perro_brando.peso} kg")
print(perro_brando.comer()) # Ejemplo de método
print(perro_brando.caminar()) # Ejemplo de método

# Creo el objeto gato
gato_roll = Animal("Roll", "Persa", 4, 3)
print(f"\nGato:\nNombre: {gato_roll.nombre}\nRaza: {gato_roll.raza}\nEdad: {gato_roll.edad} años\nPeso: {gato_roll.peso} kg")
print(gato_roll.dormir())  # Ejemplo de método

print("Fin")




