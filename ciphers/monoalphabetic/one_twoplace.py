import random

class One_two():
    def __init__(self):
        self.alphabet = [chr(i+97) for i in range(26)]
        self.alphabet.append(' ')
        self.alphabet.append('.')
        self.len = len(self.alphabet)
        self.row = [i for i in range(10)]
        self.row_len = 7
        self.column_len = 3
        self.column = []

        while len(self.column) != self.column_len:
            remove = random.randint(1, len(self.row)-1)
            self.column.append(self.row[remove])
            del self.row[remove]

        self.column = [0, 2, 3, 5, 7, 8, 9]
        self.row = [0,6,1,4]

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
        table = [[],[],[],[]]

        self.can_use = key + self.intersection(key, self.alphabet)

        for index in range(28):
            row = index // 7
            table[row].append(self.can_use[index])

        return table

    def encode(self, input_text, key):
        input_text = input_text.lower().lstrip().rstrip()
        key = key.lower().lstrip().rstrip()
        encoded_text = ""
        table = self.create_square(key)
        for letter in input_text:
            for row in range(4):
                for column in range(7):
                    if letter == table[row][column]:
                        row_x = self.row[row]
                        column_x = self.column[column] 

                        position = str(row_x) + str(column_x) + ' '
                        encoded_text += position

        return encoded_text

    def decode(self, input_text, key):
        input_text = input_text.lower().lstrip().rstrip().split(' ')
        key = key.lower().lstrip().rstrip()
        decoded_text = ""
        table = self.create_square(key)

        for pair in input_text:
            row = self.row.index(int(pair[0]))
            column = self.column.index(int(pair[1]))
            letter = table[row][column]
            decoded_text += letter

        return decoded_text

cipher = One_two()
sprava = 'ahoj tuw'
message = cipher.encode(sprava, 'branislavblazek')
print(message)
text = cipher.decode(message, 'branislavblazek')
print(text)