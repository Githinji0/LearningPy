message = input("enter message: ")

words = message.split(' ')#splitting the message

emojiMapping = {
    "sad": "😪",
    "happy": "😄",
    "shocked": "☹"

}
output = ' '
for word in words:
    output+= emojiMapping.get(word, word)

print(output)
    