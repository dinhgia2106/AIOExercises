def MD_nRE(m):
    total = 0
    result = 0
    for i in range(m):
        y = float(input("y= "))
        y_hat = float(input("y_hat= "))
        n = int(input("n= "))
        p = int(input("p= "))
        result += (y ** (1 / n) - y_hat ** (1 / n)) ** p
        total += result
        print(result)
    print(f"Final MD_nRE: {total / m}")

m = int(input("Number of samples: "))

if __name__ == "__main__":
    MD_nRE(m)