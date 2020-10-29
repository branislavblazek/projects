from pprint import pprint
import random

class Ubchi:
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
        pocet_klamacov = len(key.split(' '))
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

        #prva transpozicia je done

        second_table = []

        #druha transpozicia
        iterator_in_loop = 0
        second_row = []
        perm_copy = perm_key.copy()
        for index in perm_copy:
            minimum = min(perm_copy)
            index_of_min = perm_copy.index(minimum)
            perm_copy[index_of_min] = 9999

            for row in table:
                if index_of_min < len(row):
                    second_row.append(row[index_of_min])
                    iterator_in_loop += 1
                    if iterator_in_loop % len(perm_copy) == 0:
                        second_table.append(second_row)
                        second_row = []
        
        
        if second_row != []:
            second_table.append(second_row)
            
        for _ in range(pocet_klamacov):
            nahodny_znak = random.choice(self.alphabet)
            if len(second_table[-1]) == len(perm_key):
                second_table.append(nahodny_znak)
            else:
                second_table[-1].append(nahodny_znak)

        encoded_text = ""
        #ziskaj text
        for index in perm_key:
            minimum = min(perm_key)
            index_of_min = perm_key.index(minimum)
            perm_key[index_of_min] = 9999
            for row in second_table:
                if index_of_min < len(row):
                    encoded_text += row[index_of_min]

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

        second_text = text.copy()

        for item in pocet_row.items():
            value = item[1]
            columns.append(text[:value])
            del text[:value]

        #prejdi perm_key, ziskavaj stlpce
        perm_copy = perm_key.copy()
        for index in perm_copy:
            minimum = min(perm_copy)
            index_of_min = perm_copy.index(minimum)
            perm_copy[index_of_min] = 9999
            for index, letter_to_row in enumerate(columns[minimum]):
                table[index][index_of_min] = letter_to_row

        #najdi druhy
        pocet_row = {}
        for index in range(len(perm_key)):
            dlzka = len(second_text) // len(perm_key)
            if index < len(second_text) % len(perm_key):
                dlzka += 1
            pocet_row[perm_key[index]] = dlzka
        pocet_row = {k: v for k, v in sorted(pocet_row.items(), key=lambda item: item[0])}
        
        if [] in table[-1]:
            del table[-1][table[-1].index([]):]
            #treba odstranit n-klamacov, nie 2
            del table[-1][-2:]

        medzitext = [letter for row in table for letter in row if letter != []]

        pocet_row = {}
        for index in range(len(perm_key)):
            dlzka = len(medzitext) // len(perm_key)
            if index < len(medzitext) % len(perm_key):
                dlzka += 1
            pocet_row[perm_key[index]] = dlzka

        perm_copy = perm_key.copy()

        columns = {}

        for index in perm_copy:
            minimum = min(perm_copy)
            index_of_min = perm_copy.index(minimum)
            perm_copy[index_of_min] = 9999
            value = pocet_row[minimum]
            columns[minimum] = medzitext[:value]
            del medzitext[:value]

        decoded_text = ""

        #prejdi perm_key, ziskavaj stlpce
        for index in perm_key:
            minimum = min(perm_key)
            index_of_min = perm_key.index(minimum)
            perm_key[index_of_min] = 9999
            for index, letter_to_row in enumerate(columns[minimum]):
                table[index][index_of_min] = letter_to_row
        
        for row in table:
            for letter in row:
                decoded_text += letter

        return decoded_text

cipher = Ubchi()
message = cipher.encode('kdyz mi neco vysvetlis zapomenu to kdyz to ale sam udelam pochopim to', 'ctenar roka')
print(message)
text = cipher.decode(message, 'ctenar roka')
print(text)