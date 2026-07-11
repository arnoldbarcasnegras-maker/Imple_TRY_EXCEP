# Implementación de la recuperación try-except
# Asegurar la robustez del sistema implementando la gestión de errores y excepciones try-except 
class Transaccion:
    """Representa una transacción financiera con validación de montos."""

    def __init__(self, cliente_id, tipo, valor):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.valor = valor           # Activa el validador (setter)

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, nuevo_valor):
        """Valida y encapsula el valor de la transacción.
            Raises:
            ValueError: Si el monto no es numérico, es negativo o supera 100M.
        """
        if int(nuevo_valor) < 0:
            raise ValueError("el valor no puede ser negativo")
        elif int(nuevo_valor) > 100000000:
            raise ValueError("El valor no puede superar 100 millones")
        self._valor = int(nuevo_valor)

    def __str__(self):
        return f"{self.cliente_id} | {self.tipo} | ${self.valor}"


# 2) Lectura TOLERANTE A FALLOS: un try/except por cada linea
def cargar_transacciones(nombre_archivo):
    """Lee transacciones desde un archivo manejando registros corruptos de forma tolerante.
       Args:
        nombre_archivo (str): Ruta del archivo de texto.
        Returns:
        list: Objetos Transaccion creados exitosamente.
    """
    transacciones = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, start=1):
            linea = linea.strip()
            if not linea:
                continue  # ignora lineas en blanco
            try:
                partes = linea.split(",")
                transacciones.append(Transaccion(*partes))
            except ValueError as error:
                print(f"  [Linea {numero}] ValueError: {error}  ->  se ignora: {linea}")
            except TypeError:
                print(f"  [Linea {numero}] TypeError: datos insuficientes  ->  se ignora: {linea}")
    return transacciones


def ejecutar_sistema():
    """Punto de entrada para cargar y listar las transacciones válidas."""
    transacciones = cargar_transacciones("transacciones_corruptas.txt")

    print()
    print(f"Se procesaron {len(transacciones)} transacciones validas:")
    for t in transacciones:
        print("  ", t)



if __name__ == "__main__":
    ejecutar_sistema()