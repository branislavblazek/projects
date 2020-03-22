class Caesar:
    def __init__(self, alphabet=None):
        self.alphabet = [chr(i + 97) for i in range(26)] if alphabet is None else alphabet.lower()
        self.alpha_len = len(self.alphabet)

    def encode(self, input_text, offset):
        sign = -1 if offset < 0 else 1
        offset = abs(offset) % self.alpha_len * sign

        encoded_text = ""
        input_text = input_text.lower().rstrip().lstrip()

        for letter in input_text:
            try:   
                index = self.alphabet.index(letter)
            except ValueError:
                encoded_text += letter
                continue

            new_index = index + offset
            if new_index >= self.alpha_len:
                new_index -= self.alpha_len
            elif new_index < 0:
                new_index = self.alpha_len - index - 1

            encoded_text += self.alphabet[new_index]

        return encoded_text

    def decode(self, input_text, offset):
        sign = -1 if offset < 0 else 1
        offset = abs(offset) % self.alpha_len * sign

        decoded_text = ""
        input_text = input_text.lower().lstrip().rstrip()

        for letter in input_text:
            try:
                index = self.alphabet.index(letter)
            except ValueError:
                decoded_text += letter
                continue

            new_index = index - offset
            if new_index < 0:
                new_index = self.alpha_len + new_index
            elif new_index >= self.alpha_len:
                new_index -= self.alpha_len

            decoded_text += self.alphabet[new_index]

        return decoded_text

cipher = Caesar()
text = """Gavin Relly (1926 in Cape Town, South Africa – 10 January 1999 in Hermanus, South Africa) was a South African businessman and former chairman of Anglo American. His grandfather was Sir Walter Stanford, who argued strongly but unsuccessfully for enfranchisement for Native Peoples regardless of race or colour at the National Convention of 1909, which led to the Union of South Africa.[1]
Relly was educated at Diocesan College and Trinity College, Oxford before serving in Italy during the Second World War. He became the private secretary of Harry Oppenheimer in 1949.
He became chairman of Anglo American in 1982. He led a group of South African businessmen who met with the banned African National Congress in Zambia in 1985. He was succeeded by Julian Ogilvie Thompson in 1990."""

sprava = cipher.encode(text, 18)
normal = cipher.decode(sprava, 18)
print(sprava)
print(normal)

print(cipher.decode('mlgulw rg kwnwjfwb kljsfq', 18))