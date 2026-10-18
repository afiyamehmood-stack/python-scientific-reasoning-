# Python Scientific Reasoning

A beginner Python project that calculates the distance an object falls under gravity and uses automated unit tests to verify the results.

## Physics Formula

The project uses:

**d = ½gt²**

Where:
- `d` = distance fallen in metres
- `g` = gravitational acceleration (9.81 m/s²)
- `t` = time in seconds

## Assumptions and Limitations

- The object starts from rest.
- Air resistance is ignored.
- Gravitational acceleration is treated as constant.
- Time must be non-negative.

## Files

- `falling_object.py` — calculation function and interactive program.
- `test_falling_object.py` — automated tests using Python's built-in `unittest` framework.

## Run the Program

Make sure Python 3 is installed, then run:

```bash
python falling_object.py
```

Enter the falling time in seconds when prompted.

## Run the Tests

Run this command from the project directory:

```bash
python -m unittest test_falling_object.py
```

The tests check:
1. The calculated distance after 2 seconds.
2. The result for zero seconds.
3. Rejection of negative time.

## Example

For a falling time of 2 seconds, the calculated distance is **19.62 metres**.

## Learning Goals

This project demonstrates basic Python functions, input validation, physics calculations, exception handling, and automated unit testing.
