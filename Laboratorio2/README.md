# st0263fperezm1

Repositorio para la materia Tópicos especiales en Telemática - ST0263
Universidad EAFIT

# Autor

Federico Pérez Morales
fperezm1@eafit.edu.co
201810008010

# Software

Windows o Linux
Python 3.7 - 3.8 (Fue probado y funcional en estas dos versiones del software)

# Descripcion

El desarrollo del presente laboratorio está enfocado a la aplicación de los conocimientos adquiridos en el curso de telemática, específicamente al diseño, implementación y despliegue de una sala de chat con el uso de RPC, HTTP y los servicios de la nube de AWS.  
Para lograrlo debemos de seguir una serie de pasos enfocados al diseño lógico de la arquitectura y posteriormente ponerlo en práctica mediante el uso de Python y AWS.

La aplicación está compuesta de distintas archivos de los cuales se hablará a continuación: 

+ Se tiene un archivo llamado server.py el cual es el encargado de recibir y enviar los mensajes a los clientes y se les permita enviar mensajes.

+ Se tiene un archivo llamado client.py el cual es el encargado de conectarse con el servidor y asignar un nombre de usuario con el cual identificarse, también de enviar los mensajes al servidor para que los demás clientes puedan verlos.


# Instalación

## Despliegue del proyecto en AWS

Para la implementación y el despliegue se siguieron los siguientes pasos:

### PARTE 1 - Montar el proyecto en AWS

+ Paso 1: Nos conectamos al curso en AWS educate.
+ Paso 2: Ingresar a la consola “AWS console”.
+ Paso 3: Nos dirigimos a servicios EC2  instances.
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
+ Paso 14: Nos dirigimos a servicios ec2  Running Instances.
+ Paso 15: Presionamos en la instancia que acabamos de crear y copiamos la DNS que también será necesaria más adelante.

#### PARTE 2 - Tutorial para Windows para Conexión SSH para conectarnos a la máquina virtual

+ Paso 1: Instalar Putty (<https://www.putty.org/>).
+ Paso 2: Puede buscar en el directorio donde instalo putty, el ejecutable puttygen, y abrirlo o buscarlo en los programas instalados.
+ Paso 3: Dónde dice Type of key to generate, escogemos RSA.
+ Paso 4: Presiona Load. Por defecto, PuTTYgen solo nos muestra los archivos con extension .ppk. Para localizar tu archivo .pem, se escoge la opción para poder ver todos los tipos de archivos. (Escoge su archivo pem   el cual descargó en el paso 12 del tutorial anterior).
+ Paso 5: Si siguió los pasos correctamente la key se generara en formato .ppk.
+ Paso 6: Después de presionar en Aceptar, presione en “save private key” y guárdela. Esta clave la usaremos después para conectarnos con putty al servidor de Amazon. Presione que si al aviso que sale, y luego se guarda la clave con el nombre queramos (se generará un archivo .ppk).
+ Paso 7: Abir putty.
    + Nos dirigmos a Connection  SSH  Auth, y cargamos la clave .ppk que transformó anteriormente.
    + Regresamos a sesión y en donde dice hostname colocamos ec2-user@ (literalmente) y luego la public dns de su instancia. Algo así: ec2-user@ec2-54-196-113-35.compute-1.amazonaws.com
    + Luego en saved session, colocamos un nombre para guardar la configuración (ejemplo: ProyectoTelematica) y luego de presionamos en “Save” para qu e la configuración quede guardada, y la próxima vez, solo sea cargarla.
    + Por ultimo de click en Open, y presionamos que sí en el aviso que sale.
    + Si todo salió bien, deberá ver una terminal

#### PARTE 3 - Instalar librerías en nuestra máquina virtual

+ Paso 1: Ejecutamos el siguiente comando desde SSH (putty) para actualizar el sistema.
sudo yum update -y
+ Paso 2:
sudo yum install git -y
sudo yum install pip
sudo yum pip install grpcio grpcio-tools

#### PARTE 4 – Descargar los archivos

+ Paso 1: clone el git
Abra su proyecto en GitHub, y luego copie su ruta.
+ Paso 2: Luego aplique el siguiente comando:
sudo git clone [URL PROYECTO]
Ejemplo: sudo git clone <https://github.com/usuario/proyecto.git>
+ Paso 3: Nos dirigimos al directorio que se creó y ejecutamos el respectivo archivo.
pythton3 server.py
NOTA: SE DEBE UTILIZAR LA IPv4 PRIVADA DE LA INSTANCIA QUE SE USS COMO SERVER, SE EDITA DESDE LA MAQUINA PRIVADA.
+ Paso OPCIONAL: Si desea hacer cambios en el archivo protocol.proto, despues de hacerlos debe aplicar el siguiente comando 'python -m grpc_tools.protoc --proto_path=.  ./protocol.proto --python_out=. --grpc_python_out=.' y despues verficiar el codigo para corregir lo que se haya cambiado

