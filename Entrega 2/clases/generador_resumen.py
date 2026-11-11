class GeneradorResumen:

    def __init__(self):
        self.contenido = []

    def agregar_seccion(self, titulo, informacion):
        """Agrega una sección de información al resumen."""

        self.contenido.append(f"\n{titulo}")
        self.contenido.append("-" * 50)
        self.contenido.append(informacion)

    def generar_resumen(self, ruta):
        """Genera y guarda el resumen del procesamiento."""

        texto = "\n".join(self.contenido)

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)

        return ruta