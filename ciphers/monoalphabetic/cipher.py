class Cipher():
    def __init__(self, alphabet=None):
        self.alphabet = [chr(i+97) for i in range(26)] if alphabet is None else alphabet.lower()
        self.table = self.alphabet[len(self.alphabet)//2:] + self.alphabet[:len(self.alphabet)//2]

    def encode(self, input_text):
        input_text = input_text.lower()

        decoded_text = ""

        for letter in input_text:
            try:
                letter_index = self.alphabet.index(letter)
            except ValueError:
                decoded_text += letter
                continue

            decoded_text += self.table[letter_index]
        
        return decoded_text

class Atbam(Cipher):
    def __init__(self, alphabet=None):
        super().__init__()
        print(self.alphabet)

cipher = Atbam()