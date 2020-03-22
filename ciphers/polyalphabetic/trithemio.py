class Trithemio:
    def __init__(self):
        self.alphabet = [chr(i+97) for i in range(26)]

    def encode(self, input_text):
        input_text = input_text.lower().lstrip().rstrip()
        encoded_text = ""
        dole = 0

        for index, letter in enumerate(input_text):
            if letter in [' ', '.', ',', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                encoded_text += letter
                dole += 1
            elif letter in self.alphabet:
                i = index % 26 - dole
                pozicia = self.alphabet.index(letter)
                abeceda = self.alphabet[i:] + self.alphabet[:i]
                encoded_text += abeceda[pozicia]

        return encoded_text

    def decode(self, input_text):
        input_text = input_text.lower().lstrip().rstrip()
        decoded_text = ""
        dole = 0

        for index, letter in enumerate(input_text):
            if letter in [' ', '.', ',', '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                decoded_text += letter
                dole += 1
            elif letter in self.alphabet:
                i = index % 26 - dole
                abeceda = self.alphabet[i:] + self.alphabet[:i]
                pozicia = abeceda.index(letter)
                decoded_text += self.alphabet[pozicia]

        return decoded_text

cipher = Trithemio()
message = cipher.encode('ahoj velmi krasny svet ako sa mas dnes je krasny den na to aby som siel nieco robity')
print(message)
text = cipher.decode(message)
print(text)

print(cipher.decode('psgoii thl tevgpwb xeaxtykj'))