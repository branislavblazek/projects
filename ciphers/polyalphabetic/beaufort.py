class Beaufort:
    def __init__(self):
        self.alphabet = [chr(i+65) for i in range(26)]

    def encode(self, input_text, key):
        input_text = input_text.upper().lstrip().rstrip()
        key = key.upper().lstrip().rstrip()
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
                posun = self.alphabet.index(letter)
                abeceda = self.alphabet[posun:] + self.alphabet[:posun]
                encoded_text += self.alphabet[abeceda.index(key_list[i])]

        return encoded_text

    def decode(self, input_text, key):
        decoded_text = self.encode(input_text, key)
        return decoded_text

class Beaufort_smart:
    def __init__(self):
        self.alphabet = [chr(i+97) for i in range(26)]

    def encode(self, input_text, key):
        input_text = input_text.upper().lstrip().rstrip()
        key = key.upper().lstrip().rstrip()
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
                k = self.alphabet.index(key_list[i])
                o = self.alphabet.index(letter)
                s = k - o
                encoded_text += self.alphabet[s]

        return encoded_text

    def decode(self, input_text, key):
        input_text = input_text.upper().lstrip().rstrip()
        key = key.upper().lstrip().rstrip()
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
                k = self.alphabet.index(key_list[i])
                s = self.alphabet.index(letter)
                o = k -s
                decoded_text += self.alphabet[o]

        return decoded_text

cipher = Beaufort()
message = cipher.encode('albatros', 'pavel')
print(message)
text = cipher.decode(message, 'pavel')
print(text)

cipher_smart = Beaufort_smart()
message = cipher_smart.encode('albatros', 'pavel')
print(message)
text = cipher_smart.decode(message, 'pavel')
print(text)

print(cipher.decode('wmrenfkcn vzazkybp lkzjkw txko', 'korona'))