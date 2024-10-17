# Función para imprimir la tabla de verdad de la implicación lógica con Falso y Verdadero
def tabla_verdad_implicacion():
    print("A       | B       | A → B")
    print("-------------------------")
    # Generar todas las combinaciones de A y B (Falso y Verdadero)
    for A in [False, True]:
        for B in [False, True]:
            resultado = (not A) or B
            print(f"{str(A):<8} | {str(B):<8} |   {str(bool(resultado))}")

# Llamada a la función para ejecutar el código
if __name__ == "__main__":
    tabla_verdad_implicacion()
