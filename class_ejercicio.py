class ejercicio:

    def __init__(self, ID, ejercicio, dificultad) -> None:
        self.ID = ID
        self.ejercicio = ejercicio
        self.dificultad = dificultad


    def serialize(self):
        return {
            'ID': self.ID,
            'ejercicio': self.ejercicio,
            'repeticiones': self.repeticiones,
            'serie': self.serie
        }

    def serialize_details(self):
        return {
            'ID': self.ID,
            'ejercicio': self.ejercicio,
            'repeticiones': self.repeticiones,
            'tiempo': self.tiempo,
            'peso': self.peso,
            'fortalece': self.fortalece,
            'serie': self.serie,
            'dificultad': self.dificultad
        }
class ejercicio_gym:
     def __init__(self, ID, ejercicio, dificultad, repeticiones, series, peso) -> None:
         super().__init__(repeticiones, series, peso)
         self.repeticiones = repeticiones
         self.series = series
         self.peso = peso
    

