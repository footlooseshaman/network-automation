def check_status(device_name):
    status = device_name + " is reachable"
    return status

result = check_status("Router1")
print(result)