from personaje import Personaje # importo classe Personaje

def main(): # Funcion main() crea una instancia del jugador y mustra su estado inicial
    # Crea personaje del jugador<<
    nombre_personaje = input("Por favor Indique el nombre de tu personaje: ")
    mi_personaje = Personaje(nombre_personaje)

    print("\n¡Bienvenido al juego Gran Fantasía!")
    mi_personaje.consultar_estado()

    # Crear una istancia del "Orco"
    orco = Personaje("Orco")

    # Calcula la probabilidad de ganar contra el orco, realiza el enfrentamiento con el orco y actualiza los estados del personaje segun el resultado
    probabilidad_ganar = mi_personaje.probabilidad_ganar(orco)
    experiencia_obtenida = mi_personaje.enfrentamiento_con_orco(probabilidad_ganar)
    mi_personaje.asignar_experiencia(experiencia_obtenida)

    print("\nEstado actual del personaje:")
    mi_personaje.consultar_estado()

if __name__ == "__main__": # el programa se ejecuta llamndo a la funcion main(), facilita la ejecucion del programa y la organizacion del codigo
    main()
