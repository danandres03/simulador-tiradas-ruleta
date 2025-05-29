import matplotlib.pyplot as plt

def plot(resultados: list, opcion: int) -> None:
    """
    Grafica los resultados de las tiradas
    """
    
    estrategias = {
        1: 'Martingala',
        2: 'Docena',
        3: 'James Bond',
        4: 'D\'alembert',
        5: 'Paroli',
        6: 'Labouchere',
        7: 'Retarded',
        8: 'Fibonacci'
    }

    estrategia = estrategias.get(opcion)
    if not estrategia:
        estrategia = 'Otra'
        
    longitud = len(max(resultados, key=len))
    x = list(range(longitud))
    
    for i, lista in enumerate(resultados):
        plt.plot(x[:len(lista)], lista, label=f'Simulación {i+1}')
        
    plt.title("""Evolución del balance con Tiradas de Ruleta
    Estrategia {}""".format(estrategia))
    
    plt.xlabel('Tiradas de Ruleta')
    plt.ylabel('Balance')
    plt.grid(True)
    plt.legend()
    
    plt.show()