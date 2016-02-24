import paho.mqtt.publish as publish

publish.single("hola/mundo", "Esto es una prueba", hostname="localhost")
