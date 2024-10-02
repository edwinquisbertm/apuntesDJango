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
https://docs.djangoproject.com/en/5.0/ref/models/fields/


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

## Conectar Postgres

para esto solo tendremos que modificar de la siguiente manera:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DJANGO_DB_NAME'),
    }
    #'default': env.db('DJANGO_DB_URL') esta es otra forma de enviar los datos de la base de datos
}

debemos recordar crear el archivo .env para almacenar las variables de entorno que no se enviaran al repositorio

para ocultar las credenciales de acceso a la DB necesitaremos importar
import environ

luego tendremos que agregar:
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

con esto referenciaremos a las variables de entorno

# shell en DJango
./manage.py shell
- desde esta interfaz podremos ejecutar instrucciones para django como si estuviera corriendo el proyecto

# Clases
las clases a diferencia de las funciones no retornan ningun elemento por lo que es necesario utilizar as.view para poder llamar a la clase como si fuera una función

revisar documentación:
https://docs.djangoproject.com/en/5.1/topics/class-based-views/

# DJango Templates
Exploraremos los templates en Django y sus funcionalidades avanzadas que los diferencian del HTML estándar. Aprenderemos cómo los templates nos permiten mostrar contenido dinámico en el navegador, validar variables, recorrer listas y aplicar filtros para modificar valores antes de mostrarlos. También veremos cómo reutilizar contenido común mediante el archivo base HTML.

¿Qué son los templates en Django?
Los templates en Django son archivos HTML que incluyen funcionalidades adicionales para mostrar contenido dinámico. A diferencia del HTML puro, los Django templates permiten:

Mostrar variables
Realizar validaciones con if
Recorrer listas con for
¿Cómo se muestran variables en un template?
Para mostrar variables, se encierran en dobles llaves {{ }}. Por ejemplo, para mostrar una variable llamada var del contexto, se usaría:

{{ var }}
¿Qué son y cómo se utilizan los filtros en Django?
Los filtros permiten modificar el valor de una variable antes de mostrarla. Se usan con un pipe | seguido del nombre del filtro. Por ejemplo, para mostrar solo el día y mes de una fecha:

{{ fecha_nacimiento|date:"m/d" }}
Los filtros pueden concatenarse. Por ejemplo, convertir el resultado en minúsculas:

{{ fecha_nacimiento|date:"m/d"|lower }}
¿Qué son los tags en Django y cómo se utilizan?
Los tags agregan funcionalidades adicionales al código HTML. Se abren con {% %} y pueden incluir:

if: para validaciones
for: para recorrer listas
url: para mostrar URLs dinámicas
Algunos tags requieren una etiqueta de cierre. Por ejemplo, if y for:

{% if condition %}
    <!-- contenido -->
{% endif %}
¿Qué es el archivo base HTML en Django?
El archivo base.html permite definir contenido común para ser reutilizado en la aplicación. Se crean bloques que pueden extenderse en otros archivos. Por ejemplo:

<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <div id="content">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
Para reutilizar este contenido:

<!-- new_template.html -->
{% extends "base.html" %}
{% block content %}
    <!-- contenido específico -->
{% endblock %}

# Apuntes Proyecto
{% comment "" %}
        <form class="mt-4">
        <button
          class="block w-full rounded bg-yellow-400 p-4 text-sm font-medium transition hover:scale-105"
        >
          Add to Cart
        </button>
      </form>
{% endcomment %}
      
Este bloque nos permite comentar codigo para que DJango no lo ejecute

## TailWind
 https://www.hyperui.dev/components/marketing/product-cards
 https://tailwindcss.com/docs/container

 - otros:
 https://flowbite.com/
 
- para una mejor manejo podemos utilizar
Crispy Form Tailwind: https://github.com/django-crispy-forms/crispy-tailwind

# Admin de DJango
crear una cuenta de administrador
./manage.py createsuperuser

para agregar elementos al admin debemos modificar el archivo admin.py de la aplicacion

## En caso de que necesitemos consultar rutas estaticas de los archivos almacenados debemos utilizar:
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Unit Testing en DJango
Django tiene sus propios elementos para hacer pruebas y se pueden crear a través de los archivos tests.py
para ejecutar una prueba utilizamos el comando:
./manage.py test
este comando crear una base de datos de prueba temporal en donde ejecuta los Unit Test

## black
este nos permite formatear el codigo para manejar una sintaxis unica en todo el proyecto
- instalamos con
pip install black
- ejecutamos con:
black .

solo se utiliza para el entorno de desarrollo
