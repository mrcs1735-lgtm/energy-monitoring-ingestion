import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===== KONFIGURASI dari Environment Variables =====
MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC")
MQTT_USER = os.getenv("MQTT_USER")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")

INFLUX_URL = os.getenv("INFLUX_URL")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
INFLUX_ORG = os.getenv("INFLUX_ORG")
INFLUX_BUCKET = os.getenv("INFLUX_BUCKET")

print("Connecting to InfluxDB...")
influx_client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)
print("✅ InfluxDB connected")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
        print(f"✅ Subscribed to: {MQTT_TOPIC}")
    else:
        print(f"❌ MQTT connection failed, rc={rc}")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload)
        print(f"\n📩 Received: {payload}")

        point = Point("energy_telemetry") \
            .tag("device_id", payload["device_id"]) \
            .field("voltage", float(payload["voltage"])) \
            .field("current", float(payload["current"])) \
            .field("power", float(payload["power"])) \
            .field("energy", float(payload["energy"])) \
            .field("power_factor", float(payload["power_factor"])) \
            .field("frequency", float(payload["frequency"]))

        write_api.write(bucket=INFLUX_BUCKET, record=point)
        print(f"✅ Data written to InfluxDB")

    except Exception as e:
        print(f"❌ Error: {e}")

print("\n🚀 Starting MQTT to InfluxDB Ingestion Service...")
print("=" * 50)

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

print(f"Connecting to MQTT: {MQTT_BROKER}")
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

print("Waiting for messages... (Press Ctrl+C to stop)\n")
mqtt_client.loop_forever()