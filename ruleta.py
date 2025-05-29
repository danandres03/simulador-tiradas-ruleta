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
        
        numeros_sesgados = {5, 24, 16, 33, 1, 0}
        total_numeros = 37
        p_base = 1 / total_numeros

        # Distribución de probabilidades con sesgo sumando a los sesgados
        p_sesgado = p_base + sesgo
        suma_sesgados = p_sesgado * len(numeros_sesgados)
        p_otros = (1 - suma_sesgados) / (total_numeros - len(numeros_sesgados))

        if p_otros < 0:
            raise ValueError("El sesgo es demasiado alto y rompe la distribución de probabilidad.")

        # Generar la lista de probabilidades
        numeros = list(range(37))
        probabilidades = [p_sesgado if n in numeros_sesgados else p_otros for n in numeros]

        numero = random.choices(numeros, weights=probabilidades)[0]
        color = self._colores[numero]
        return numero, color