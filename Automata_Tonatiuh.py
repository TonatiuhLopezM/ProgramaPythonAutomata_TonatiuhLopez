def automata(word):
    # Estado inicial
    state = "q0"

    # Procesar cada símbolo de la palabra
    for symbol in word:
        if state == "q0":
            if symbol == 'a':
                state = "q1"
            elif symbol == 'b':
                state = "q2"
            else:
                return False  # Símbolo no reconocido
        elif state == "q1":
            if symbol == 'a' or symbol == 'b':
                state = "q1"
            else:
                return False
        elif state == "q2":
            if symbol == 'b':
                state = "q2"
            elif symbol == 'a':
                state = "q0"
            else:
                return False

    # Verificar si el estado final es de aceptación
    return state == "q1" or state == "q2"

def main():
    # Lista de palabras para probar
    palabras = ["ab", "ba", "aaa", "bba", "abb", "bbb", "aab"]

    for palabra in palabras:
        if automata(palabra):
            print(f"La palabra '{palabra}' es aceptada.")
        else:
            print(f"La palabra '{palabra}' no es aceptada.")

if __name__ == "__main__":
    main()
