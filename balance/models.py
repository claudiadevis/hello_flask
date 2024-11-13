import csv
from datetime import date

from . import RUTA_FICHERO


class Movimiento:

    def __init__(self, fecha, concepto, tipo, cantidad):
        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            print(
                f'********** La fecha {fecha} no es una fecha ISO 8601 válida')

        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

    def __str__(self):
        return f'{self.fecha} | {self.concepto} | {self.tipo} | {self.cantidad}'


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_desde_archivo(self):
        self.movimientos = []
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                movimiento = Movimiento(
                    fila.get('fecha', None),
                    fila.get('concepto', 'Varios'),
                    fila.get('ingreso_gasto', '-'),
                    fila.get('cantidad', 0)
                )
                self.movimientos.append(movimiento)

    def __str__(self):
        result = ''
        for mov in self.movimientos:
            result += f'\n{mov}'
        return result
