from flask import render_template

from .models import ListaMovimientos
from . import app


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()
    return render_template('inicio.html', movs=lista.movimientos)


@app.route('/nuevo')
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV
    """
    return render_template('nuevo.html')


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
