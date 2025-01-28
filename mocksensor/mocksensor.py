import time
import json
import random
import os

def generate_random_temperature(sensor_data):
    sensor_data["timestamp"] = time.time()
    current_temp = sensor_data["temperature"]
    difference = random.uniform(0, 0.5)
    add_or_subtract = random.randint(0, 1)

    if add_or_subtract and current_temp < 35:
        sensor_data["temperature"] += difference
    elif current_temp > 10:
        sensor_data["temperature"] -= difference

def main():
    sensor_data = {
        "device_id": "3F5A7C2D",
        "client_id": "A9E1B47F",
        "sensor_type": "temperature",
        "temperature": 25,
        "timestamp": time.time()
    }

    output_dir = "/tmp"
    output_file_path = os.path.join(output_dir, "output_mock_sensor.json")

    # Crea el directorio si no existe
    os.makedirs(output_dir, exist_ok=True)

    try:
        while True:
            generate_random_temperature(sensor_data)
            with open(output_file_path, 'w') as output_file:
                json.dump(sensor_data, output_file, indent=4)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nDeteniendo el generador de datos del sensor...")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == '__main__':
    main()
