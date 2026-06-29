#save_config — a Netmiko method that saves the device's current running configuration
# to its startup configuration, so changes survive a reload. Netmiko issues the correct
#  save command for the platform automatically.

from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

load_dotenv()

device = {
    "device_type" : "cisco_xe",
    "host"        : os.getenv("NETMIKO_HOST"),
    "username"    : os.getenv("NETMIKO_USERNAME"),
    "password"    : os.getenv("NETMIKO_PASSWORD"),
}

connection = ConnectHandler(**device)


config_commands = [
    "interface loopback100",
    "description configured-by-netmiko",
]
output = connection.send_config_set(config_commands)
print(output)

output = connection.save_config()
print(output)

connection.disconnect()
