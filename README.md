# Examen-IoT
Repositorio del parcial 1 de IoT. Andrés Rejón Ancona.

El siguiente repositorio, correspondiente al primer parcial de Internet de las Cosas, consiste en dos códigos diferentes para realizar un medidor de temperatura sencillo usando
Raspberry Pi Pico W y ThingSpeak. 

PRIMERA PARTE: RASPBERRY Y THINGSPEAK.
¿Cómo funciona? Primero y más importante: El archivo main.py. Este es un código de MicroPython que realiza una conexión a WiFi a través de la placa y que eventualmente conecta con nuestro canal de ThingsPeak utilizando una API de escritura. Utilizando el sensor integrado, este medirá la temperatura, conviertiendo el valor ADC a voltaje mediante fórmulas matemáticas. Tras convertir el voltaje a temperatura mediante otra fórmula, este dato será enviado a ThingSpeak y graficado. Las mediciones son realizadas cada 3 minutos.

Para continuar, es necesario tener una cuenta activa en ThingSpeak y un canal abierto (CHANNELS > My Channels > New Channel), este canal debe ser público y también debe contar con un field para poder graficar los resultados de nuestras mediciones.

La instalación es sencilla, basta con conectar nuestro Raspberry a la computadora y abrir nuestro entorno de desarrollo (en mi caso siendo Thonny). Dentro del IDE, copiaremos el código adjunto en este repositorio y modificaremos la siguiente información:

1. SSID (El nombre de la red WIFI).
2. PASSWORD (Clave de la red).
3. API KEY DE THINGSPEAK (La API de escritura de nuestro canal).
4. URL DE THINGSPEAK (La URL de escritura del canal).

Tras modificar estos datos, guardaremos el archivo en nuestra placa (no en computadora) bajo el nombre de "main.py", esto hará que se ejecute automáticamente, incluso sin estar conectado a la computadora.
OJO: Tras haber guardado el código y desconectar la placa de la computadora, es necesario seguirla cargando usando una caja cargadora conectada a la corriente y el mismo cable MicroUSB que usamos para conectar la placa a la PC. Desconectar el Raspberry hará que se detenga la ejecución del código (a mí me pasó, cuidado con eso). 

SEGUNDA PARTE: MATHWORKS.
Tras haber hecho esto, y si nuestro Raspberry está mandando exitosamente las mediciones de temperatura, procedemos a ir a ThingSpeak una vez más, pero en esta ocasión a la sección de análisis de MATLAB (APPS > MATLAB Analysis > New) aquí haremos un nuevo análisis custom y pegaremos el código adjuntado en este repositorio. Sin embargo. es muy importante reemplazar el primer parámetro de la línea 4 (thingSpeakRead), pues aquí el primer parámetro debe ser el ID de nuestro canal a analizar, por lo que tendrás que cambiarlo por tu propio ID. Tras esto, bastará con guardar y ejecutar cada vez que se quiera.  

¿Qué hace este código? Simple y sencillamente mide los últimos 10 datos obtenidos del canal para promediarlos. Si la temperatura promedio superase los 35°, este emite una alerta.

Esto sería todo, muchas gracias por su atención.
