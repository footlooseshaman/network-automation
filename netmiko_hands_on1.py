from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

load_dotenv()

device = {
    "device_type" : "cisco_xe",
    "host" : os.getenv("NETMIKO_HOST"),
    "username" : os.getenv("NETMIKO_USERNAME"),
    "password" : os.getenv("NETMIKO_PASSWORD"),
}

commands = [
    "show ip interface brief",
    "show version",
    "show ip route",
]

connection = ConnectHandler(**device)

for command in commands:
    print(f"\n=== OUTPUT OF: {command} ====")
    output = connection.send_command(command)
    print(output)


connection.disconnect()
