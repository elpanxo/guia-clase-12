def guardar_informe(ventas_totales):
    try:
        with open("informe_ventas.txt", "w") as archivo:
            archivo.write("Informe de Ventas Diarias\n\n")
            for producto, cantidad in ventas_totales.items():
                archivo.write(f"{producto}: {cantidad}\n")
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo para guardar el informe.")
    except Exception as e:
        print(f"Ocurrió un error al guardar el informe: {e}")
    finally:
        print("Informe de ventas guardado exitosamente.")

def main():
    productos_precios = {
        "pan ciabatta": 2000,
        "pie de limon": 3500,
        "café": 2200,
        "té": 1600,
        "alfajor": 1000
    }

    ventas_totales = {producto: 0 for producto in productos_precios}

    try:
        for producto, precio in productos_precios.items():
            while True:
                try:
                    cantidad = int(input(f"Ingrese la cantidad vendida de {producto}: "))
                    if cantidad < 0:
                        raise ValueError("La cantidad no puede ser negativa.")
                    ventas_totales[producto] += cantidad
                    break
                except ValueError as ve:
                    print(f"Error: {ve}. Por favor ingrese un número entero positivo.")

        total_ventas = sum(ventas_totales.values())
        print("\nInforme de Ventas Diarias\n")
        for producto, cantidad in ventas_totales.items():
            print(f"{producto}: {cantidad}")
        print(f"\nTotal de ventas del día: {total_ventas}")

        guardar_informe(ventas_totales)

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
