from random import uniform, seed
from math import sqrt

seed(42)

try:
    num_samples = int(input("Number of samples: "))
except ValueError:
    print("Number of samples must be an integer number")
    exit(1)

loss_name = input("Input loss name (MAE, MSE, RMSE): ")

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

if __name__ == "__main__":
    loss_cal(num_samples)