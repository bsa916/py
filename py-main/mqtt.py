import json
import random
import time
import paho.mqtt.client as mqtt_client
import requests
from pathlib import Path

# Энергостед
url = "10.71.0.93"
port = 8004

# MQTT
url_broker = "91.229.10.143"
port_broker = 9001
topic = "energo/data"
client_id = f"python-mqtt-{random.randint(0, 1000)}"
username = "daniil"
password = "12345678990"

# Параметры программы
DEBUG = True
DEBUG_FILE = Path("test-json-1.txt")
i = -1

def on_connect(client, userdata, flags, rc, properties=None):
    global i
    i = rc
    if rc == 0:
        print("Подключились")
    else:
        print(f"Неудача, код: {rc}")

client = mqtt_client.Client(
    mqtt_client.CallbackAPIVersion.VERSION2, client_id=client_id
)
client.username_pw_set(username, password)
client.on_connect = on_connect

try:
    print("Попытка подключения к брокеру...")
    client.connect(url_broker, port_broker, keepalive=60)
    print("Подключение к MQTT успешно!")
except Exception as e:
    print(f"Произошла ошибка при подключении к MQTT: {e}")
    # exit()

def get_data():
    if DEBUG:
        if not DEBUG_FILE.exists():
            raise FileNotFoundError(f"Файл для отладки не найден: {DEBUG_FILE}")
        with open(DEBUG_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            return json.loads(content)
    else:
        http_url = f"http://{url}:{port}"
        response = requests.get(http_url, timeout=10)
        response.raise_for_status()
        return json.loads(response.content)

while True:
    try:
        data = get_data()
        print("Полученные данные:", data)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    except json.JSONDecodeError as e:
        print(f"Не удалось распарсить JSON: {e}")

    time.sleep(5)

#

