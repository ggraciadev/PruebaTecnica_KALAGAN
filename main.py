#-------------- EJERCICIO 1 --------------

import math

class Figura:
    def __init__(self):
        pass
    
    def area(self):
        pass

class Rectangulo(Figura):
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def area(self):
    return self.base * self.altura

class Circulo:
  def __init__(self, radio):
    self.radio = radio

  def area(self):
    return self.radio * self.radio * math.pi


def mostrar_area(figura : Figura):
    print("El area de la figura es: " + str(figura.area()))
    

circ = Circulo(4)
rect = Rectangulo(5,2)

print("-------------- EJERCICIO 1 --------------")
mostrar_area(circ)
mostrar_area(rect)

#-------------- EJERCICIO 2 --------------

def remove_duplicates(lista):
  return list(dict.fromkeys(lista))

def sumar_lista(list_a, list_b):
    counter = 0
    temp_list_a = remove_duplicates(list_a)
    for value in temp_list_a:
       if isinstance(value, int) and value in list_b:
          counter += value

    return "La suma de los elementos comunes es: " + str(counter)
        
print("-------------- EJERCICIO 2 --------------")
lista_a = [0,3,1,1,1,1,1,4,5]
lista_b = [5,2,1,6,5,1,1,1,1,2,5]

lista_c = ['a','e','i','o','u']
lista_d = ['a','b','c','d','e']

print(sumar_lista(lista_a, lista_b))