strings = str(input("String: "))


def count_chars(strings):
    char_count = {}

    for char in strings:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    sorted_char_count = dict(
        sorted(char_count.items(), key=lambda item: item[1], reverse=False))

    print(sorted_char_count)


if __name__ == "__main__":
    count_chars(strings)
