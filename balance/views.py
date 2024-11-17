from flask import render_template, request

from .models import ListaMovimientos, Movimiento
from . import app


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()
    return render_template('inicio.html', movs=lista.movimientos)


@app.route('/nuevo', methods=['GET', 'POST'])
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV
    """
    if request.method == 'GET':
        return render_template('nuevo.html')
    if request.method == 'POST':
        lista = ListaMovimientos()
        # TODO: crear un movimiento, agregarlo a la lista, guardar la lista y devolver el texto 'OK' (o 'ERROR' si falla)
        mov = request.form

        lista.leer_desde_archivo()
        resultado = lista.agregar_mov(mov)
        lista.guardar()

        return resultado


@app.route('/modificar')
def update():
    """
    Permite editar los datos de un movimiento creado previamente.
    """
    return 'Actualizar movimiento'


@app.route('/borrar')
def delete():
    """
    Elimina un movimiento existente
    """
    return 'Borrar movimiento'
