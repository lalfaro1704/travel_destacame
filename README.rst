Travel destacame
================

Una agencia de buses necesita una plataforma para gestionar sus viajes. El sistema debe permitir que se ingresen diversos trayectos. Cada trayecto tendrá varios buses asignados a distintos horarios. Cada bus tendrá un solo chofer y varios pasajeros asignados a sus asientos. Todos los buses tienen la misma capacidad de 10 pasajeros sentados. Los asientos son enumerados y se reservan para cada pasajero. El sistema debe soportar el ingreso de pasajeros a un trayecto y horario en particular, ademas de permitir la asignación de choferes a sus respectivos buses.

Modelo de datos
Escriba a continuación las tablas que utilizaría para resolver este problema con los campos y llaves de éstas. Intente hacer el sistema lo más robusto posible, pero sin incluir datos adicionales a los que se plantean acá.

Backend
Si usted estuviera resolviendo el problema de la agencia de buses implementando una aplicación web que incluya las siguientes funcionalidades:

CRUD pasajeros, choferes, trayectos, buses.
Listar a los trayectos junto a su promedio de pasajeros.
Filtrar a todos los buses de un trayecto con más del 0% de su capacidad vendida.
Para la implementación hay que utilizar el Django y su ORM.


Pre-requisitos 📋
=================

* Python 3:

* Pip: ::

	Mac:
	----
		$ brew install pip
		$ sudo pip install --upgrade pip

	Debian:
	-------
		$ sudo apt-get install python-pip
		$ sudo pip install --upgrade pip

* Virtualenv: ::

	Mac:
		$ brew install virtualenv

	Debian:
		$ sudo apt-get virtualenv

Instalación 🔧
==============

Entorno virtual con la versión de python 3.6: ::

	$ virtualenv -p python3.6 .venv

-Levantamos el entorno virtual:-
```
$ source .venv/bin/activate
```

## Variables de entorno y variables globales ⚙️
-Mac:_
```
$ source .envs/.local/.django; export $(grep -v '^#' .envs/.local/.django | xargs -0)
```

-Debian:_
```
$ source .envs/.local/.django; export $(grep -v '^#' .env/local.sh | xargs -d '\n')
```

## Deployment 📦

-Instalamos las dependencias del proyecto:-
```
$ pip install -r requirements/local.txt
```

_Base de datos_
_Mac:_
```
$ createdb travel
```

_Debian:_
```
sudo su postgres -c "createdb travel"
```

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autor ✒️

* **Luis Alfaro** - *Test destacame.cl* - [lalfaro1704](https://github.com/lalfaro1704)

## Licencia 📄

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

Este proyecto está bajo :Licencia: MIT

## Gratitud 🎁

* Gracias a destacame.cl por darme la oportunidad 🍺 🤓
