class Mixed_alphabet:
    def __init__(self, alphabet=None):
        self.alphabet = [chr(i + 65) for i in range(26)] if alphabet is None else alphabet.upper()
        self.alphabet = list(self.alphabet)
        self.alpha_len = len(self.alphabet)

    def repeating_string(self, given_string):
        seen = set()
        ret = []
        for c in given_string:
            if c not in seen and c in self.alphabet:
                seen.add(c)
                ret.append(c)
        return ''.join(ret)

    def encode(self, input_text, key):
        #druhy sposob, prvy je nahodny kluc
        key = key.upper().lstrip().rstrip()
        short_key = self.repeating_string(key)
        decoded_text = ""
        input_text = input_text.upper().lstrip().rstrip()

        short_table = self.alphabet.copy()
        for letter in short_key:
            if letter in short_table:
                short_table.remove(letter)

        table = list(short_key) + short_table

        for letter in input_text:
            try:
                index = self.alphabet.index(letter)
            except ValueError:
                decoded_text += letter
                continue

            decoded_text += table[index]

        return decoded_text

    def decode(self, input_text, key):
        key = key.upper().lstrip().rstrip()
        short_key = self.repeating_string(key)
        decoded_text = ""
        input_text = input_text.upper().lstrip().rstrip()

        short_table = self.alphabet.copy()
        for letter in short_key:
            if letter in short_table:
                short_table.remove(letter)

        table = list(short_key) + short_table

        for letter in input_text:
            try:
                index = table.index(letter)
            except ValueError:
                decoded_text += letter
                continue

            decoded_text += self.alphabet[index]

        return decoded_text


cipher = Mixed_alphabet(" .,?!ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
key = '5 minutes'
sprava = cipher.encode('We can also use a key phrase.', key)
print(sprava)
message = cipher.decode('V.5EUG5QO.5GQFT.LO5AG5P!.5C.X5J!LUO.5PHH', key)
print(message)
