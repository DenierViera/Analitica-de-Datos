import json


class ManejadorJSON:

    def __init__(self):
        self.datos = None
        self.registros_procesados = 0
        self.modificaciones = []

    def importar_json(self, ruta):
        """Importa y carga la información de un archivo JSON."""

        with open(ruta, "r", encoding="utf-8") as archivo:
            self.datos = json.load(archivo)

        if isinstance(self.datos, (list, dict)):
            self.registros_procesados = len(self.datos)
        else:
            self.registros_procesados = 1

        return self.datos

    def modificar_registro(self, indice, clave, nuevo_valor):
        """Modifica un campo de un registro dentro de una lista JSON."""

        if not isinstance(self.datos, list):
            raise TypeError("El JSON no contiene una lista de registros.")

        if indice < 0 or indice >= len(self.datos):
            raise IndexError("El índice del registro no es válido.")

        if not isinstance(self.datos[indice], dict):
            raise TypeError("El registro seleccionado no es un objeto JSON.")

        valor_anterior = self.datos[indice].get(clave)

        self.datos[indice][clave] = nuevo_valor

        self.modificaciones.append({
            "indice": indice,
            "campo": clave,
            "valor_anterior": valor_anterior,
            "valor_nuevo": nuevo_valor
        })

        return valor_anterior, nuevo_valor

    def guardar_json(self, ruta):
        """Guarda los datos modificados en un nuevo archivo JSON."""

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(self.datos, archivo, ensure_ascii=False, indent=4)

        return ruta