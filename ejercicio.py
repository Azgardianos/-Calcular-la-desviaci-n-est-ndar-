import unittest
import math

class Estadistica:
    def media(self, lista):
        "Se verifica que cada elemento de la lista sea de tipo int o float"
        if all(isinstance(x, (int, float)) for x in lista):
            return sum(lista) / len(lista)
        else:
            raise ValueError("La función solamente admite números")

    def desviacionEstandar(self, lista):
        if all(isinstance(x, (int, float)) for x in lista):
            media = self.media(lista)
            acumulado = sum((x - media) ** 2 for x in lista)
            return math.sqrt(acumulado / len(lista))
        else:
            raise ValueError("La función solamente admite números.")

# Creación de objetos
operacion = Estadistica()

# Manipulación de las funciones de los objetos
lista = [9, 3, 8, 8, 5.6, 9, 8, 9, 18, 1.442677]
print(f"Lista: {', '.join(str(x) for x in lista)}")
print(f"Media: {operacion.media(lista)}")
print(f"Desviación estándar: {operacion.desviacionEstandar(lista)}")

class TestEstadistica(unittest.TestCase):
    def setUp(self):
        self.operacion = Estadistica()

    def TestMediaEnteros(self):
        lista = [1, 2, 3, 4, 5]
        resultado = self.operacion.media(lista)
        self.assertEqual(resultado, 3)

    def TestMediaFloats(self):
        lista = [1.5, 3.5, 9.5, 5.5, 2.5]
        resultado = self.operacion.media(lista)
        self.assertAlmostEqual(resultado, 3.5)

    def TestMediaMixta(self):
        lista = [7, 9.5, 5, 6.5, 1]
        resultado = self.operacion.media(lista)
        self.assertAlmostEqual(resultado, 3.2)

    def TestDEInvalidos(self):
        lista = [1, 'a',5]
        with self.assertRaises(ValueError):
            self.operacion.media(lista)

    def TestDEEnteros(self):
        lista = [1, 2, 3, 4, 5]
        resultado = self.operacion.desviacionEstandar(lista)
        self.assertAlmostEqual(resultado, 1.4142135623730951)

    def TestDEFloats(self):
        lista = [2.5, 6.5, 3.5, 4.5, 8.5]
        resultado = self.operacion.desviacionEstandar(lista)
        self.assertAlmostEqual(resultado, 1.4142135623730951)

    def TestDEValoresInvalidos(self):
        lista = [1, 'a', 7]
        with self.assertRaises(ValueError):
            self.operacion.desviacionEstandar(lista)

if __name__ == '__main__':
   unittest.main()