# Hello World
## Instalando Flask
Empezamos creando el directorio en el que se alojará nuestra aplicación
```bash
$ mkdir flaskmegatutorial
$ cd flskmegatutorial
```
Creamos un entorno virtual
```bash=
$ virtualenv venv
```
Con el comando anterior se crea un entorno virtual de nombre `venv`. 

Cuiando termine de ejecutarse el comando anterior se crea el directorio `env`. En dichi directorio se almacenarán los archivos del entorno virtual.

Una vez creado, hemos de indicarle a nuestro sistema que queremos activarlos. Para ello ejecutamos:
```bash
$ source venv/bin/activate
(venv) $ _
```
Una vez activado se modifica la sesión del terminal de forma que el interprete de Python que se invoca al ejecutar `python` es la almacenada en el entorno virtual.

Una vez creado y activado el entorno virtual podemos instalar Flask:
```bash
(venv) $ pip install flask
```
## Creando una aplicación "Hello, World"

###### tags: `flask` `flaskmegatutorial` `hello_world.md`