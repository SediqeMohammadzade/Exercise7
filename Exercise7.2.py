def word_count():
    word = input("Enter your word: ")
    counter = len(word.split(" "))
    print("how many word:", counter)

word_count()