class ejercicios:
    def __init__(self, ID, ejercicio, dificultad) -> None:
        self.ID = ID
        self.ejercicio = ejercicio
        self.dificultad = dificultad

    def describir(self):
        return f"Ejercicio: {self.ejercicio}, Dificultad: {self.dificultad}"

class EjercicioGym(ejercicios):
    def __init__(self, ID, ejercicio, dificultad, repeticiones, serie, peso) -> None:
        super().__init__(ID, ejercicio, dificultad)
        self.repeticiones = repeticiones
        self.serie = serie
        self.peso = peso

    def describir(self):
        descripcion_base = super().describir()
        return f"{descripcion_base}, Repeticiones: {self.repeticiones}, Serie: {self.serie}, Peso: {self.peso}kg"

class EjercicioRun(ejercicios):
    def __init__(self, ID, ejercicio, dificultad, distancia, tiempo) -> None:
        super().__init__(ID, ejercicio, dificultad)
        self.distancia = distancia
        self.tiempo = tiempo

    def describir(self):
        descripcion_base = super().describir()
        return f"{descripcion_base}, Distancia: {self.distancia}km, Tiempo: {self.tiempo}min"

