from math import e


def is_number(x):
    try:
        int(x)
        return True
    except ValueError:
        print("x must be an integer")
        return False


def activation_function(x, fname):
    alpha = 0.01

    if fname.lower() == "sigmoid":
        return 1 / (1 + e ** -x)
    elif fname.lower() == "relu":
        return max(0, x)
    elif fname.lower() == "elu":
        return alpha * (e ** x - 1) if x <= 0 else x


def check_activation_function(fname):
    if fname.lower() not in ["sigmoid", "relu", "elu"]:
        return print(f'{fname} is not supported')
    return True


if __name__ == "__main__":
    x = input("x = ")
    if is_number(x):
        x = int(x)
        fname = input("Input activation Function (sigmoid|relu|elu): ")
        if check_activation_function(fname):
            print(activation_function(x, fname))
