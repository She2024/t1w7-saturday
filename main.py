from text_processing import count_words, unique_words, count_characters, count_unique_characters, reverse_string

import text_processing as tp #will allow you to change the name to a more managable short name for the file you add this to only

from tp import count_words as cw

# Test string
test_string = "Hello World hello"

# Using word_count module
print("Word Count:", count_words(test_string))
print("Unique words:", unique_words(test_string))

# Using char_count module
print("Character Count:", count_characters(test_string))
print("Unique Character Count:", count_unique_characters(test_string))

# Using reverse module
print("Reversed string:", reverse_string(test_string))