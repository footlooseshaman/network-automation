# link_check.py - classifies a link based on ping latency

latency = int(input("Enter ping latency in ms: "))

if latency < 20:
    print("Excellent link")

elif latency < 50:
    print("Good link")

elif latency < 100:
    print("Acceptable link")

else:
    print("Poor link - investigate")