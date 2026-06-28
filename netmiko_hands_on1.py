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

connection = ConnectHandler(**device)
output = connection.send_command("show ip interface brief")
print(output)

connection.disconnect()
