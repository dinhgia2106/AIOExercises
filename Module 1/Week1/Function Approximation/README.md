# Function Approximation

This Python script calculates the approximate values of sine, cosine, hyperbolic sine, and hyperbolic cosine functions using their Taylor series expansions.

## Description

The script defines two functions:
1. `factorial(n)`: Calculates the factorial of a given number `n`.
2. `approx_cal(x, n)`: Calculates the approximate values of `sin(x)`, `cos(x)`, `sinh(x)`, and `cosh(x)` using `n` terms of their respective Taylor series expansions.

The script then takes input from the user for `x` (the point at which the functions are to be approximated) and `n` (the number of terms to use in the series expansions), and prints the approximations.

## Usage

To run the script, you need to have Python installed on your system. Follow these steps:

1. Clone or download the repository.
2. Navigate to the directory containing the script.
3. Run the script using Python:

    ```sh
    python Funcion_Approximation.py
    ```

4. Enter the value of `x` when prompted.
5. Enter the value of `n` when prompted.

The script will then print the approximate values of `sin(x)`, `cos(x)`, `sinh(x)`, and `cosh(x)`.

## Example

```sh
$ python Funcion_Approximation.py
X = 1.0
n = 10
Approx_sin = 0.8414709848078965
Approx_cos = 0.5403023058681398
Approx_sinh = 1.1752011936438014
Approx_cosh = 1.5430806348152437
```

## Requirements

- **Python 3.x**

## Author

- Trần Đình Gia - GrazT