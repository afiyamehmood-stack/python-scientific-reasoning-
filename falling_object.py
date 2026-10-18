# Falling Object Calculator
# Calculates the distance an object falls under gravity.
# Assumes the object starts from rest and ignores air resistance.

GRAVITY = 9.81  # metres per second squared

time = float(input("Enter falling time in seconds: "))

if time < 0:
    print("Error: Time cannot be negative.")
else:
    distance = 0.5 * GRAVITY * time ** 2

    print(f"Time: {time} seconds")
    print(f"Distance fallen: {distance:.2f} metres")
