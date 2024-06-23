import streamlit as st


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f. readlines()
    words = sorted(set([line . strip(). lower() for line in lines]))
    return words


vocabs = load_vocab(
    file_path="Module 1/Week4/source/source/data/vocab.txt")


def levenshtein_distance(source, target):
    if len(source) < len(target):
        return levenshtein_distance(target, source)

    if len(target) == 0:
        return len(source)

    previous_row = range(len(target) + 1)
    for i, c1 in enumerate(source):
        current_row = [i + 1]
        for j, c2 in enumerate(target):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):

        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        # sorted by distance
        sorted_distences = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(sorted_distences)


if __name__ == "__main__":
    main()
