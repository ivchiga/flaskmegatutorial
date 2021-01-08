# Hello World
## Instalando Flask
Empezamos creando el directorio en el que se alojará nuestra aplicación
```bash
$ mkdir flaskmegatutorial
$ cd flskmegatutorial
```
Creamos un entorno virtual
```bash
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
En lugar de hacer una configuración básica creramos una un poco más elaborada que servirá de base para aplicaciones más complejas.

La aplicación la crearemos como un *paquete*. En Python, cualquier subdirectorio que incluya un fichero de nombre `__init__.py` es considreado como un paquete y puede ser importado. Al importar un paquete, se ejecuta dicho archivo en el que se definen que símbolos del paquete son accesibles desde el mundo exterior.

Creamos un paquete de nombre `app` que hospedará la aplicación.

```bash
(venv) $ mkdir app
```
El fichero `__init__.py` de `app` contendrá:
```python
from flask import Flask

app = Flask(__name__)

from app import routes
```
El script crea la aplicación como un objeto que es una instancia de la clase `Flask` importada del paquete `Flask`. La variable `__name__` que le pasamos a la clase`Flask` es una variable predefinida de Python que tiene asignado el nombre del módulo que usa.

La aplicación importa el módulo `routes` que todavía no existe.

El módulo `routes` es importado al final del fichero para evitar `imports circulares`, ya que cómo veremos el módulo `routes` necesita importar el módulo `app`.

So what goes in the routes module? The routes are the different URLs that the application implements. In Flask, `handlers` for the application routes are written as `Python functions`, called view functions. View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests a given URL.

Las rutas las definimos en el fichero `app/routes.py`:
```python
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
```

Los decoradores son usados aquí para registrar funciones como llamadas ante ciertos eventos. En este caso, el decorador `@app.route` crea una asociación entre la URL pasada como argumento y la función. En este caso hay dos URLs (/, /index) asociadas a la función.

Para completar nuesta aplicación necesitamos un script de alto nivel que cree una instancia de la aplicación Flask. La creamos en el fichero `microblog.py`
```python
from app import app
```
Nuestra apliación inicial ya está completa. Antes de ejecutarla hemos de decirle a Python como importarla estableciendo el valor de la variable de entorno `FLASK_APP`. Ejecutamos:
```bash=
(venv) $ export FLASK_APP=microblog.py
```
Para iniciar la aplicación usamos el comando:
```python
(venv) $ flask run
 * Serving Flask app "microblog"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Podemos comprobarlo accediendo en el navegador a `http://localhost:5000` o a `http://localhost:5000/index`

Como las variables de entorno se pierden al cerrar el terminal Flask permite desde la versión 1.0 importarlas al ejecutar el comando `flask`. Para usar dicha opción debemos instalar el paquete `python-dotenv`
```python
(venv) $ pip install python-dotenv
```
Y guardar las variables de entorno en un fichero de nombre `.flaskenv` en el directorio raíz del proyecto.
```python
FLASK_APP=microblog.py
```
###### tags: `flask` `flaskmegatutorial` `hello_world.md`