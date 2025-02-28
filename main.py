import network
import urequests
import utime
from machine import ADC

# Configuración de WiFi
SSID = "Totalplay-42AB"
PASSWORD = "42AB2D54RV7mqtze"

# Configuración de ThingSpeak
THINGSPEAK_API_KEY = "KKAXD3023Y4HZ8C8"
THINGSPEAK_URL = "https://api.thingspeak.com/update?api_key=KKAXD3023Y4HZ8C8&field1=0"

# Configuración del sensor de temperatura interno
sensor_temp = ADC(4)  # Canal ADC 4 (sensor interno de la RP2040)

# Función para conectar a WiFi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Conectando a Wi-Fi...")
    while not wlan.isconnected():
        utime.sleep(1)
    
    print("Conectado a Wi-Fi:", wlan.ifconfig())

# Función para leer la temperatura del sensor interno
def leer_temperatura():
    valor_adc = sensor_temp.read_u16()  # Leer valor ADC (0-65535)
    voltaje = valor_adc * 3.3 / 65535  # Convertir a voltaje (3.3V ref)
    temperatura = 27 - (voltaje - 0.706) / 0.001721  # Fórmula oficial de la Raspberry Pi Pico
    return round(temperatura, 2)

# Función para enviar datos a ThingSpeak
def enviar_datos(temperatura):
    url = f"{THINGSPEAK_URL}&field1={temperatura}"
    try:
        respuesta = urequests.get(url)  # Hacemos la solicitud GET
        respuesta.close()
    except Exception as e:
        print("Error al enviar datos:", e)

# *Código Principal*
conectar_wifi()  # Conectar a la red WiFi

while True:
    temperatura = leer_temperatura()  # Leer temperatura interna
    print(f"Temperatura actual: {temperatura} °C")
    
    enviar_datos(temperatura)  # Enviar a ThingSpeak
    
    utime.sleep(180)  # Esperar 180 segundos (3 min) antes de la siguiente medición