import csv
from datetime import date

from . import RUTA_FICHERO


class Movimiento:

    def __init__(self, fecha, concepto, tipo, cantidad):
        self.errores = []
        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            mensaje = f'La fecha {
                fecha} no es una fecha ISO 8601 válida (o no se ha agregado ninguna fecha)'
            self.errores.append(mensaje)

        self.concepto = concepto

        if not (tipo == 'I' or tipo == 'G'):
            self.tipo = None
            mensaje = f'El tipo debe ser Ingreso o Gasto'
            self.errores.append(mensaje)
        else:
            self.tipo = tipo

        if (cantidad == ''):
            mensaje = 'No se ha agregado ninguna cantidad'
            self.errores.append(mensaje)
        elif not (float(cantidad) >= 0):
            self.cantidad = 0
            mensaje = f'El valor {cantidad} no es un número positivo'
            self.errores.append(mensaje)
        else:
            self.cantidad = cantidad

    @property
    def has_errors(self):
        return len(self.errores) > 0

    def __str__(self):
        return f'{self.fecha} | {self.concepto} | {self.tipo} | {self.cantidad}'

    def __repr__(self):
        return self.__str__()


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
                    fila.get('tipo', '-'),
                    fila.get('cantidad', 0)
                )
                self.movimientos.append(movimiento)

    def guardar(self):
        with open(RUTA_FICHERO, 'w') as fichero:
            # cabeceras = ['fecha', 'concepto', 'tipo', 'cantidad']
            # writer = csv.writer(fichero)
            # writer.writerow(cabeceras)

            cabeceras = list(self.movimientos[0].__dict__.keys())
            cabeceras.remove('errores')

            writer = csv.DictWriter(fichero, fieldnames=cabeceras)
            writer.writeheader()

            for mov in self.movimientos:
                mov_dict = mov.__dict__
                mov_dict.pop('errores')
                writer.writerow(mov_dict)

    def agregar_mov(self, mov):
        # print({mov})
        fecha = str(mov.get('date'))
        concepto = mov.get('subject')
        tipo = mov.get('mov_type')
        cantidad = mov.get('amount')
        nuevo_mov = Movimiento(fecha, concepto, tipo, cantidad)
        self.movimientos.append(nuevo_mov)
        if nuevo_mov.errores == []:
            result = 'OK'
        else:
            result = f'ERROR: {
                nuevo_mov.errores}'
        return result

    def __str__(self):
        result = ''
        for mov in self.movimientos:
            result += f'\n{mov}'
        return result
