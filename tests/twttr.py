def main():
    word = input("Enter a word to remove the vowels (e.g., Twitter becomes Twttr): ")
    print(twttr(word))


def twttr(word):
    new_word = word.translate(str.maketrans('', '', 'aeiouAEIOU'))
    return new_word

if __name__ == "__main__":
    main()