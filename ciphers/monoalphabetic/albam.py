class Albam():
    def __init__(self, alphabet=None):
        self.alphabet = [chr(i+65) for i in range(26)] if alphabet is None else alphabet.upper()
        self.table = self.alphabet[len(self.alphabet)//2:] + self.alphabet[:len(self.alphabet)//2]
        print(self.table)

    def encode(self, text):
        input_text = text.upper()

        decoded_text = ""

        for letter in input_text:
            try:
                letter_index = self.alphabet.index(letter)
            except ValueError:
                decoded_text += letter
                continue

            decoded_text += self.table[letter_index]
        
        return decoded_text

    def decode(self, text):
        input_text = text.upper()

        decoded_text = ""

        for letter in input_text:
            try:
                letter_index = self.alphabet.index(letter)
            except ValueError:
                decoded_text += letter
                continue

            decoded_text += self.table[letter_index]

        return decoded_text


cipher = Albam("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
sprava = cipher.encode('Oko albatros')
print(sprava)
normal = cipher.decode(sprava)
print(normal)