def get_middle(s):
    word_length = len(s)

    characters = s[word_length // 2 - 1:word_length // 2 + 1] if word_length % 2 == 0 \
        else s[word_length // 2]

    return characters
