class Polybious:
    def __init__(self, pridaj=0):
        self.alphabet = [chr(i+97) for i in range(26)]
        self.alphabet.remove('w')
        if pridaj == 1:
            self.alphabet += [str(i) for i in range(0, 10)]
            self.alphabet.append(' ')
        self.len = len(self.alphabet)
        self.can_use = self.alphabet
        self.grid = 5 + pridaj

    def intersection(self, lst1, lst2): 
        lst3 = [value for value in lst2 if value not in lst1] 
        return lst3 

    def repeating_string(self, given_string):
        seen = set()
        ret = []
        for c in given_string:
            if c not in seen and c in self.alphabet:
                seen.add(c)
                ret.append(c)
        return ''.join(ret)

    def create_square(self, key):
        key = self.repeating_string(key)
        key = list(key)
        table = [[],[],[],[],[],[]]

        self.can_use = key + self.intersection(key, self.alphabet)

        for index in range(self.len):
            row = index // self.grid
            table[row].append(self.can_use[index])

        return table

    def encode(self, input_text, key):
        input_text = input_text.lower().lstrip().rstrip().replace('w', 'v')
        key = key.lower().lstrip().rstrip()
        encoded_text = ""
        table = self.create_square(key)

        for letter in input_text:
            for row in range(self.grid):
                for column in range(self.grid):
                    if letter == table[row][column]:
                        encoded_text += str(row+1) + str(column+1) + ' '
        return encoded_text

    def decode(self, input_text, key):
        input_text = input_text.lower().lstrip().rstrip().split(' ')
        key = key.lower().lstrip().rstrip()
        decoded_text = ""
        table = self.create_square(key)

        for pair in input_text:
            row = int(pair[0])-1
            column = int(pair[1])-1
            letter = table[row][column]
            decoded_text += letter

        return decoded_text

cipher = Polybious()
sprava = 'dnes je velmi krasny den na to aby som siel nieco robit von. Moje cislo je 0123456789'
message = cipher.encode(sprava, 'branislavblazek')
print(message)
text = cipher.decode(message, 'branislavblazek')
print(text)

print(cipher.decode('52 42 15 21 51 34 25 24 42 45 11 43 25 21 15 25 43 42 23 12 45 14 25 43 42 24 41 25 15 12 43 14 23 15 14 23', 'tarinka'))