message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
abd = "abcdefghijklmnopqrstuvwxyz"
decoded_message = []
for letter in message:
    if letter not in abd:
        decoded_message.append(letter)
        continue
    pos = abd.find(letter)
    real = pos + 10
    if real > len(abd) - 1:
        real = real - len(abd)
    decoded_message.append(abd[real])
print("".join(decoded_message))

#New message 
new_message = "i love this cryptography game!"
encoded_message = []
for letter in new_message:
    if letter not in abd:
        encoded_message.append(letter)
        continue
    pos = abd.find(letter)
    real = pos - 10
    if real < 0:
        real = real + len(abd)
    encoded_message.append(abd[real])
print("".join(encoded_message))

#Function for decoding
def decode(message, shift):
    decoded_message = []
    for letter in message:
        if letter not in abd:
            decoded_message.append(letter)
            continue
        pos = abd.find(letter)
        real = pos + shift
        if real > len(abd) - 1:
            real = real - len(abd)
        decoded_message.append(abd[real])
    return "".join(decoded_message)

print(decode("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))
print(decode("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))

#Function for encoding
def encode(message, shift):
    messageToLowerCase = message.lower()
    encoded_message = []
    for letter in messageToLowerCase:
        if letter not in abd:
            encoded_message.append(letter)
            continue
        pos = abd.find(letter)
        real = pos - shift
        if real < 0:
            real = real + len(abd)
        encoded_message.append(abd[real])
    return "".join(encoded_message)

#Force Brute decoding
def forceBrute(message):
    for i in range(1, 26):
        print(decode(message, i))

# forceBrute("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")
        
#The Vigenère Cipher
message2 = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
keyword = "friends"
# Pass original message to message with keyword
keyword_phrase = []
index = 0
for letter in message2:
    if letter not in abd:
        keyword_phrase += letter
        continue
    keyword_phrase.append(keyword[index])
    if index < len(keyword) - 1:
        index += 1
    else:
        index = 0
print("".join(keyword_phrase))
# Decoding the message
decoded_message2 = []
for i in range(len(message2)):
    if message2[i] not in abd:
        decoded_message2.append(message2[i])
        continue
    pos1 = abd.find(message2[i])
    pos2 = abd.find(keyword_phrase[i])
    real = pos2 + pos1
    if real > len(abd) - 1:
        real = real - len(abd)
    decoded_message2.append(abd[real])
print("".join(decoded_message2))

#Function for decoding Vigenère Cipher
def decodeVigenere(message, keyword):
    keyword_phrase = []
    index = 0
    for letter in message:
        if letter not in abd:
            keyword_phrase += letter
            continue
        keyword_phrase.append(keyword[index])
        if index < len(keyword) - 1:
            index += 1
        else:
            index = 0
    decoded_message = []
    for i in range(len(message)):
        if message[i] not in abd:
            decoded_message.append(message[i])
            continue
        pos1 = abd.find(message[i])
        pos2 = abd.find(keyword_phrase[i])
        real = pos2 + pos1
        if real > len(abd) - 1:
            real = real - len(abd)
        decoded_message.append(abd[real])
    return "".join(decoded_message)

print(decodeVigenere("aiwfeyq ayc adcsvke!", "cat"))
#Function for encoding Vigenère Cipher
def encodeVigenere(message, keyword):
    keyword_phrase = []
    index = 0
    for letter in message:
        if letter not in abd:
            keyword_phrase += letter
            continue
        keyword_phrase.append(keyword[index])
        if index < len(keyword) - 1:
            index += 1
        else:
            index = 0
    encoded_message = []
    for i in range(len(message)):
        if message[i] not in abd:
            encoded_message.append(message[i])
            continue
        pos1 = abd.find(message[i])
        pos2 = abd.find(keyword_phrase[i])
        real = pos1 - pos2
        if real < 0:
            real = real + len(abd)
        encoded_message.append(abd[real])
    return "".join(encoded_message)
print(encodeVigenere("i love you!", "cat"))
print(decodeVigenere("g lvte fmu!", "cat"))