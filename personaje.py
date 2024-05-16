import random 

class Personaje:
    def __init__(self, nombre): # Constructor (__init__):
#El constructor inicializa los atributos de instancia: nombre, nivel y experiencia.
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
# Accesadores y Mutadores
    def consultar_estado(self): # Muestra en pantalla el estado actual del personaje.
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Experiencia: {self.experiencia}")

    def asignar_experiencia(self, experiencia): # Actualiza la experiencia del personaje según las reglas especificadas.
        if experiencia >= 0:
            self.experiencia += experiencia
            while self.experiencia >= 100:
                self.nivel += 1
                self.experiencia -= 100
        else:
            self.experiencia += experiencia
            while self.experiencia < 0 and self.nivel > 1:
                self.nivel -= 1
                self.experiencia += 100
# Sobrecarga de Operadores
    def __lt__(self, otro_personaje): # Sobrecarga del operador “menor que” para comparar niveles.
        return self.nivel < otro_personaje.nivel

    def __gt__(self, otro_personaje): # Sobrecarga del operador “mayor que” para comparar niveles.
        return self.nivel > otro_personaje.nivel
# Probabilidad de Ganar
    def probabilidad_ganar(self, otro_personaje): # Calcula la probabilidad de ganar contra otro personaje según la diferencia de niveles.
        if self.nivel > otro_personaje.nivel:
            return 0.66
        elif self.nivel < otro_personaje.nivel: 
            
            return 0.33
        else:
            return 0.5

    def enfrentamiento_con_orco(self, probabilidad):  # Simula el enfrentamiento con el orco, generando un resultado aleatorio(random)
                                                      # y actualizando los estados según el resultado.
        print("\n¡Oh no!, Ha aparecido un orco!")
        print(f"Con tu nivel actual, tienes Probabilidad de ganar: {probabilidad * 100:.2f}%")

        opcion = int(input("¿Deseas atacar (1) o huir (2)? "))
        if opcion == 1:
            resultado_ataque = random.random()
            if resultado_ataque <= probabilidad:
                print("\n¡Has ganado Felicidades! Recibes 50 puntos de experiencia.")
                return 50
            else:
                print("\n¡Ho no!,¡Has perdido! Pierdes 30 puntos de experiencia.")
                return -30
        elif opcion == 2:
            print("Has decidido huir. El orco ha quedado atrás.")
            return 0
        else:
            print("Opción inválida. Se considera como huir.")
            return 0
