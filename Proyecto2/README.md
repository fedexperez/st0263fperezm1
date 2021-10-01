# Proyecto 2

Carpeta del Proyecto 2 para la materia Tópicos especiales en Telemática - ST0263
Universidad EAFIT

# Autores

+ Federico Pérez Morales
+ fperezm1@eafit.edu.co
+ 201810008010

+ Ricardo Saldarriaga Serna
+ rsaldarris@eafit.edu.co
+ 201810038010

# Pre-requisitos

+ Sistema operativo Windows o Linux
+ Tener instalado Python 3.7 o Python 3.8 (Fue probado y es funcional en estas dos versiones del software)

# Descripcion

El desarrollo del presente proyecto está enfocado a la aplicación de los conocimientos adquiridos, específicamente al diseño, implementación y despliegue de una aplicación open source LAMP de comunidad que represente un sistema de información del tipo Sistema de Gestión de Contenidos (CMS), en esté caso Wordpress.
Para lograrlo debemos de seguir una serie de pasos enfocados al diseño lógico de la arquitectura y posteriormente ponerlo en práctica mediante el uso de Google Cloud Platafform (GCP) y Docker.

# Instalación

## Despliegue del proyecto en GCP

Para la implementación y el despliegue del laboratorio se siguieron los siguientes pasos:

### PARTE 1 - Obtener clave para VM del proyecto

+ Paso 1: Nos conectamos a la plataforma de GCP.
+ Paso 2: Ingresamos al proyecto generado.
+ Paso 3: Nos dirigimos al menu de navegación al apartado de PROCESAMIENTO -> Compute Engine -> Configuración
+ Paso 4: Presionamos en donde dice “Metadatos”.
+ Paso 5: Se selecciona el proyecto y continuamos.
+ Paso 6: Seleccionamos CLaves SSH.
+ Paso 7: Presionamos Next o Continuar (dependiendo del idioma) hasta llegar a “configure security groups”.
+ Paso 8: En “security groups” creamos una regla para TCP con el cual abrimos el puerto que deseamos usar.
+ Paso 9: Presionamos en “review and launch”.
+ Paso 10: Presionamos en “launch”.
+ Paso 11: Creamos una nueva “key pair” y le ponemos el nombre que queramos.
+ Paso 12: Descargamos la clave .pem ya mas adelante la necesitaremos.
+ Paso 13: Presionamos en “launch instance”.
+ Paso 14: Nos dirigimos a servicios ec2 Running Instances.
+ Paso 15: Presionamos en la instancia que acabamos de crear y copiamos la DNS que también será necesaria más adelante.

### PARTE 2 - Tutorial para Windows con el fin de estabalecer Conexión SSH y conectarnos a la máquina virtual

+ Paso 1: Instalar Putty (<https://www.putty.org/>).
+ Paso 2: Puede buscar en el directorio donde instalo putty, el ejecutable puttygen, y abrirlo o buscarlo en los programas instalados.
+ Paso 3: Dónde dice Type of key to generate, escogemos RSA.
+ Paso 4: Presiona Generate.
+ Paso 5: Si siguió los pasos correctamente la key se generara y debera de darle un nombre si lo desea.
+ Paso 6: Debe copiar la Public Key y añadirla como un nuevo elemento en las claves SSH de su proyecto.
+ Paso 7: Después de presionar en Aceptar, presione en “save private key” y guárdela. Esta clave la usaremos después para conectarnos con putty al servidor de Google. Presione que si al aviso que sale, y luego se guarda la clave con el nombre queramos (se generará un archivo .ppk).
+ Paso 8: Abir putty.
    + Nos dirigmos a Connection, SSH, Auth, y cargamos la clave .ppk que transformó anteriormente.
    + Regresamos a sesión y en donde dice hostname colocamos la IP externa de nuestra maquina virtual.
    + Luego en saved session, colocamos un nombre para guardar la configuración (ejemplo: ProyectoTelematica) y luego de presionamos en “Save” para que la configuración quede guardada, y la próxima vez, solo sea cargarla.
    + Por ultimo de click en Open, y presionamos que sí en el aviso que sale.
    + Si todo salió bien, deberá ver una terminal y debera poner el nombre de la key que se le puso anteriormente para poder hacer el login.

### PARTE 3 - Instalar librerías en nuestra máquina virtual

+ Paso 1: Ejecutamos el siguiente comando desde SSH (putty) para actualizar el sistema.
```
sudo yum update
```
+ Paso 2: Instalar recursos
```
sudo yum install git -y
sudo yum install pip -y
sudo yum install docker -y
pip3 install cassandra-driver
pip3 install pandas
pip3 install prettytable
pip3 install environs
pip3 install psycopg2-binary
```

### PARTE 4 – Descargar los archivos

+ Paso 1: Clone el git
Abra el proyecto en GitHub, y luego copie su ruta para poder clonarlo.
+ Paso 2: Aplique el siguiente comando:
```
$ sudo git clone <URL PROYECTO>
```
Ejemplo:
```
$ sudo git clone <https://github.com/usuario/proyecto.git>
```

# Ejecución

+ Paso 1: Ya dentro de la instacias que creamos, nos dirigimos al respectivo directorio del laboratorio.
```
$ cd "carpeta"
```
+ Paso 2: Descargar o crear el archivo .env
+ Paso 3: Cuando se tenga el archivo .env con los datos respectivos, ejecutamos el archivo main.py
```
$ pythton3 main.py
```
+ Paso 4: Ver como el programa estará en funcionamiento y poder hacer uso de él.

# Referencias:
A continuación se encuentran las paginas de las cuales se investigó para desarrollar el código.

+ [Base de datos](https://docs.aws.amazon.com/es_es/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html)
+ [PostgreSQL youtube](https://www.youtube.com/watch?v=t_Q5NTtYbx4)
+ [Python CRUD](https://cosasdedevs.com/posts/como-crear-un-crud-en-python-parte-1-estructura-y-clase/)
+ [Python Dictionaries](https://www.studytonight.com/python/dictionaries-in-python)
+ [Validar entrada](https://codingornot.com/08-python-validar-entradas-ejemplos)
