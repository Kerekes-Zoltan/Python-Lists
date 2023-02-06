def long_words(n, word_lst):
    return [word for word in word_lst if len(word) > n]

words = ["Hello", "World", "this", "is", "a", "test"]
long_words_list = long_words(6, words)

print("List modified ", long_words_list)