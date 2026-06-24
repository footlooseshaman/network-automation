# access_check.py - decides whether to push config to a device

reachable = input("Is the device reachable? (yes/no): ").lower()
authenticated = input("Did authentication succeed? (yes/no): ").lower()

if reachable == "yes" and authenticated == "yes":
    print("All checks passed - pushing config")
else:
    print("Checks failed - aborting, will not push config")

