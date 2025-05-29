"""
Este script permite al usuario simular tiradas de una ruleta con la estrategia preferida y graficar los resultados.
Las estrategias disponibles son:
- Martingale
- Dozen
- James Bond
- D'alembert
- Paroli (Inverse Martingale)
- Labouchere
- Retarded
- Fibonacci

Se pide al usuario que decida la estrategia e ingrese los datos necesarios para la simulación.
El script luego simula la estrategia y grafica los resultados.

El gráfico después representa la evolución del balance conforme a las tiradas de la ruleta, siendo cada linea una simulación

El script requiero los siguientes imports:
- estrategias
- matplotlib.pyplot
"""
from estrategias import Estrategia
from ruleta import Ruleta
from graficos import plot

menu = """
------MENU PRINCIPAL------
Elija la estrategia que desea utilizar
1. Martingala
2. Docena
3. James Bond
4. D'alembert
5. Paroli (Martingala inversa)
6. Labouchere
7. Retarded
8. Fibonacci
Otro. Salir
--------------------------
"""

if __name__ == "__main__":
    print(menu)
    secuenciaref = None
    objetivo = 0
    balanceref = None
    apuestaref = None
    while True:
        opcion = input("Ingrese la estrategia: ")
        try:
            opcion = int(opcion)
            if opcion >= 1 and opcion <= 8:
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Por favor, ingrese un número entero.")

    if opcion == 1 or opcion == 4 or opcion == 5:
        print("La apuesta recomendada debe ser entre el 0.33% y 1% del balance")
    if opcion == 6:
        secuenciaref = input("Ingrese la secuencia separadas por '-': ")
        secuenciaref = [int(num) for num in secuenciaref.split('-')]
        objetivo = sum(secuenciaref)
        balanceref = 0
        apuestaref = secuenciaref[0] + secuenciaref[-1]
    elif opcion == 8:
        print("""
Para esta estrategia, se predetermina que la apuesta inicial es de 2
y el balance inicial es de 0. No introducir -1 en el número de jugadas,
ya que la secuencia de Fibonacci es infinita.""")
        balanceref = 0
        apuestaref = 2
    if opcion != 6 and opcion != 8:
        balanceref = float(input("Ingrese el balance: "))
        apuestaref = float(input("Ingrese la apuesta: "))
    jugadasref = int(input("Ingrese el numero de jugadas (-1 para infinto): "))
    simulaciones = int(input("Ingrese el numero de simulaciones: "))
    compuesto = []
    apuesta_doblada = apuestaref
    ruleta = Ruleta()
    estrategias = Estrategia(ruleta)
    while simulaciones > 0:
        resultados = []
        apuesta = apuestaref if apuestaref is not None else 0
        apuesta_doblada = apuestaref if apuestaref is not None else 0
        balance = balanceref if balanceref is not None else 0
        jugadas = jugadasref
        if secuenciaref is not None:
            secuencia = secuenciaref.copy()
        else:
            secuencia = None
        resultados.append(balance)
        if opcion == 1: # Martingala
            resultados = estrategias.martingala(resultados, jugadas, balance, apuesta_doblada, apuesta)
        elif opcion == 2: # Docena
            resultados = estrategias.docena(resultados, jugadas, balance, apuesta)
        elif opcion == 3: # James Bond
            resultados = estrategias.james_bond(resultados, jugadas, balance, apuesta)
        elif opcion == 4: # D'alembert
            resultados = estrategias.dalembert(resultados, jugadas, balance, apuesta_doblada)
        elif opcion == 5: # Paroli
            resultados = estrategias.paroli(resultados, jugadas, balance, apuesta_doblada, apuesta)
        elif opcion == 6: # Labouchere
            if secuencia is not None:
                apuesta_labouchere = float(apuestaref) if apuestaref is not None else 0.0
                resultados = estrategias.labouchere(resultados, balance, apuesta_labouchere, objetivo, secuencia)
            else:
                print("Secuencia no definida para Labouchere.")
                break
        elif opcion == 7: # Retarded
            resultados = estrategias.retarded(resultados, jugadas, balance, apuesta)
        elif opcion == 8: # Fibonacci
            apuestaref_fibo = float(apuestaref) if apuestaref is not None else 2.0
            resultados = estrategias.fibonacci(resultados, jugadas, balance, apuesta, apuestaref_fibo)
        else:
            print("Not implemented yet")
            break
        simulaciones -= 1
        compuesto.append(resultados)
    plot(compuesto, opcion)