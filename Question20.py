def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

# Example usage
sentence = "Hello, how are you?"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)  # Output: "you? are how Hello,"
