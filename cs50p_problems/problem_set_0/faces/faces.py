def main():
    emoji = input()
    converted = convert(emoji)
    print(converted)


def convert(emoji):
    emoji1 = emoji.replace(":)", "🙂")
    emoji2 = emoji1.replace(":(", "🙁")
    return emoji2


main()
