import math
import unittest

class Estadistica:
    def media(self, lista):
        "Se verifica que cada elemento de la lista sea de tipo int o float"
        if (all((isinstance(x, int) or isinstance(x, float)) for x in lista) == True):
            acumulado = 0
            for x in lista:
                acumulado = acumulado + x
            return acumulado / len(lista)
        else:
            print("La función solamente admite números")
            return 0

    def desviacionEstandar(self, lista):
        if (all((isinstance(x, int) or isinstance(x, float)) for x in lista) == True):
            acumulado = 0
            media = self.media(lista)
            for x in lista:
                acumulado = acumulado + ((x - media) ** 2)
            return math.sqrt(acumulado / len(lista))
        else:
            print("La función solamente admite números.")
            return 0

class TestEstadistica(unittest.TestCase):
    def setUp(self):
        self.operacion = Estadistica()
    
    def test_media(self):
        lista = [9, 3, 8, 8, 5.6, 9, 8, 9, 18, 1.442677]
        resultado = self.operacion.media(lista)
        esperado = sum(lista) / len(lista)
        self.assertAlmostEqual(resultado, esperado, places=5)

    def test_media_con_valores_invalidos(self):
        lista = [9, 3, 'a', 8, 5.6]
        resultado = self.operacion.media(lista)
        self.assertEqual(resultado, 0)
    
    def test_desviacion_estandar(self):
        lista = [9, 3, 8, 8, 5.6, 9, 8, 9, 18, 1.442677]
        resultado = self.operacion.desviacionEstandar(lista)
        media = sum(lista) / len(lista)
        suma_cuadrados = sum((x - media) ** 2 for x in lista)
        esperado = math.sqrt(suma_cuadrados / len(lista))
        self.assertAlmostEqual(resultado, esperado, places=5)

    def test_desviacion_estandar_con_valores_invalidos(self):
        lista = [9, 3, 'a', 8, 5.6]
        resultado = self.operacion.desviacionEstandar(lista)
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    # Ejecución de pruebas
    unittest.main(exit=False)

    # Creación de objetos y manipulación de funciones
    operacion = Estadistica()
    lista = [9, 3, 8, 8, 5.6, 9, 8, 9, 18, 1.442677]
    print("Lista: " + ", ".join(str(x) for x in lista))
    print("Media: " + str(operacion.media(lista)))
    print("Desviación estándar: " + str(operacion.desviacionEstandar(lista)))
