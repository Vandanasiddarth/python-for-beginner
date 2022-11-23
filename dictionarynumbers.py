dict = {
    "1": "One",
    "2": "two",
    "3": "Three",
    "4": "Four"
}

phone = input("Phone:")
output = ''
for i in phone:
    output += dict.get(i,  '!') + ' '
print(output)

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😒"
}

result = ''
for word in words:
    result += emojis.get(word, word) + ' '
print(result)