import time

print("==== Countdown Timer ====")

seconds = int(input("Enter time in seconds: "))

for i in range(seconds, 0, -1):
    print(f" Time Left: {i} seconds", end="\r")
    time.sleep(1)

print("\n Time's up!")

