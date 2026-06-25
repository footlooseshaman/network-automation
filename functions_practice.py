def check_status(device_name):
    status = device_name + " is reachable"
    return status

result = check_status("Router1")
print(result)


device = {
    "host": "192.168.1.1",
    "username": "admin",
    "password": "cisco123",
    "device_type": "cisco_ios"
}

print(device["host"])
print(device["device_type"])

# Change an existing value
device["password"] = "newpass456"

# Add a brand-new key-value pair
device["location"] = "Mumbai-DC"

print(device["password"])
print(device["location"])
#print(device["model"])

print(device.get("model"))
print(device.get("model", "unknown"))