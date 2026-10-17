import json
import random
import time
import paho.mqtt.client as mqtt_client

url = "10.71.0.93"  
port = 1883  
topic = "energo/data"
client_id = f"python-mqtt-{random.randint(0, 1000)}"


username = "Stepan"
password = "Borisov"

rc = -1

def on_connect(client, userdata, flags, rc, properties=None):
    global rc 
    if rc==0:
        print("подключились")
    else:
        print("неудача")    

client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, client_id=client_id)
client.username_pw_set(username, password)

client.on_connect = on_connect


try:
    print("Попытка подключения к брокеру...")
    client.connect(url, port, keepalive=60)
    client.loop_start()
    
    while True:
        print("все окей")
        
        time.sleep(5) 
except Exception as e:
    print(f"Произошла ошибка: {e}")
            
    #дальше с нейронкой делал

while True:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # выбросит ошибку, если статус не 2xx

        data = json.loads(response.content)
        print("Полученные данные:", data)

        # Тут можно добавить свою логику обработки data

    except requests.exceptions.RequestException as e:
        # Сюда попадают ошибки сети, таймауты, 4xx/5xx (из-за raise_for_status)
        print(f"Ошибка запроса: {e}")

    except json.JSONDecodeError as e:
        # Если сервер вернул не JSON
        print(f"Не удалось распарсить JSON: {e}, сырой ответ: {response.text[:200]}")

    # Пауза, чтобы не «заспамить» сервер запросами
    time.sleep(5)