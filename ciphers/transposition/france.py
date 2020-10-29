from pprint import pprint
class France:
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

    def encode(self, input_text, key, diagonal_a, diagonal_b):
        input_text = input_text.upper().lstrip().rstrip()
        text = [letter for letter in input_text if letter in self.alphabet]
        key = key.upper().lstrip().rstrip()
        diagonal_a = diagonal_a.upper().lstrip().rstrip()
        diagonal_b = diagonal_b.upper().lstrip().rstrip()
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

        key = perm_key
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

        #prejdi prvu uhlopriecku
        for index, letter in enumerate(key):
            if letter == diagonal_a:
                #ziskaj pismena v diagonale
                for index_of_row, row in enumerate(table):
                    if index + index_of_row < len(row):
                        encoded_text += row[index + index_of_row]
                        table[index_of_row][index + index_of_row] = '-'

        #prejdi druhu uhlopriecku
        for index in range(len(key)-1,-1,-1):
            letter = key[index]
            if letter == diagonal_b:
                #ziskaj pismena v diagonale
                for index_of_row, row in enumerate(table):
                    if index - index_of_row >= 0 and row[index - index_of_row] != '-':
                        encoded_text += row[index - index_of_row]
                        table[index_of_row][index - index_of_row] = '-'

        #prejdi perm_key, ziskavaj stlpce
        for index in perm_key:
            minimum = min(perm_key)
            index_of_min = perm_key.index(minimum)
            perm_key[index_of_min] = 9999
            for row in table:
                if index_of_min < len(row) and row[index_of_min] != '-':
                    encoded_text += row[index_of_min]

        #rozdel po piatich
        encoded_text = [encoded_text[i:i+5] for i in range(0,len(encoded_text), 5)]
        encoded_text = ' '.join(encoded_text)

        return encoded_text
    
    def decode(self, input_text, key, diagonal_a, diagonal_b):
        input_text = input_text.upper().lstrip().rstrip()
        text = [letter for letter in input_text if letter in self.alphabet]
        key = key.upper().lstrip().rstrip()
        diagonal_a = diagonal_a.upper().lstrip().rstrip()
        diagonal_b = diagonal_b.upper().lstrip().rstrip()
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

        key = perm_key
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

        #prva diagonala
        for index, letter in enumerate(key):
            if letter == diagonal_a:
                #pridaj pismena do diagonaly
                for index_of_row, row in enumerate(table):
                    if index_of_row + index < len(row):
                        table[index_of_row][index + index_of_row] = text[0]
                        del text[0]
        
        #druha diagonala
        for index in range(len(key)-1, -1, -1):
            letter = key[index]
            if letter == diagonal_b:
                #pridaj pismena do diagonaly
                for index_of_row, row in enumerate(table):
                    if index - index_of_row >= 0 and row[index - index_of_row] == []:
                        table[index_of_row][index - index_of_row] = text[0]
                        del text[0]

        #prejdi perm_key, ziskavaj stlpce
        for index in perm_key:
            minimum = min(perm_key)
            index_of_min = perm_key.index(minimum)
            perm_key[index_of_min] = 9999
            for index, row in enumerate(table):
                if row[index_of_min] == []:
                    if index_of_min < len(row) and len(text) > 0:
                        table[index][index_of_min] = text[0]
                        del text[0]

        decoded_text = ""    
        for row in table:
            for letter in row:
                if letter in self.alphabet:
                    decoded_text += letter 

        return decoded_text

cipher = France()
text = 'laska temer nahrazuje mysleni laska je horouci zapomenuti na vsechno ostatni a potom zadejte aby vasen byla logicka'
message = cipher.encode(text, 'eiffelova vez', 'e', 'v')
print(message)
text = cipher.decode(message, 'eiffelova vez', 'e', 'v')
print(text)