# MCIB_B_G12
Práctica clase 1, desplegar un API con Docker

## Creación de archivo de configuración .env
1. Crear un archivo .env con las siguientes variables\
**#Configuración de la aplicación**\
FLASK_APP=flask_api.py \
FLASK_ENV=development \
FLASK_DEBUG=1 \
**#Configuración del servidor**\
HOST=0.0.0.0\
PORT=5001

## Ejecutar archivo script 'deploy.sh'
Dentro del archivo deploy.sh se encuentran los comandos para crear la imagen y levantar el contenedor.\
![alt text](<Captura de pantalla 2025-08-19 a la(s) 9.33.39 p.m..png>)
1. Ejecutar el siguiente comando para poder crear una imagen de docker y levantar la imagen en un contenedor\
Linux o Mac\
./deploy.sh\
![alt text](<Captura de pantalla 2025-08-19 a la(s) 9.34.41 p.m..png>)
2. Revisar que el contenedor se haya levantado correctamente\
![alt text](<Captura de pantalla 2025-08-19 a la(s) 9.34.59 p.m..png>)\
De igual manera de puede revisar si el contenedor se levantó correctamente con el siguiente comando:\
docker ps -a | grep api-flask\
![alt text](<Captura de pantalla 2025-08-19 a la(s) 9.55.09 p.m..png>)

## Realizar peticiones al API
Se pueden realizar peticiones al API desde la aplicación de POSTMAN o desde cualquier otra aplicación.\
1. Endpoint - Obtener la información de una IP
![alt text](<Captura de pantalla 2025-08-19 a la(s) 9.35.22 p.m..png>)
2. Endpoint - Obtener el factorial de cualquier número
![alt text](<Captura de pantalla 2025-08-19 a la(s) 9.36.02 p.m..png>)
3. Endpoint - Invertir el orden de una cadena de texto
![alt text](<Captura de pantalla 2025-08-19 a la(s) 9.36.29 p.m..png>)\

Podemos revisar que dentro del contenedor se estan realizando las peticiones correspondientes a los endpoints antes mencionados\
![alt text](<Captura de pantalla 2025-08-19 a la(s) 9.36.37 p.m..png>)