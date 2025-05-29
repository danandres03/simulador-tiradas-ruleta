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