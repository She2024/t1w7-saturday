def count_words(text):
    words = text.split()
    return len(words)
def unique_words(text):
    words = text.lower().split()
    return set(words)


sentence = "Hello, I am a coder and I am cool."