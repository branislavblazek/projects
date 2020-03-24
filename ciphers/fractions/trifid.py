from pprint import pprint

class Trifid:
    def __init__(self):
        self.alphabet = [chr(i+65) for i in range(26)]
        self.alphabet.append('.')
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

        for zero_point in range(self.len)[::9]:
            usable = self.can_use[zero_point:zero_point+9]
            row = len(usable) // 3
            mini_table = []
            for index in range(row):
                mini_table.append(usable[index*3:index*3+3])
            
            table.append(mini_table)

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
        third_line = []
        encoded_text = ''

        for word in text.split(' '):
            first = []
            second = []
            third = []
            for letter in word:
                can_break = False
                for index_table, mini_table in enumerate(table):
                    for index_row, row in enumerate(mini_table):
                        if letter in row:
                            first.append(index_table)
                            second.append(index_row)
                            third.append(row.index(letter))
                            break
                            can_break = True
                    if can_break:
                        break

            first_line.append(first)
            second_line.append(second)
            third_line.append(third)
            
        for index in range(len(first_line)):
            read = first_line[index] + second_line[index] + third_line[index]
            for index in range(len(read)//3):
                pair = read[index*3:index*3+3]
                encoded_text += table[pair[0]][pair[1]][pair[2]]
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
                for index_table, mini_table in enumerate(table):
                    can_break = False
                    for index_row, row in enumerate(mini_table):
                        if letter in row:
                            word_indexes.append(index_table)
                            word_indexes.append(index_row)
                            word_indexes.append(row.index(letter))
                            can_break = True
                            break
                    if can_break:
                        break
            
            pocet = len(word_indexes) // 3
            for i in range(pocet):
                pair = word_indexes[i::pocet]
                decoded_text += table[pair[0]][pair[1]][pair[2]]
            decoded_text += ' '

        return decoded_text


cipher = Trifid()
message = cipher.encode('novyt ypsif ry', 'qyfbmrxiwsalkveuj.dotzgchpn')
print(message)
text = cipher.decode(message, 'qyfbmrxiwsalkveuj.dotzgchpn', True)
print(text)