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


Instalación 🔧
==============

* Python 3: ::

	* Mac:
		brew install python

	* Debian:
		cd /tmp/
		sudo apt-get install python3-dev libffi-dev libssl-dev zlib1g-dev
		wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
		tar xvf Python-3.6.0.tgz
		cd Python-3.6.0
		./configure --enable-optimizations
		make -j8
		sudo make altinstall
		python3.6

* Pip: ::

	* Mac:
		$ brew install pip
		$ sudo pip install --upgrade pip

	* Debian:
		$ sudo apt-get install python-pip
		$ sudo pip install --upgrade pip

* Virtualenv: ::

	* Mac:
		$ brew install virtualenv

	* Debian:
		$ sudo apt-get virtualenv

	* Entorno virtual con la versión de python 3.6:
		$ virtualenv -p python3.6 .venv
		$ source .venv/bin/activate

Variables de entorno y variables globales ⚙️
============================================

* Mac: ::

	$ source .envs/.local/.django; export $(grep -v '^#' .envs/.local/.django | xargs -0)

* Debian: ::

	$ source .envs/.local/.django; export $(grep -v '^#' .env/local.sh | xargs -d '\n')

Deployment 📦
=============

* Base de datos ::

	* Mac:
		$ createdb travel

	* Debian:
		$ sudo su postgres -c "createdb travel"

	$ ./manage.py migrate

* dependencias del proyecto: ::

	$ pip install -r requirements/local.txt

* superusuario y token de acceso: ::

	$ ./manage.py createsuperuser
		Username:
		Email address:
		Password:
		Password (again):

	$ ./manage.py drf_create_token <USERNAME_CREADO>

* Datos iniciales de la base de datos: ::

	$ ./manage.py loaddata travel_destacame/users/fixtures/*.json
	$ ./manage.py loaddata travel_destacame/travel/fixtures/*.json

* runserver: ::

	$ ./manage.py runserver

Versionado 📌
=============

* Git: ::

	* https://github.com/lalfaro1704/travel_destacame.git

Autor ✒️
========

* **Luis Alfaro** - *Test destacame.cl* - [lalfaro1704](https://github.com/lalfaro1704)

Licencia 📄
===========

:Licencia: MIT

Agradecimiento 🎁
=================

* Gracias a destacame.cl por darme la oportunidad 🍺 🤓
