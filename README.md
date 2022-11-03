LIBRERIA: MI PRIMER PROYECTO

Esta libreria tiene como funcion facilitar la validacion de direcciones fisicas Colombianas 
Tanto urbanas como rurales, todo esto gracias a las grandes funcionalidades de expresiones regulares 
que nos ofrece la libreria "re" de python en donde comparamos las direcciones que nos ingresa el usuario
con diferentes expresiones regulares que hemos creado para poder validar diferentes tipos de direcciones
que pueda llegar a necesitar el usuraio de esta libreria.

para poder usar la libreria es necesario contener un archivo txt llamado "Direcciones.txt" dentro de nuestra carpeta de proyecto, esto con el fin de poder validar mas cantidad de direcciones.

Prerequisitos 

Python 3

Ademas se incluye en la libreria un txt con algunas direcciones de ejemplo

Para instalar la libreria debe hacerlo con el comando: 

- pip install -i https://test.pypi.org/simple/ MiPrimerProyecto==0.0.2

Listo despues de instalarlo solo debemos invocarlo desde nuestro nuevo proyecto con el siguiente comando: 
- from MiPrimerProyecto import runner

Se recuerda que se debe tener un archivo txt en el proyecto llamado "Direcciones.txt" en el cual se introducen las direcciones que se deseen leer
