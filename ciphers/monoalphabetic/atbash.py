class Atbash():
    def __init__(self, alphabet=None):
        self.alphabet = [chr(i+65) for i in range(26)] if alphabet is None else alphabet.upper()

    def encode(self, text):
        input_text = text.upper()

        decoded_text = ""

        for letter in input_text:
            try:
                letter_index = self.alphabet.index(letter)
            except ValueError:
                decoded_text += letter
                continue

            new_index = len(self.alphabet) - letter_index
            decoded_text += self.alphabet[new_index - 1]
        
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

            new_index = len(self.alphabet) - letter_index
            decoded_text += self.alphabet[new_index - 1]

        return decoded_text


cipher = Atbash("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
sprava = cipher.encode('We are discovered!')
print(sprava)
normal = cipher.decode('854VS5 Q25L 9YY 5R79U5')
print(normal)