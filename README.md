# Tarea 3 Sistemas Distribuidos.

Este tutorial contempla la instalación de nginx desde UBUNTU.

# PREREQUISITOS
```
python 3.9
flask
psycopg2
docker.
```
#REQUISITOS: 
## Instalar Nginx.
```
sudo apt install nginx
```

# Pasos a seguir.

## Clonar el contenido del repositorio.

### Realizar la configuración de Nginx: 
```
    - Dirigirse al lugar de instalaciónd e Nginx, por defecto: cd /etc/nginx/
    - abrir con su editor de texto favorito el archivo nginx.conf, es necesario tener permisos: sudo vim nginx.conf
    - en la sección "http", dirigirse a la última linea y agregar lo siguiente: "include RUTA/DONDE/CLONARON/ELREPO/app.conf"
    - comentar la linea "include /etc/nginx/sites-enabled/*;"
    - hacer reload y restart de nginx: "sudo service nginx reload" y "sudo service nginx restart".
    - ahora nginx está configurado.
```
### Ejecutar el dockercompose:
```
    - Dirigirse al lugar donde clonaron el repositorio.
    - (Opcional) Modificar las variables de entorno a gusto.
    - Utilizar el siguiente comando: "docker-compose up -d"
    - Ahora las bases de datos fueron creadas en modo master/slave.
```
### Crear tabla products:
```
    - Es necesario crear la tabla products con filas: id auto incrementable, name varchar, value int.
```
### Dar permisos a la base de datos slave:
```
    - Por defecto, no se permite realizar consultas a la base de dato slave, es necesario utilizar el comando "GRANT SELECT ON products TO PUBLIC;"
 ```
 
### Correr aplicación:
```
    - Una vez todo este configurado, se debe ejecutar app.py, app2.py y app3.py
    - A través de postman, ingresar productos mediante /addproduct.
    - Para obtener todos los productos con nombre similar a la búsqueda, utilizar /getproducts.
```
 ### Comandos para probar en terminal:
 ```
    post: curl -X POST -F 'name=pantalla' -F 'value=43532234' http://localhost:8080/addproduct/
    get: curl -X GET http://localhost:8080/getproducts/pantalla
```
  
