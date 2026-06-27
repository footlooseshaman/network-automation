device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": 'cisco123',
}


devices = [
    {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "cisco123",
},
{
    "device_type": "cisco_ios",
    "host": "192.168.1.2",
    "username": "admin",
    "password": "cisco123",
},
{
    "device_type": "cisco_ios",
    "host":"192.168.1.3",
    "username": "admin",
    "password": "cisco123",
}
]

for device in devices:
    print(device["host"])
    print(device["device_type"])
