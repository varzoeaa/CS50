def convert(emoticon):
    emoticon = emoticon.replace(":)", "\U0001F60A")
    emoticon = emoticon.replace(":(", "\U0001F641")
    return emoticon

def main():
    sentence = input("Tell me something with an emoticon! ")
    converted_sentence = convert(sentence)
    print (converted_sentence)

main()
