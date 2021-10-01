# Proyecto 1

Carpeta del Proyecto 1 para la materia Tópicos especiales en Telemática - ST0263
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
+ Base de datos PostgreSQL

# Descripcion

El desarrollo del presente proyecto está enfocado a la aplicación de los conocimientos adquiridos, específicamente al diseño, implementación y despliegue de un Sistema de Almacenamiento y Recuperación Distribuida de datos (SARDD)
Para lograrlo debemos de seguir una serie de pasos enfocados al diseño lógico de la arquitectura y posteriormente ponerlo en práctica mediante el uso de Python y AWS.

# Instalación

## Despliegue del proyecto en AWS

Para la implementación y el despliegue del laboratorio se siguieron los siguientes pasos:

### PARTE 1 - Montar el proyecto en AWS

+ Paso 1: Nos conectamos al curso en AWS educate.
+ Paso 2: Ingresar a la consola “AWS console”.
+ Paso 3: Nos dirigimos a servicios EC2 instances.
+ Paso 4: Presionamos en donde dice “launch instance”.
+ Paso 5: Se selecciona la siguiente Amazon Machine Image: (La que viene por defecto).
+ Paso 6: Seleccionamos t2.micro y luego continuamos.
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
+ Paso 4: Presiona Load. Por defecto, PuTTYgen solo nos muestra los archivos con extension .ppk. Para localizar tu archivo .pem, se escoge la opción para poder ver todos los tipos de archivos. (Escoge su archivo pem   el cual descargó en el paso 12 del tutorial anterior).
+ Paso 5: Si siguió los pasos correctamente la key se generara en formato .ppk.
+ Paso 6: Después de presionar en Aceptar, presione en “save private key” y guárdela. Esta clave la usaremos después para conectarnos con putty al servidor de Amazon. Presione que si al aviso que sale, y luego se guarda la clave con el nombre queramos (se generará un archivo .ppk).
+ Paso 7: Abir putty.
    + Nos dirigmos a Connection, SSH, Auth, y cargamos la clave .ppk que transformó anteriormente.
    + Regresamos a sesión y en donde dice hostname colocamos ``` ec2-user@"public dns de su instancia" ```. (sin los ")
    EJEMPLO:
    ```
    $ ec2-user@ec2-54-196-113-35.compute-1.amazonaws.com
    ```
    + Luego en saved session, colocamos un nombre para guardar la configuración (ejemplo: ProyectoTelematica) y luego de presionamos en “Save” para qu e la configuración quede guardada, y la próxima vez, solo sea cargarla.
    + Por ultimo de click en Open, y presionamos que sí en el aviso que sale.
    + Si todo salió bien, deberá ver una terminal

### PARTE 3 - Crear base de Datos PostgreSQL en Amazon RDS

+ [Base de datos](https://docs.aws.amazon.com/es_es/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html)
+ Se debe recordar de poner el puerto 5432 abierto para poder ejecutar el programa en su totalidad.

### PARTE 4 - Instalar librerías en nuestra máquina virtual

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
