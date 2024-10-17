# Función para imprimir la tabla de verdad de una compuerta AND
def tabla_verdad_and():
    print("A | B | A AND B")
    print("----------------")
    # Generar todas las combinaciones de A y B (0 y 1)
    for A in [0, 1]:
        for B in [0, 1]:
            resultado = A and B
            print(f"{A} | {B} |   {resultado}")

# Llamada a la función para ejecutar el código
if __name__ == "__main__":
    tabla_verdad_and()
