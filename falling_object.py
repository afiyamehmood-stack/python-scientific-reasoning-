GRAVITY = 9.81  # metres per second squared


def calculate_distance(time):
    """Calculate distance fallen from rest, ignoring air resistance."""
    if time < 0:
        raise ValueError("Time cannot be negative.")
    return 0.5 * GRAVITY * time ** 2


def main():
    time = float(input("Enter falling time in seconds: "))

    try:
        distance = calculate_distance(time)
        print(f"Time: {time} seconds")
        print(f"Distance fallen: {distance:.2f} metres")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
