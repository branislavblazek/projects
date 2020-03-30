from pprint import pprint

class Polybious:
    def __init__(self):
        self.alphabet = [chr(i+65) for i in range(26)]
        self.alphabet.remove('W')
        self.len = len(self.alphabet)
        self.can_use = self.alphabet
        self.grid = 5

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
        table = [[],[],[],[],[]]

        self.can_use = key + self.intersection(key, self.alphabet)

        for index in range(self.len):
            row = index // self.grid
            table[row].append(self.can_use[index])

        return table

    def encode(self, input_text, key):
        input_text = input_text.upper().lstrip().rstrip().replace('W', 'V')
        key = key.upper().lstrip().rstrip()
        encoded_text = ""
        self.table = self.create_square(key)
        xx = 'ADFGX'
        for letter in input_text:
            for row in range(self.grid):
                for column in range(self.grid):
                    if letter == self.table[row][column]:
                        encoded_text += xx[row] + xx[column]
        return encoded_text

    def decode(self, input_text, key):
        input_text = input_text.upper().lstrip().rstrip()
        key = key.upper().lstrip().rstrip()
        decoded_text = ""
        self.table = self.create_square(key)
        xx = 'ADFGX'
        
        for pair in range(len(input_text)//2):
            letters = input_text[2*pair:2*pair+2]
            row = xx.index(letters[0])
            column = xx.index(letters[1])
            letter = self.table[row][column]
            decoded_text += letter

        return decoded_text

class Simple:
    def __init__(self):
        self.alphabet = [chr(i+65) for i in range(26)]

    def find_order(self, lst):
        indexes = []
        order = []

        for letter in lst:
            indexes.append(self.alphabet.index(letter))
            order.append(9999)

        for i, letter in enumerate(indexes):
            #zober hodnotu a jeho index
            minimum = min(indexes)
            index_of_min = indexes.index(minimum)
            #nastav aby nebol najmensi a pridaj do poradia
            indexes[index_of_min] = 9999
            order[index_of_min] = i

        return order

    def encode(self, input_text, key):
        input_text = input_text.upper().lstrip().rstrip()
        text = [letter for letter in input_text if letter in self.alphabet]
        key = key.upper().lstrip().rstrip()
        #len povolene znaky
        key = [letter for letter in key if letter in self.alphabet]
        #najdi opakovanie
        perm_key = []
        for index, letter in enumerate(key):
            if index != 0:
                if key[index-1] != letter:
                    perm_key.append(letter)
            else:
                perm_key.append(letter)

        perm_key = self.find_order(perm_key)
        #vytvor tabulku
        table = []
        for index, letter in enumerate(text):
            row = index // len(perm_key)
            #skontroluj ci je row v table
            if len(table) <= row:
                table.append([])
            
            table[row].append(letter)

        encoded_text = ""

        #prejdi perm_key, ziskavaj stlpce
        for index in perm_key:
            minimum = min(perm_key)
            index_of_min = perm_key.index(minimum)
            perm_key[index_of_min] = 9999
            for row in table:
                try:
                    encoded_text += row[index_of_min]
                except IndexError:
                    pass

        #rozdel po piatich
        encoded_text = [encoded_text[i:i+5] for i in range(0,len(encoded_text), 5)]
        encoded_text = ' '.join(encoded_text)

        return encoded_text
    
    def decode(self, input_text, key):
        input_text = input_text.upper().lstrip().rstrip()
        text = [letter for letter in input_text if letter in self.alphabet]
        key = key.upper().lstrip().rstrip()
        #len povolene znaky
        key = [letter for letter in key if letter in self.alphabet]
        #najdi opakovanie
        perm_key = []
        for index, letter in enumerate(key):
            if index != 0:
                if key[index-1] != letter:
                    perm_key.append(letter)
            else:
                perm_key.append(letter)

        perm_key = self.find_order(perm_key)
        #vytvor tabulku
        pocet_row = {}
        for index in range(len(perm_key)):
            dlzka = len(text) // len(perm_key)
            if index < len(text) % len(perm_key):
                dlzka += 1
            pocet_row[perm_key[index]] = dlzka

        xx = [item[1] for item in pocet_row.items()]
        max_row = max(xx)
        pocet_row = {k: v for k, v in sorted(pocet_row.items(), key=lambda item: item[0])}

        table = [[[] for _ in range(len(perm_key))] for _ in range(max_row)]
        columns = []

        for item in pocet_row.items():
            value = item[1]
            columns.append(text[:value])
            del text[:value]

        #prejdi perm_key, ziskavaj stlpce
        for index in perm_key:
            minimum = min(perm_key)
            index_of_min = perm_key.index(minimum)
            perm_key[index_of_min] = 9999
            for index, letter_to_row in enumerate(columns[minimum]):
                table[index][index_of_min] = letter_to_row

        decoded_text = ""    
        for row in table:
            for letter in row:
                if letter in self.alphabet:
                    decoded_text += letter 

        return decoded_text

class Adfgx:
    def __init__(self):
        self.alphabet = [chr(i+65) for i in range(26)]
        self.polybious = Polybious()
        self.simple = Simple()

    def encode(self, input_text, subs_key, perm_key):
        input_text = input_text.upper().lstrip().rstrip()
        subs_key = subs_key.upper().lstrip().rstrip()
        perm_key = perm_key.upper().lstrip().rstrip()

        #najprv sa vytvori polybiov stvorec 5x5 s heslom ADFGX
        square = self.polybious.encode('skakal pes pres oves', subs_key)
        #dam to do tabulky
        table = self.simple.encode(square, perm_key)
        return table

    def decode(self, input_text, subs_key, perm_key):
        input_text = input_text.upper().lstrip().rstrip()
        subs_key = subs_key.upper().lstrip().rstrip()
        perm_key = perm_key.upper().lstrip().rstrip()

        table = self.simple.decode(input_text, perm_key)
        square = self.polybious.decode(table, subs_key)
        print(square)

cipher = Adfgx()
message = cipher.encode('skakal pes pres oves', 'at zije nase republika zvitezime', 'ukazka')
print(message)
text = cipher.decode(message, 'at zije nase republika zvitezime', 'ukazka')
