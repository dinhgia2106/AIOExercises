def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def approx_cal(x, n):
    approx_sin = 0
    approx_cos = 0
    approx_sinh = 0
    approx_cosh = 0

    for i in range(n):
        approx_sin += (-1) ** i * (x ** (2 * i + 1) / factorial(2 * i + 1))
        approx_cos += (-1) ** i * (x ** (2 * i) / factorial(2 * i))
        approx_sinh += x ** (2 * i + 1) / factorial(2 * i + 1)
        approx_cosh += x ** (2 * i) / factorial(2 * i)

    print(f"Approx_sin = {approx_sin}")
    print(f"Approx_cos = {approx_cos}")
    print(f"Approx_sinh = {approx_sinh}")
    print(f"Approx_cosh = {approx_cosh}")


x = float(input("X = "))
n = int(input("n = "))
approx_cal(x, n)