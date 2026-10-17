import json
import random
import time
import paho.mqtt.client as mqtt_client
import requests  # Ошибка: добавили импорт

url = "10.71.0.93"
port = 8004
topic = "energo/data"
client_id = f"python-mqtt-{random.randint(0, 1000)}"
username = "Stepan"
password = "Borisov"

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
#
try:
    print("Попытка подключения к брокеру...")
    client.connect(url, port, keepalive=60)
except Exception as e:
    print(f"Произошла ошибка при подключении к MQTT: {e}")

while True:
    try:
        http_url = f"http://{url}:8004"

        response = requests.get(http_url, timeout=10)
        response.raise_for_status()
        data = json.loads(response.content)
        print("Полученные данные:", data)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    except json.JSONDecodeError as e:
        print(
            f"Не удалось распарсить JSON: {e}, сырой ответ: {response.text[:200]}"
        )

    time.sleep(5)

#

