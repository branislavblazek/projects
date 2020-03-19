class Gronsfeld:
    def __init__(self):
        self.alphabet = [chr(i+97) for i in range(26)]

    def encode(self, input_text, key):
        input_text = input_text.lower().lstrip().rstrip()
        key = str(key)
        key = key.lower().lstrip().rstrip()
        encoded_text = ""
        key_list = key * (len(input_text) // len(key))
        key_list += key[:(len(input_text) % len(key))]
        dole = 0

        for index, letter in enumerate(input_text):
            if letter in [' ', '.', ',', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                encoded_text += letter
                dole += 1
            elif letter in self.alphabet:
                i = index - dole
                posun = int(key_list[i])
                abeceda = self.alphabet[posun:] + self.alphabet[:posun]
                encoded_text += abeceda[self.alphabet.index(letter)]

        return encoded_text

    def decode(self, input_text, key):
        input_text = input_text.lower().lstrip().rstrip()
        key = str(key)
        key = key.lower().lstrip().rstrip()
        decoded_text = ""
        key_list = key * (len(input_text) // len(key))
        key_list += key[:(len(input_text) % len(key))]
        dole = 0

        for index, letter in enumerate(input_text):
            if letter in [' ', '.', ',', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                decoded_text += letter
                dole += 1
            elif letter in self.alphabet:
                i = index - dole
                posun = int(key_list[i])
                abeceda = self.alphabet[posun:] + self.alphabet[:posun]
                decoded_text += self.alphabet[abeceda.index(letter)]

        return decoded_text

cipher = Gronsfeld()
message = cipher.encode('dnes je krasny den aby som nieco robil!', 1)
print(message)
text = cipher.decode(message, 1)
print(text)