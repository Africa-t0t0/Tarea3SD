FROM nginx:stable
COPY ./app.conf /etc/nginx/
COPY ./nginx.conf /etc/nginx/nginx.conf

# COPY C:/Users/jrami/Desktop/Tarea3SD/nginx.conf /etc/nginx/nginx.conf
# COPY C:/Users/jrami/Desktop/Tarea3SD/app.conf /etc/nginx/