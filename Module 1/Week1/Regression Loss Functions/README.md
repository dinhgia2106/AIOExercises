# Loss Calculation

## Overview

This script calculates loss metrics (MAE, MSE, RMSE) based on randomly generated predictions and targets. It allows the user to specify the number of samples and the type of loss metric to calculate.

## Features

- Generates random predictions and targets.
- Computes Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE).
- Displays the loss for each sample and the final loss.

## Usage

1. **Run the script:**
   ```sh
   Loss_Calculation.py
   ```

2. **Input prompts:**
   - The script will prompt you to enter the number of samples.
   - The script will prompt you to enter the loss name (MAE, MSE, RMSE).

## Example

```sh
Number of samples: 5
Input loss name (MAE, MSE, RMSE): MAE
```

## How It Works

1. **Seeding the random number generator:**
   ```python
   seed(42)
   ```

2. **Getting user input:**
   ```python
   num_samples = int(input("Number of samples: "))
   loss_name = input("Input loss name (MAE, MSE, RMSE): ")
   ```

3. **Loss calculation:**
   ```python
   def loss_cal(n):
       total_loss = 0
       if loss_name.upper() not in ["MAE", "MSE", "RMSE"]:
           print("Invalid loss name. Please input MAE, MSE, or RMSE.")
           return

       for i in range(n):
           pred = uniform(0, 10)
           target = uniform(0, 10)
           
           if loss_name.upper() == "MAE":
               loss = abs(target - pred)
               total_loss += loss
           elif loss_name.upper() == "MSE":
               loss = (target - pred) ** 2
               total_loss += loss
           elif loss_name.upper() == "RMSE":
               loss = (target - pred) ** 2
               total_loss += loss
           
           print(f'Loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}')
       
       if loss_name.upper() == "MAE":
           final_loss = total_loss / n
       elif loss_name.upper() == "MSE":
           final_loss = total_loss / n
       elif loss_name.upper() == "RMSE":
           final_loss = sqrt(total_loss / n)

       print(f'Final {loss_name}: {final_loss}')
   ```

4. **Execution:**
   ```python
   if __name__ == "__main__":
       loss_cal(num_samples)
   ```

## Error Handling

- If the input for the number of samples is not an integer, the script will display an error message and exit.
- If an invalid loss name is provided, the script will display an error message and prompt for a valid input.

## Requirements

- **Python 3.x**
- **Libraries**:
  - **random**: Required for generating random numbers. Specifically, it uses the `uniform` and `seed` functions.
  - **math**: Necessary for mathematical operations. Specifically, it uses the `sqrt` function.

## Author

- Trần Đình Gia - GrazT
