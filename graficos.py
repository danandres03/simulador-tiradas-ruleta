import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import polars as pl

def plot(resultados: list, opcion: int) -> None:
    """
    Grafica los resultados de las tiradas usando seaborn.
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
    estrategia = estrategias.get(opcion, 'Otra')

    # Estilo general de seaborn
    sns.set_theme(style="whitegrid", font_scale=1.1)

    # Preparo figura
    fig, ax = plt.subplots(figsize=(10, 6))

    # Genero el eje X según la simulación más larga
    max_len = max(len(r) for r in resultados)
    x = list(range(max_len))

    # Dibujamos cada simulación con lineplot de seaborn
    for idx, serie in enumerate(resultados, start=1):
        sns.lineplot(
            x=x[:len(serie)],
            y=serie,
            ax=ax,
            label=f"Simulación {idx}",
            linewidth=1,
            alpha=0.7
        )

    # Línea horizontal en y=0 para referencia
    ax.axhline(0, linestyle="--", linewidth=1.2, color="gray", alpha=0.8)

    # Títulos y etiquetas
    ax.set_title(
        "Evolución del balance con Tiradas de Ruleta\n"
        f"Estrategia {estrategia}",
        pad=12
    )
    ax.set_xlabel("Tiradas de Ruleta")
    ax.set_ylabel("Balance")

    # Leyenda fuera del plot
    ax.legend(
        loc='upper left',
        bbox_to_anchor=(1.02, 1),
        borderaxespad=0,
        frameon=True,
        title="Simulaciones"
    )

    # Ajuste de márgenes
    fig.tight_layout()
    plt.show()  

def graf_media_con_bandas(resultados):
    """ Grafica la trayectoria media de las simulaciones con bandas de confianza. 
    Debido a la carga de trabajo, se usa Polars para el cálculo eficiente.

    Args:
        resultados (list): Lista de listas con los balances de cada simulación.
    """
    # ajustamos todas a la misma longitud: rellenar con NaN
    max_len = max(len(s) for s in resultados)
    padded = [serie + [None] * (max_len - len(serie)) for serie in resultados]
    # cambiar filas por columnas
    padded = np.array(padded).T.tolist()  # Transponer para que cada fila sea una simulación
    # convertimos a DataFrame de Polars
    df = pl.DataFrame(padded).cast(pl.Float64)

    # calculamos media y percentiles 10%/90%
    media = df.mean().to_numpy().ravel()           # shape (max_len,)
    p10   = df.quantile(0.1).to_numpy().ravel()  # shape (max_len,)
    p90   = df.quantile(0.9).to_numpy().ravel()  # shape (max_len,)
    
    # generamos el eje X
    x = np.arange(max_len)
    
    plt.figure(figsize=(10,5))
    plt.plot(x, media, label="Media", color="navy")
    plt.fill_between(x, p10, p90, color="navy", alpha=0.2, label="10–90 percentil")
    plt.axhline(0, linestyle="--", color="gray")
    plt.title("Trayectoria media con banda de confianza")
    plt.xlabel("Tiradas")
    plt.ylabel("Balance")
    plt.legend()
    plt.tight_layout()
    plt.show()