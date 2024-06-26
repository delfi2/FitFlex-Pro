class Ejercicios:
    def __init__(self, ID, ejercicio, dificultad) -> None:
        self.ID = ID
        self.ejercicio = ejercicio
        self.dificultad = dificultad

    def serialize(self):
        return {
            'ID': self.ID,
            'ejercicio': self.ejercicio,
        }

    def serialize_detail(self):
        return {
            'ID': self.ID,
            'ejercicio': self.ejercicio,
            'dificultad': self.dificultad
        }

    def __describir(self):
        return f"Ejercicio: {self.ejercicio}, Dificultad: {self.dificultad}"


class ejercicio_gym(Ejercicios):
    def __init__(self, ID, ejercicio, dificultad, repeticiones, serie, peso) -> None:
        super().__init__(ID, ejercicio, dificultad)
        self.repeticiones = repeticiones
        self.serie = serie
        self.peso = peso

    def serialize(self):
        return {
            'ID': self.ID,
            'ejercicio': self.ejercicio,
            'repeticiones': self.repeticiones,
        }

    def serialize_detail(self):
        return {
            'ID': self.ID,
            'ejercicio': self.ejercicio,
            'dificultad': self.dificultad,
            'repeticiones': self.repeticiones,
            'serie': self.serie,
            'peso': self.peso
        }

    def __describir(self):
        descripcion_base = super().describir()
        return f"{descripcion_base}, Repeticiones: {self.repeticiones}, Serie: {self.serie}, Peso: {self.peso}kg"


class ejercicio_run(Ejercicios):
    def __init__(self, ID, ejercicio, dificultad, distancia, tiempo) -> None:
        super().__init__(ID, ejercicio, dificultad)
        self.distancia = distancia
        self.tiempo = tiempo

    def serialize(self):
        return {
            'ID': self.ID,
            'ejercicio': self.ejercicio,
            'distancia': self.distancia
        }

    def serialize_detail(self):
        return {
            'ID': self.ID,
            'ejercicio': self.ejercicio,
            'dificultad': self.dificultad,
            'distancia': self.distancia,
            'tiempo': self.tiempo
        }

    def __describir(self):
        descripcion_base = super().describir()
        return f"{descripcion_base}, Distancia: {self.distancia}km, Tiempo: {self.tiempo}min"
