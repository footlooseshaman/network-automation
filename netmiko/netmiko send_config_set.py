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

connection.disconnect()

#send_config_set — a Netmiko method that takes a list of configuration commands, 
#automatically enters the device's global configuration mode, sends each command in order, 
#then exits config mode — returning the session output.
#The two things that make it different from send_command, worth noting:
#It expects a list of commands, not a single string: ["interface loopback100", "description automated"].
#It handles config mode for you — you don't manually type configure terminal
# or end. Netmiko enters config mode, runs the list, and exits automatically.