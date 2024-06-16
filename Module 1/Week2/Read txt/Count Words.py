def count_words(split_document):
    word_count = {}
    for char in split_document:
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1
    
    sorted_alpha = dict(
        sorted(word_count.items(), key=lambda item: item[0], reverse=False))

    print(sorted_alpha)


file_path = "Module 1/Week2/Read txt/P1_data.txt"

with open(file_path, 'r') as f:
    document = f.read()

split_document = document.lower().split()

count_words(split_document)
