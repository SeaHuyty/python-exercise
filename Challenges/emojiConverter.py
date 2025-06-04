# Exercise: Write a program that convert symbols to emoji.
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "🙂",
    ":(": "😭",
    "><": "🥹",
    ":'(": "🥲"
}
sentence = ""
for word in words:
    sentence += emojis.get(word, word) + " "
    # We use the second 'word' in get just to put back the same word if we ain't have it.
print(sentence)