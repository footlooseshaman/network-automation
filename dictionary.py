
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

print("--- Device details ---")
for key, value in device.items():
    print(key, "=", value)




inventory = [
    {"host": "192.168.1.1", "device_type": "cisco_ios"},
    {"host": "192.168.1.2", "device_type": "cisco_ios"},
    {"host": "192.168.1.3", "device_type": "cisco_nxos"}
]

for device in inventory:
    print("Connecting to", device["host"], "-", device["device_type"])



# Returns None (No error raised!)
print(device.get("email")) 
