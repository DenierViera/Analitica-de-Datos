
import csv


class ManejadorCSV:

    def __init__(self):
        self.encabezados = []
        self.datos = []
        self.registros_procesados = 0
        self.modificaciones = []

    def importar_csv(self, ruta):
        """Importa un archivo CSV y separa encabezados y registros."""

        with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.reader(archivo)

            self.encabezados = next(lector)
            self.datos = list(lector)

        self.registros_procesados = len(self.datos)

        return self.encabezados, self.datos

    def modificar_valor(self, numero_fila, columna, nuevo_valor):
        """Modifica un valor específico del CSV."""

        if columna not in self.encabezados:
            raise ValueError(f"La columna '{columna}' no existe.")

        if numero_fila < 0 or numero_fila >= len(self.datos):
            raise IndexError("El número de fila no es válido.")

        indice_columna = self.encabezados.index(columna)
        valor_anterior = self.datos[numero_fila][indice_columna]

        self.datos[numero_fila][indice_columna] = str(nuevo_valor)

        self.modificaciones.append({
            "fila": numero_fila,
            "columna": columna,
            "valor_anterior": valor_anterior,
            "valor_nuevo": str(nuevo_valor)
        })

        return valor_anterior, nuevo_valor

    def guardar_csv(self, ruta):
        """Guarda los datos modificados en un nuevo archivo CSV."""

        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)

            escritor.writerow(self.encabezados)
            escritor.writerows(self.datos)

        return ruta
