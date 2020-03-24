class ROT13:
    def __init__(self, alphabet=None):
        self.alpha_offset = 65
        self.alphabet = [chr(i + self.alpha_offset) for i in range(26)] if alphabet is None else alphabet.upper()

    def encode(self, input_text):
        encoded_text = ""
        input_text = input_text.upper().rstrip().lstrip()

        for letter in input_text:
            try:   
                index = self.alphabet.index(letter)
            except ValueError:
                encoded_text += letter
                continue

            new_index = index + 13
            if new_index >= len(self.alphabet):
                new_index -= len(self.alphabet)

            encoded_text += self.alphabet[new_index]

        return encoded_text

    def decode(self, input_text):
        decoded_text = ""
        input_text = input_text.upper().lstrip().rstrip()

        for letter in input_text:
            try:
                index = self.alphabet.index(letter)
            except ValueError:
                decoded_text += letter
                continue

            new_index = index - 13
            if new_index < 0:
                new_index = 26 + new_index

            decoded_text += self.alphabet[new_index]

        return decoded_text

cipher = ROT13()
sprava = cipher.encode('Zacnite s vystahovanim!')
normal = cipher.decode(sprava)
print(normal)