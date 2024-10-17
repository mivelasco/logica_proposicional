# Función para imprimir la tabla de verdad de una compuerta OR
def tabla_verdad_or():
    print("A | B | A OR B")
    print("---------------")
    # Generar todas las combinaciones de A y B (0 y 1)
    for A in [0, 1]:
        for B in [0, 1]:
            resultado = A or B
            print(f"{A} | {B} |   {resultado}")

# Llamada a la función para ejecutar el código
if __name__ == "__main__":
    tabla_verdad_or()
