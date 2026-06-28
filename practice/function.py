def connect(host, username):
    return f"Connecting to {host} as {username}"

host = input("host =")
username = input("username =")

print(connect(host, username))
print("\n",connect(host, username))

    