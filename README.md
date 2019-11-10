# Here be dragons

## Prerequisites

```shell
apt-get install mosquitto mosquitto-clients
```

## Run

Mosquitto MQTT server:
```shell
sudo systemctl start mosquitto
```

Web server:
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python led_dragoon.py
```

## Test command

```shell
mosquitto_pub -d -t /home/esp1/set -m '{"effect": "St Paddy", "state": "ON"}'
```
