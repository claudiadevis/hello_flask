# hello-flask

Conocemos el framework para web: Flask

## A tener en cuenta

Flask necesita un servidor web para funcionar.
El servidor web es el encargado de recibir las peticiones
HTTP del navegador y enviarlas al programa que
hacemos en Flask. Flask le da el resultado al servidor
web y este se lo envía al navegador.

Para simplificar el escenario, por el momento solamente
vamos a utilizar el **SERVIDOR WEB DE DESARROLLO** que nos
proporciona Flask. Este servidor **NO SIRVE para poner una
aplicación pública en internet en modo PRODUCCIÓN**.
Solamente sirve en el escenario en el que estamos
desarrollando localmente nuestra aplicación.

## Variables de entorno

- Linux / Mac
  export FLASK_APP=hola
  export FLASK_DEBUG=True

- Windows
  set FLASK_APP=hola
  set FLASK_DEBUG=True
