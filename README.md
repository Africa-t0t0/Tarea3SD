# Tarea3SD
Tarea 3 Sistemas Distribuidos. Consiste en 2 bases de datos configuradas de manera master/slave. La base master procesa los INSERT mientras que la base slave maneja los SELECT. Se utiliza NGINX para distribuir entre 3 microservicios las request.

Este tutorial contempla la instalación de nginx desde UBUNTU.

REQUISITOS: nginx, python 3.9, flask, psycopg2, docker.

pasos a seguir.

Clonar el contenido del repositorio.

Realizar la configuración de Nginx: 
    - Dirigirse al lugar de instalaciónd e Nginx, por defecto: cd /etc/nginx/
    - abrir con su editor de texto favorito el archivo nginx.conf, es necesario tener permisos: sudo vim nginx.conf
    - en la sección "http", dirigirse a la última linea y agregar lo siguiente: "include RUTA/DONDE/CLONARON/ELREPO/app.conf"
    - comentar la linea "include /etc/nginx/sites-enabled/*;"
    - hacer reload y restart de nginx: "sudo service nginx reload" y "sudo service nginx restart".
    - ahora nginx está configurado.

Ejecutar el dockercompose:
    - Dirigirse al lugar donde clonaron el repositorio.
    - (Opcional) Modificar las variables de entorno a gusto.
    - Utilizar el siguiente comando: "docker-compose up -d"
    - Ahora las bases de datos fueron creadas en modo master/slave.

Crear tabla products:
    - Es necesario crear la tabla products con filas: id auto incrementable, name varchar, value int.

Dar permisos a la base de datos slave:
    - Por defecto, no se permite realizar consultas a la base de dato slave, es necesario utilizar el comando "GRANT SELECT ON products TO PUBLIC;"
   

  
