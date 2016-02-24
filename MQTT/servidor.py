import paho.mqtt.publish as publish

publish.single("hola/mundo", "echo123", hostname="localhost")
