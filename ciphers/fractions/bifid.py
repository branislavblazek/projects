from pprint import pprint

class Bifid:
    def __init__(self):
        self.alphabet = [chr(i+65) for i in range(26)]
        self.alphabet += [str(i) for i in range(0, 10)]
        self.len = len(self.alphabet)

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
        table = []

        self.can_use = key + self.intersection(key, self.alphabet)

        for index in range(self.len):
            row = index // 6
            if len(table) <= row:
                table.append([])
            table[row].append(self.can_use[index])

        return table

    def encode(self, input_text, password, more_secure=False):
        input_text = input_text.upper().lstrip().rstrip()
        password = password.upper().lstrip().rstrip()
        text = input_text
        if more_secure:
            text = text.replace(' ', '')
            text = [text[i:i+5] for i in range(0,len(text), 5)]
            text = ' '.join(text)

        table = self.create_square(password)

        first_line = []
        second_line = []
        encoded_text = ''

        for word in text.split(' '):
            first = []
            second = []
            for letter in word:
                for index_row, row in enumerate(table):
                    if letter in row:
                        first.append(index_row)
                        second.append(row.index(letter))
                        break

            first_line.append(first)
            second_line.append(second)

        for index in range(len(first_line)):
            read = first_line[index] + second_line[index]
            for index in range(len(read)//2):
                pair = read[index*2:index*2+2]
                encoded_text += table[pair[0]][pair[1]]
            encoded_text += ' '

        return encoded_text

    def decode(self, input_text, password, more_secure=False):
        input_text = input_text.upper().lstrip().rstrip()
        password = password.upper().lstrip().rstrip()
        text = input_text
        if more_secure:
            text = text.replace(' ', '')
            text = [text[i:i+5] for i in range(0,len(text), 5)]
            text = ' '.join(text)

        table = self.create_square(password)
        
        decoded_text = ''

        for word in text.split(' '):
            word_indexes = []
            for index, letter in enumerate(word):
                for index_row, row in enumerate(table):
                    if letter in row:
                        word_indexes.append(index_row)
                        word_indexes.append(row.index(letter))
                        break

            half_0, half_1 = word_indexes[:len(word_indexes)//2], word_indexes[len(word_indexes)//2:]
            for index in range(len(half_0)):
                decoded_text += table[half_0[index]][half_1[index]]
            decoded_text += ' '

        return decoded_text


cipher = Bifid()
message = cipher.encode('novy typ sifry na specialne ucely 3.ho oddielu', 'albatros')
print(message)
text = cipher.decode(message, 'albatros')
print(text)