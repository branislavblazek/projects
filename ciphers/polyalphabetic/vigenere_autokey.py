class Vigenere_autokey:
    def __init__(self):
        self.alphabet = [chr(i+65) for i in range(26)]

    def encode(self, input_text, key):
        input_text = input_text.upper().lstrip().rstrip()
        key = key.upper().lstrip().rstrip()
        encoded_text = ""
        raw_text = input_text.replace(' ', '')
        key_list = key + raw_text
        key_list = key_list[:len(input_text)]
        dole = 0

        for index, letter in enumerate(input_text):
            if letter in [' ', '.', ',', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                encoded_text += letter
                dole += 1
            elif letter in self.alphabet:
                i = index - dole
                posun = self.alphabet.index(key_list[i])
                abeceda = self.alphabet[posun:] + self.alphabet[:posun]
                encoded_text += abeceda[self.alphabet.index(letter)]

        return encoded_text

    def decode(self, input_text, key):
        input_text = input_text.upper().lstrip().rstrip()
        key = key.upper().lstrip().rstrip()
        decoded_text = ""
        raw_text = input_text.replace(' ', '')
        key_list = key + raw_text
        key_list = key_list[:len(input_text)]
        dole = 0

        for index, letter in enumerate(input_text):
            if letter in [' ', '.', ',', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                decoded_text += letter
                dole += 1
            elif letter in self.alphabet:
                i = index - dole
                posun = self.alphabet.index(key_list[i])
                abeceda = self.alphabet[posun:] + self.alphabet[:posun]
                decoded_text += self.alphabet[abeceda.index(letter)]
                key += self.alphabet[abeceda.index(letter)]
                key_list = key + raw_text
                key_list = key_list[:len(input_text)]

        return decoded_text

cipher = Vigenere_autokey()
message = cipher.encode('meet me at the corner!', 'king')
print(message)
text = cipher.decode(message, 'king')
print(text)