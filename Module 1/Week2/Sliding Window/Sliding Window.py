num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3


def max_sliding_window(k):
    max_num = []
    for i in range(len(num_list)):
        if i <= len(num_list) - k:
            max_num.append(max(num_list[i:k + i]))

    print(max_num)


if __name__ == "__main__":
    max_sliding_window(k)
