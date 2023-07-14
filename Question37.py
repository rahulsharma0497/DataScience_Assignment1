def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Example usage
sentence = "Hello, how are you?"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)  # Output: "you? are how Hello,"
