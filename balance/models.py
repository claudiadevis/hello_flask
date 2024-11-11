import csv

from . import RUTA_FICHERO


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_desde_archivo(self):
        self.movimientos = []
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                self.movimientos.append(fila)

    def __str__(self):
        result = ''
        for mov in self.movimientos:
            result += f'\n{mov}'
        return result
