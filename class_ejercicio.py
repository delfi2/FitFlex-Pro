class ejercicio:

    def __init__(self, ID, ejercicio, dificultad) -> None:
        self.ID = ID
        self.ejercicio = ejercicio
        self.dificultad = dificultad

class ejercicio_gym:
     def __init__(self, ID, ejercicio, dificultad, repeticiones, series, peso) -> None:
         super().__init__(repeticiones, series, peso)
         self.repeticiones = repeticiones
         self.series = series
         self.peso = peso
class ejercicio_run:
     def __init__(self, ID, ejercicio, dificultad, distancia, tiempo) -> None:
         super().__init__(repeticiones, series, peso)
         self.distancia = distancia
         self.tiempo = series
