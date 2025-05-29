"""
Este módulo contiene la clase Ruleta que simula el lanzamiento de una ruleta.
"""

import random

class Ruleta:
    """
    Clase que simula el lanzamiento de la ruleta.
    """
    def lanzar(self):
        rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        numero = random.randint(0, 36)
        if numero in rojos:
            color = 'r'
        elif numero != 0:
            color = 'n'
        else:
            color = 'v'
        return numero, color