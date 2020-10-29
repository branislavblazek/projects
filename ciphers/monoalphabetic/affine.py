class Affine:
    def __init__(self, alphabet=None):
        self.alphabet = [chr(i+65) for i in range(26)] if alphabet is None else alphabet.upper()
        self.alpha_len = len(self.alphabet)

    def encode(self, input_text, a, b):
        input_text = input_text.upper()
        encoded_text = ""

        if self.alpha_len % a == 0:
            print('Warning: ' + str(a) + ' and ' + str(self.alpha_len) + ' have at least one common factor and this will cause a problem in decryption!')

        for letter in input_text:
            try:
                index = self.alphabet.index(letter)
            except ValueError:
                encoded_text += letter
                continue

            new_index = (a * index + b ) % self.alpha_len
            encoded_text += self.alphabet[new_index]

        return encoded_text

    def decode(self, input_text, a, b):
        input_text = input_text.upper()
        decoded_text = ""

        if self.alpha_len % a == 0:
            print('Warning: ' + str(a) + ' and ' + str(self.alpha_len) + ' have at least one common factor and this will cause a problem in decryption!')

        #c * a mod self.alpha_len = 1
        #x mod self.alpha_len = 1 
        x = None
        for i in range(0,1000, self.alpha_len):
            if i <= 2:
                continue

            if (i+1) % self.alpha_len == 1:
                x = i + 1
                if x % a == 0:
                    c = x / a
                    break
        else:
            print('cannot find!')

        for letter in input_text:
            try:
                index = self.alphabet.index(letter)
            except ValueError:
                decoded_text += letter
                continue

            new_index = c * (index - b) % self.alpha_len
            decoded_text += self.alphabet[int(new_index)]

        return decoded_text

cipher = Affine( "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
message = cipher.encode('A simple message', 7, 13)
print(message)
normal = cipher.decode('NCDQWTQP FQ CEL NEFRMWLYN FA PTDQCN', 15, 3)
print(normal)


#ak a-cko a dlzka abecedy maju spolocneho delitela okrem 1, sposobi to nepresne desifrovanie
#pre spravne koeficienti 
# - pri abecede s dlzkou 26: a je 12 ktore nemaju spolocneho delitela a b je 26
#   - je to 12 * 26 = 312 moznych klucov
# - ak je dlzka abecedy prirodzene cislo, tak a moze byt 30 a b je 26
#   - tak to je 780 moznych klucov, lepsie!
