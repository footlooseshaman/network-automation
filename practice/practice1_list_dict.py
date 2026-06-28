device_names = ["Router1", "Router2", "Router3"]

for device_name in device_names:
    print(f"Name of device is : {device_name}")





device = {
    "host": "192.168.1.1",
    "vendor": "Cisco",
    "model": "Catalyst 9300"
}

for key, value in device.items():
    print(f"Device {key}: {value}")


