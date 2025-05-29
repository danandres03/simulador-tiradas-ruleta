"""
Este script permite al usuario simular tiradas de una ruleta con la estrategia preferida y graficar los resultados.
Las estrategias disponibles son:
- Martingale
- Dozen
- James Bond
- D'alembert
- Paroli (Inverse Martingale)
- Labouchere
- Stupid
- Fibonacci

Se pide al usuario que decida la estrategia e ingrese los datos necesarios para la simulación.
El script luego simula la estrategia y grafica los resultados.

El gráfico después representa la evolución del balance conforme a las tiradas de la ruleta, siendo cada linea una simulación
"""
from estrategias import Estrategia
from ruleta import Ruleta
from graficos import *

# Funciones para recoger inputs según estrategia

def coleccion_balance_apuesta():
    """Balance y apuesta simples"""
    balance = float(input("Ingrese el balance: "))
    apuesta = float(input("Ingrese la apuesta: "))
    return {
        "balance": balance,
        "apuesta": apuesta
    }

def coleccion_balance_apuesta_doblada_y_apuesta():
    """Balance, apuesta inicial y apuesta_doblada = apuesta"""
    balance = float(input("Ingrese el balance: "))
    apuesta = float(input("Ingrese la apuesta: "))
    return {
        "balance": balance,
        "apuesta": apuesta,
        "apuesta_doblada": apuesta
    }

def coleccion_balance_apuesta_doblada_solo():
    """Balance y apuesta_doblada (sin parámetro 'apuesta' extra)"""
    balance = float(input("Ingrese el balance: "))
    apuesta = float(input("Ingrese la apuesta: "))
    return {
        "balance": balance,
        "apuesta_doblada": apuesta
    }

def coleccion_labouchere():
    """Secuencia para Labouchere"""
    raw = input("Ingrese la secuencia (p.ej. 1-2-3-4): ")
    secuencia = [int(n) for n in raw.split("-") if n.strip().isdigit()]
    objetivo = sum(secuencia)
    apuesta = secuencia[0] + secuencia[-1]
    # Labouchere comienza con balance=0
    return {
        "balance": 0.0,
        "apuesta": apuesta,
        "secuencia": secuencia,
        "objetivo": objetivo
    }

def coleccion_fibonacci():
    """Fibonacci: apuesta inicial 2, balance inicial 0"""
    print("Para Fibonacci: apuesta inicial = 2, balance inicial = 0")
    return {
        "balance": 0.0,
        "apuesta": 2.0,
        "apuestaref": 2.0
    }

# Mapeo de opciones a configuración de estrategia 

ESTRATEGIAS = {
    1: {
        "nombre":   "Martingala",
        "metodo":   "martingala",
        "collector": coleccion_balance_apuesta_doblada_y_apuesta,
        "uses_jugadas": True
    },
    2: {
        "nombre":   "Docena",
        "metodo":   "docena",
        "collector": coleccion_balance_apuesta,
        "uses_jugadas": True
    },
    3: {
        "nombre":   "James Bond",
        "metodo":   "james_bond",
        "collector": coleccion_balance_apuesta,
        "uses_jugadas": True
    },
    4: {
        "nombre":   "D'alembert",
        "metodo":   "dalembert",
        "collector": coleccion_balance_apuesta_doblada_solo,
        "uses_jugadas": True
    },
    5: {
        "nombre":   "Paroli",
        "metodo":   "paroli",
        "collector": coleccion_balance_apuesta_doblada_y_apuesta,
        "uses_jugadas": True
    },
    6: {
        "nombre":   "Labouchere",
        "metodo":   "labouchere",
        "collector": coleccion_labouchere,
        "uses_jugadas": False
    },
    7: {
        "nombre":   "Stupid",
        "metodo":   "stupid",
        "collector": coleccion_balance_apuesta,
        "uses_jugadas": True
    },
    8: {
        "nombre":   "Fibonacci",
        "metodo":   "fibonacci",
        "collector": coleccion_fibonacci,
        "uses_jugadas": True
    }
}

def main():
    ruleta = Ruleta()
    estrategias = Estrategia(ruleta)

    # — Mostrar menú —
    print("------ MENÚ PRINCIPAL ------")
    for key, cfg in ESTRATEGIAS.items():
        print(f"{key}. {cfg['nombre']}")
    print("Otro. Salir")
    print("-----------------------------")

    # — Leer opción válida —
    while True:
        try:
            opcion = int(input("Ingrese la estrategia: "))
            if opcion in ESTRATEGIAS:
                break
            print("Opción inválida, intente de nuevo.")
        except ValueError:
            print("Por favor ingrese un número entero.")

    cfg = ESTRATEGIAS[opcion]

    # — Recoger parámetros específicos —
    params = cfg["collector"]()

    # — Número de jugadas (si aplica) y simulaciones —
    if cfg["uses_jugadas"]:
        jugadas = int(input("Ingrese el número de jugadas (-1 para infinito): "))
    else:
        jugadas = None

    simulaciones = int(input("Ingrese el número de simulaciones: "))

    # — Ejecutar simulaciones y almacenar resultados —
    compuesto = []
    metodo = getattr(estrategias, cfg["metodo"])
    for _ in range(simulaciones):
        resultados = [params["balance"]]
        params_copy = params.copy()
        if opcion == 6:
            params_copy["secuencia"] = params_copy["secuencia"].copy()
        if cfg["uses_jugadas"]:
            resultados = metodo(resultados, jugadas, **params_copy)
        else:
            resultados = metodo(resultados, **params_copy)
        compuesto.append(resultados)

    # — Mostrar gráfico —
    plot(compuesto, opcion)
    graf_media_con_bandas(compuesto)

if __name__ == "__main__":
    main()
