"""
Este módulo contiene varias funciones que simulan diferentes estrategias de apuestas en el juego de la ruleta.
"""

class Estrategia:
    """
    Clase base para estrategias de apuestas en la ruleta.
    """
    def __init__(self, ruleta):
        self.ruleta = ruleta

    def martingala(self, resultados: list, jugadas: int, balance: float, apuesta_doblada: float, apuesta: float) -> list:
        """
        Simula la estrategia de Martingala
        """

        while jugadas != 0 and balance > 0:
            balance -= apuesta_doblada
            _, color = self.ruleta.lanzar()
            
            if color == 'r' or color == 'v': # perdida
                
                resultados.append(balance)
                apuesta_doblada *= 2
                if balance - apuesta_doblada <= 0:
                    break
                
            elif color == 'n': # ganancia
                
                balance += (apuesta_doblada*2)
                resultados.append(balance)
                apuesta_doblada = apuesta 
            
            jugadas -= 1
        return resultados

    def docena(self, resultados: list, jugadas: int, balance: float, apuesta: float) -> list:
        """
        Simula la estrategia de Docena
        """
        valid = [13, 14, 15, 17, 18, 20, 21, 22, 23, 24]
        while jugadas != 0 and balance > 0:
            balance -= apuesta
            number, _ = self.ruleta.lanzar()
            
            if (number >= 1 and number <= 12) or (number >= 25 and number <= 36):
                balance += apuesta
            elif number in valid:
                balance += ((apuesta/30) * 36)
                
            resultados.append(balance)
            jugadas -= 1
        return resultados

    def james_bond(self, resultados: list, jugadas: int, balance: float, apuesta: float) -> list:
        """
        Simula la estrategia de James Bond
        """
        while jugadas != 0 and balance > 0:
            apuesta_1 = apuesta * 0.7
            apuesta_2 = apuesta * 0.25
            apuesta_3 = apuesta * 0.05 
            balance -= apuesta_1 + apuesta_2 + apuesta_3
            number, _ = self.ruleta.lanzar()
            
            if number >= 19 and number <= 36:
                balance += apuesta_1 * 2
            elif number >= 13 and number <= 18:
                balance += apuesta_2 * 6
            elif number == 0:
                balance += apuesta_3 * 36
                
            resultados.append(balance)
            jugadas -= 1
        return resultados

    def dalembert(self, resultados: list, jugadas: int, balance: float, apuesta_doblada: float)-> list:
        """
        Simula la estrategia de D'alembert
        """
        while jugadas != 0 and balance > 0:
            balance -= apuesta_doblada
            _, color = self.ruleta.lanzar()
            
            if color == 'r' or color == 'v': # perdida
                
                resultados.append(balance)
                apuesta_doblada += 1
                
                if balance - apuesta_doblada <= 0:
                    break
                
            elif color == 'n': # ganancia
                
                balance += (apuesta_doblada*2)
                resultados.append(balance)
                apuesta_doblada -= 1
            
            jugadas -= 1
        return resultados

    def paroli(self, resultados: list, jugadas: int, balance: float, apuesta_doblada: float, apuesta: float)-> list:
        """
        Simula la estrategia de Paroli
        """
        while jugadas != 0 and balance > 0:
            balance -= apuesta_doblada
            _, color = self.ruleta.lanzar()
            
            if color == 'r' or color == 'v': # perdida
                apuesta_doblada = apuesta
                
            elif color == 'n': # ganancia
                
                balance += (apuesta_doblada*2)
                apuesta_doblada *= 2
                
            resultados.append(balance)
            jugadas -= 1
        return resultados

    def labouchere(self, resultados: list, balance: float, apuesta: float, objetivo: int, secuencia: list)-> list:
        """
        Simula la estrategia de Labouchere
        """
        while balance < objetivo:  
            if secuencia == []:
                break
            
            elif len(secuencia) == 1:
                
                apuesta = secuencia[0]
                
            else:
                apuesta = secuencia[0] + secuencia[-1]
                
            balance -= apuesta
            _, color = self.ruleta.lanzar()
            
            if color == 'r' or color == 'v':
                secuencia.append(apuesta)
                
            elif color == 'n':
                
                balance += apuesta * 2
                
                if secuencia != [] and len(secuencia) > 1:
                    
                    secuencia.pop(0)
                    secuencia.pop(-1)
                elif secuencia != [] and len(secuencia) == 1:
                    
                    secuencia.pop(0)
                
            resultados.append(balance)
        return resultados

    def stupid(self, resultados: list, jugadas: int, balance: float, apuesta: float)-> list:
        """
        Simula la estrategia stupid, apostar siempre al 0
        """
        while jugadas != 0:
            balance -= apuesta
            _, color = self.ruleta.lanzar()
            if color == 'v':
                balance += apuesta * 36
            resultados.append(balance)
            jugadas -= 1
        return resultados

    def fibonacci(self, resultados: list, jugadas: int, balance: float, apuesta: float, apuestaref:float)-> list:
        """
        Simula la estrategia de Fibonacci
        """
        fibonacci_sequence = [1, 1]
        apuesta = apuestaref = 2
        for _ in range(jugadas):
            balance -= apuesta
            _, color = self.ruleta.lanzar()
            if color == 'n':  # Ganancia
                balance += apuesta*2
                fibonacci_sequence = [1, 1]  # Reiniciar la secuencia después de una victoria
                apuesta = apuestaref
            else:
                fibonacci_sequence.append(apuesta)
                apuesta = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            resultados.append(balance)
        return resultados
    
    def pelayo(self, resultados: list, jugadas: int, balance: float, apuesta: float) -> list:
        """
        Simula la estrategia de los Pelayo, donde unos numeros ten una probabilidad de salir mayor que otr
        minima. Solo apuesta a los números 5, 24, 16, 33, 1 y 0.
        """
        while jugadas != 0 and balance > 0:
            balance -= apuesta
            number, _ = self.ruleta.lanzar_sesgado(sesgo=0.005)
            if number in {5, 24, 16, 33, 1, 0}:
                balance += apuesta * 36
            resultados.append(balance)
            jugadas -= 1
        return resultados

            
            
            