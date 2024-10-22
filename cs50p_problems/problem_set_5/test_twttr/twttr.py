def main():
    # Get user input
    word = input("Input: ").strip()
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    consoants_word = ""
    # Remove vowels
    for short_word in word:
        if not short_word.lower() in vowels:
            consoants_word += short_word

    return consoants_word

if __name__ == "__main__":
    main()
