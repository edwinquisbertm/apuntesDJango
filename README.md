# apuntesDJango

# django-admin
django-admin --help
//este comando nos permite ver las opciones del framework

django-admin startproject my_first_project .
//con esto se inicia el proyecto y el punto al final evita que se cree una carpeta extra

# documentacion
https://www.djangoproject.com/
https://docs.djangoproject.com/en/5.1/
https://docs.python.org/3/tutorial/venv.html

# correr el proyecto
python manage.py runserver

# estructura del framework
-Model: gestiona la base de datos
-View: gestiona los controladores que interactuan con el modelo y posteriormente con el template,
-Template: el template permite definir la parte grafica del proyecto con el que el usuario interactua.

# manage.py
python manage.py --help
//con este comando podremos ver las opciones de configuración que tenemos.

# para comenzar a definir los modulos que tendra el proyecto tendremos que trabajar con aplicaciones
para crear una aplicacion deberemos utilizar el comando
python manage.py startapp name

# en esta aplicacion tendremos definidos el model, vista
Obs: se debe enlazar la aplicacion creada en el archivo settings.py en INSTALLED_APPS

- Ahora dentro la app debemos crear la carpeta "template" y dentro un directorio con le nombre de la aplicacion para gestionar las vistas

# DJango utiliza ORM para la gestion de BD
La “M” en el patrón MVC se refiere al Modelo, que es crucial para manejar datos de la base de datos en Django. En lugar de utilizar listas con datos estáticos en las vistas, ahora trabajaremos con datos provenientes del modelo, aprovechando el ORM de Django.

- ¿Qué es el ORM en Django?
El ORM (Object-Relational Mapping) en Django nos permite definir clases de Python que se relacionan directamente con las tablas de la base de datos. De esta forma, evitamos escribir sentencias SQL, ya que todo se maneja mediante Python.

- ¿Cómo se define una clase de modelo en Django?
Para definir un modelo, creamos una clase en el archivo models.py. Cada clase de modelo se corresponde con una tabla en la base de datos. Por ejemplo, si definimos la clase Car, esta se convertirá en una tabla con el nombre Car en la base de datos.

- ¿Qué son las migraciones en Django?
Las migraciones son un sistema que Django usa para aplicar y revertir cambios en la base de datos. Cuando creamos o modificamos un modelo, generamos migraciones que se pueden aplicar para crear o actualizar tablas en la base de datos.

- Aplicar una migración
Creamos la clase Car con un atributo title.
Ejecutamos la migración hacia adelante para crear la tabla Car en la base de datos.
Si agregamos un campo year a la clase Car, otra migración aplicará este cambio a la tabla.

- Revertir una migración
Si es necesario, podemos revertir una migración para volver al estado anterior de la tabla.
Por ejemplo, al revertir la migración del campo year, la tabla Car quedará como antes de agregar dicho campo.
¿Cómo permite Django ser independiente del motor de base de datos?
Django ORM es compatible con varios motores de base de datos. En este curso, utilizaremos SQLite para ejemplos iniciales y PostgreSQL para el proyecto final.

# Base de Datos
para inicializar las tablas de la BD de DJango debemos utilizar
./manage.py migrate
./manage.py makemigrations
- // makemigrations nos permite estruturar el ORM para luego se aplique con migrate en la BD
- //si no definimos el id, este sera creado por DJango a través de DJango
- por ultimo debemos volver a colocar el comando
./manage.py migrate

- para configurar otras BD debemos ingresar a settings.py y modificar el apartado DATABASES

## Documentacion BD
https://www.sqlite.org/docs.html
https://docs.djangoproject.com/en/5.0/ref/django-admin/#dbshell
https://docs.djangoproject.com/en/5.0/ref/settings/#databases

## para verificar la DB
debemos colocar
./manage.py dbshell

## Apuntes manejo de la BD
¿Cómo se agrega un nuevo campo a una tabla en Django?
Para agregar un nuevo campo a una tabla existente, necesitas modificar la clase del modelo correspondiente. Por ejemplo, si deseas añadir el campo “año” a la clase Carro, lo haces así:

Añade el campo como un TextField con un MaxLength de 4, ya que solo necesitas almacenar valores como 2022, 2023, etc.
class Carro(models.Model):
    ...
    año = models.TextField(max_length=4, null=True)
¿Qué pasos se siguen después de modificar el modelo?
Después de agregar el nuevo campo al modelo, sigue estos pasos:

Guardar los cambios en el archivo del modelo: No olvides guardar el archivo después de realizar modificaciones.
Crear nuevas migraciones: Ejecuta el comando python manage.py makemigrations. Si no detecta cambios, verifica si guardaste el archivo.
Aplicar las migraciones: Ejecuta python manage.py migrate. Este comando actualiza la base de datos con la nueva estructura.
¿Cómo se soluciona el error de campo no nulo?
Si intentas crear un campo no nulo en una tabla que ya contiene datos, Django te pedirá resolver cómo manejar los registros existentes. Puedes:

Proveer un valor por defecto.
Permitir valores nulos.
En este ejemplo, se permite que el campo “año” sea nulo (null=True), para evitar problemas con registros anteriores.

¿Cómo se utiliza el ORM de Django para interactuar con los datos?
Una vez aplicado el nuevo campo, puedes usar el ORM de Django para interactuar con la base de datos. Usamos el comando python manage.py shell para acceder al shell interactivo de Django.

Ejemplo de cómo crear un nuevo registro:
Importar el modelo:
from my_first_app.models import Carro
Crear una instancia de Carro:
nuevo_carro = Carro(titulo='BMW', año='2023')
Guardar la instancia en la base de datos:
nuevo_carro.save()
¿Cómo mejorar la visualización de los objetos en el shell?
Define el método __str__ en tu modelo para que la representación textual del objeto sea más clara:

class Carro(models.Model):
    ...
    def __str__(self):
        return f"{self.titulo} - {self.año}"
¿Cómo agregar un nuevo atributo y practicar?
Añadir un nuevo atributo, como el color del carro, sigue los mismos pasos:

Modifica la clase del modelo para incluir el nuevo campo.
Guarda el archivo.
Ejecuta los comandos makemigrations y migrate.
Utiliza el shell para crear y guardar nuevos registros con el atributo color.

# shell en DJango
./manage.py shell
- desde esta interfaz podremos ejecutar instrucciones para django como si estuviera corriendo el proyecto