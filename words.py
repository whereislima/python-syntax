def print_upper_words(words, first_letter):
    """
    print out each word in all uppercase
    only print words that start with h or y
    """

    for word in words:
        if word[0] == "h" or word[0] == "y":
            print(word.upper())



# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "y"})