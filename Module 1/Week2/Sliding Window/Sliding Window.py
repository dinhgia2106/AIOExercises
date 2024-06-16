num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3


def max_sliding_window(k):
    output = []
    max_num = min(num_list)
    for i in range(len(num_list)):
        if i <= len(num_list) - 3:
            for n in range(i, k + i):
                if num_list[n] > max_num:
                    max_num = num_list[n]
            output.append(max_num)
    print(output)


if __name__ == "__main__":
    max_sliding_window(k)
