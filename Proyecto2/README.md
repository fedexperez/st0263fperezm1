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
Para lograrlo debemos de seguir una serie de pasos enfocados al diseño lógico de la arquitectura y posteriormente ponerlo en práctica mediante el uso de Google Cloud Platafform (GCP) o Amazon (AWS) y Docker.

# Instalación

## Despliegue del proyecto

Para la implementación y el despliegue del laboratorio se siguieron los siguientes pasos:

### PARTE 1 - Montar el proyecto en AWS

+ Paso 1: Nos conectamos al curso en AWS educate.
+ Paso 2: Ingresar a la consola “AWS console”.
+ Paso 3: Nos dirigimos a servicios EC2 instances.
+ Paso 4: Presionamos en donde dice “launch instance”.
+ Paso 5: Se selecciona la siguiente Amazon Machine Image: (La que viene por defecto).
+ Paso 6: Seleccionamos t2.micro y luego continuamos.
+ Paso 7: En la tercera perstaña debemos seleccionar un File System (Puede crearlo directamente desde ahí, y si ya tiene uno, usar ese mismo para las instancias que serán utilziadas por wordpress)
+ Paso 8: Presionamos Next o Continuar (dependiendo del idioma) hasta llegar a “configure security groups”.
+ Paso 9: En “security groups” creamos una regla para TCP con el cual abrimos el puerto que deseamos usar.
+ Paso 10: Presionamos en “review and launch”.
+ Paso 11: Presionamos en “launch”.
+ Paso 12: Creamos una nueva “key pair” y le ponemos el nombre que queramos.
+ Paso 13: Descargamos la clave .pem ya mas adelante la necesitaremos.
+ Paso 14: Presionamos en “launch instance”.
+ Paso 15: Nos dirigimos a servicios ec2 Running Instances.
+ Paso 16: Presionamos en la instancia que acabamos de crear y copiamos la DNS que también será necesaria más adelante.

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
+ Paso 2: Instalar recursos - GCP
```
sudo yum install git -y
sudo yum install pip -y
sudo yum install docker -y
sudo yum install docker-compose -y
sudo systemctl enable docker.service
sudo systemctl start docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
pip3 install mysql
```

+ Paso 2: Instalar recursos - AWS
```
sudo yum install git -y
sudo yum install pip -y
sudo amazon-linux-extras install docker -y
sudo usermod -a -G docker ec2-user
sudo systemctl enable docker.service
sudo systemctl start docker
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
pip3 install mysql
```

### PARTE 4 – Descargar los archivos

+ Paso 1: Clone el git
Abra el proyecto en GitHub, y luego copie su ruta para poder clonarlo.
+ Paso 2: Aplique el siguiente comando:
```
sudo git clone <URL PROYECTO>
```
Ejemplo:
```
sudo git clone <https://github.com/usuario/proyecto.git>
```

# PARTE 5 - Ejecución

+ Paso 1: Ya dentro de la instacias que creamos, nos dirigimos al respectivo directorio del laboratorio.
```
cd st0263
cd Proyecto2
```
+ Paso 2: Editar el archivo dorcker-compose de wordpress con el comando "sudo vi docker-compose.yml" .
```
version: '3.1'
services:
  wordpress:
    image: wordpress:5.8.1
    container_name: wordpress
    restart: always
    volumes:
      - wordpress_data:/var/www/html
    environment:
      WORDPRESS_DB_HOST: privateipaddressofdb:3306
      WORDPRESS_DB_NAME: wpdb
      WORDPRESS_DB_USER: user
      WORDPRESS_DB_PASSWORD: password
    ports:
      - 80:80
      - 443:443
volumes:
  wordpress_data: {}
```
+ Paso 3: Ir a la carpeta de wordpress y la carpeta de database para ejecutar el siguiente comando en cada una.
```
sudo docker-compose up -d
```
+ Paso 4: Ver como el programa estará en funcionamiento y poder hacer uso de él.

# PARTE 6 - Configuración de dominio

+ Paso 1: Dirigirnos a freenom e iniciar sesion. Si no tiene una cuenta deberá crearla. (https://my.freenom.com/)

+ Paso 2: Generar el nombre de dominio deseado, deseablemente un dominio que finalice en .ml .

+ Paso 3: En Cloudfare, registrar los nombres de los dominios generados.

+ Paso 5: Crear dos nuevos record, de tipo A con el nombre de nuestro dominio y el valor será la direccion ip publica de nuestro CMS.

+ Paso 6: Dos daran dos nameservers, esos valores los copiaremos uno en uno en los nameservers de nuestro dominio en freenom.

# PARTE 7 - Configuración de Load Balancer HaProxy

+ Paso 1: Generar una instancai en AWS

+ Paso 2
```
sudo su
mkdir -p /opt/haproxy/
vi haproxy.cfg
```


+ Paso 3: En haproxy.cfg escribir lo siguiente:
```
global
        log 127.0.0.1   local0
        log 127.0.0.1   local1 debug
        maxconn   45000 # Total Max Connections.
        daemon
        nbproc      1 # Number of processing cores.
defaults
        timeout server 86400000
        timeout connect 86400000
        timeout client 86400000
        timeout queue   1000s

frontend main
        bind *:80
        default_backend app

# [HTTP Site Configuration]
listen  http_web ipofhaproxyinstance:80
        mode http
        balance roundrobin  # Load Balancing algorithm
        option httpchk
        option forwardfor
        server server1 fperezmpr2.tk weight 1 maxconn 512 check
        server server2 rsaldarrispr2.tk weight 1 maxconn 512 check

```


+ Paso 4: 
```
sudo yum install haproxy
sudo yum install docker
sudo amazon-linux-extras install docker -y
sudo usermod -a -G docker ec2-user
sudo systemctl enable docker.service
sudo systemctl start docker
docker run -d --name haproxy -p 80:80 -v /opt/haproxy:/usr/local/etc/haproxy:ro haproxy:1.7 tail -f /dev/null
```

# Referencias:
A continuación se encuentran las paginas de las cuales se investigó para desarrollar el código.

+ [Firewall GCP](https://cloud.google.com/vpc/docs/using-firewalls#console)
+ [Quickstart: Compose and WordPress](https://docs.docker.com/samples/wordpress/#bring-up-wordpress-in-a-web-browser)
+ [Install Docker Compose](https://docs.docker.com/compose/install/)
+ [HaProxy](https://tecadmin.net/install-and-configure-haproxy-on-centos/)
+ [HaProxy Youtube](https://www.youtube.com/watch?v=77wXzh_Kjv0)
+ [Certificados SSL](https://certbot.eff.org/lets-encrypt/centosrhel7-other)
+ [Freenom](https://my.freenom.com/)
+ [Route 53 AMAZON](https://www.youtube.com/watch?v=cBohHhCN3TM)
+ [Amazon EFS](https://www.youtube.com/watch?v=yKhE2hzlbqA)
