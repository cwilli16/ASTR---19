import math
import numpy as np

def main():
    # Generate 1000 x values between 0 and 2
    x_values = np.linspace(0, 2, 1000)

    # Calculate sin(x) for each x value
    sin_x_values = [math.sin(x) for x in x_values]

    # Print the header of the table
    print(f"{'x':<15} {'sin(x)':<15}")
    print(f"{'':-<30}")

    # Print the table entries
    for x, sin_x in zip(x_values, sin_x_values):
        print(f"{x:<15.6f} {sin_x:<15.6f}")

if __name__ == "__main__":
    main()