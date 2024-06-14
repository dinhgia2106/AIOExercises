# MD_nRE Calculation

## Overview

This Python script calculates a metric named `MD_nRE`(potentially related to Mean Absolute Normalized Residual Error). It prompts the user for input and computes the `MD_nRE` value.

## Features

- Calculates the MD_nRE metric for multiple samples.
- Provides clear instructions for running the script and entering user input.

## Usage

1. **Run the script:**

   ```sh
   MD_nRE_Calculation.py
   ```

2. **Input prompts:**

    ```sh
    - Number of samples: Specify the number of calculations you want to perform (integer value).
    - y (value of y): The actual or true value of the variable being measured.
    - y_hat (value of yˆ): The predicted or estimated value of the variable being measured.
    - n (nth root): The power to which both `y` and `y_hat` will be raised before calculating the difference.
    - p (power of loss function): The exponent to which the difference between `y` and `y_hat` will be raised.
    ```

## Example

```sh
Number of samples: 2

y (sample 1): 0.5
y_hat (sample 1): 0.4
n (sample 1): 2
p (sample 1): 3

0.0004160171531466459

y (sample 2): ... (enter values for sample 2)

... (intermediate result for sample 2)

Final MD_nRE: ... (average MD_nRE across all samples)
```

## How It Works

User Input: The script prompts you for the number of samples.
Looping: It iterates through the specified number of samples.
Within Each Iteration:
- Prompts for values of `y`, `y_hat`, `n`, and `p`.
- Calculates the `MD_nRE` for the current sample.
- Prints the intermediate `MD_nRE` result.
Final Result: After processing all samples, it calculates and prints the final `MD_nRE` (average of intermediate results).


## Requirements

- **Python 3.x**

## Author

- Trần Đình Gia - GrazT