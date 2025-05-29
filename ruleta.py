"""
Este módulo contiene la clase Ruleta que simula el lanzamiento de una ruleta.
"""

import random

# ---- Definición única de los colores, para rendimiento ----
_ROJOS = {
    1, 3, 5, 7, 9, 12, 14, 16, 18,
    19, 21, 23, 25, 27, 30, 32, 34, 36
}

_COLORES = tuple(
    'v' if i == 0 else ('r' if i in _ROJOS else 'n')
    for i in range(37)
)

class Ruleta:
    """
    Simula lanzamientos de una ruleta Europea (0–36).
    """
    # ahora apuntas a los objetos ya construidos
    _rojos = _ROJOS
    _colores = _COLORES

    def lanzar(self):
        # randrange(37) es ligeramente más rápido que randint(0,36)
        numero = random.randrange(37)
        color = self._colores[numero]  # acceso O(1)
        return numero, color
    
    def lanzar_sesgado(self, sesgo: float = 0.0):
        """
        Lanza la ruleta con un sesgo.
        El sesgo es un número entre 0 y 1 que indica la probabilidad de que salga una sección específica,
        en este caso los numeros 5, 24, 16, 33, 1, 0
        """
        if not (0 <= sesgo <= 1):
            raise ValueError("El sesgo debe estar entre 0 y 1.")
        
        # Genera un número aleatorio con el sesgo aplicado
        if random.random() < sesgo:
            numero = random.choice([5, 24, 16, 33, 1, 0])
        else:
            numero = random.randrange(37)
        
        color = self._colores[numero]
        return numero, color