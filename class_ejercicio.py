class ejercicio:

    def __init__(self, ID, ejercicio, dificultad) -> None:
        self.ID = ID
        self.ejercicio = ejercicio
        self.dificultad = dificultad

class ejercicio_gym(ejercicio):
     def __init__(self, ID, ejercicio, dificultad, repeticiones, serie, peso) -> None:
         super().__init__(repeticiones, serie, peso)
         self.repeticiones = repeticiones
         self.serie = serie
         self.peso = peso
class ejercicio_run(ejercicio):
     def __init__(self, ID, ejercicio, dificultad, distancia, tiempo) -> None:
         super().__init__(distancia, tiempo)
         self.distancia = distancia
         self.tiempo = tiempo
