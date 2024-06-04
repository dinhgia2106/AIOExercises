# Activation Functions

This "Activation_Functions" script implements various activation functions commonly used in neural networks. The activation functions included are Sigmoid, ReLU, and ELU.

## Functions

### `is_number(x)`

Checks if the input `x` is a number.

- **Parameters:**
  - `x`: The input value to check.
- **Returns:** 
  - `True` if `x` is an integer, otherwise `False`.

### `activation_function(x, fname)`

Applies the specified activation function to the input `x`.

- **Parameters:**
  - `x`: The input value.
  - `fname`: The name of the activation function. Supported values are `"sigmoid"`, `"relu"`, and `"elu"`.
- **Returns:** 
  - The result of the activation function.

### `check_activation_function(fname)`

Checks if the provided activation function name is supported.

- **Parameters:**
  - `fname`: The name of the activation function.
- **Returns:** 
  - `True` if the activation function is supported, otherwise prints an error message.

## Usage

1. Run the script.
2. Input a value for `x` when prompted.
3. Input the name of the activation function (`sigmoid`, `relu`, or `elu`) when prompted.
4. The script will output the result of the specified activation function applied to `x`.

## Example

```sh
$ python Activation\ Functions.py
x = 2
Input activation Function (sigmoid|relu|elu): relu
2
```

In this example, the ReLU activation function is applied to the input value `2`, resulting in `2`.

## Requirements

- Python 3.x

## Author

- Trần Đình Gia - GrazT
