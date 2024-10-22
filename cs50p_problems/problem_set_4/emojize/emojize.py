import emoji

string = input("Input: ")
output = emoji.emojize(string, language='alias')

print("Output: ", output)
