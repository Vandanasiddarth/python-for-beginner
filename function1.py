def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😒",
        ">:o": "😠"
    }

    result = ''
    for word in words:
        result += emojis.get(word, word) + ' '
    return result


message = input(">")
print(emoji_converter(message))

