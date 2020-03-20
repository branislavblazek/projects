class Simple:
    def __init__(self):
        self.alphabet = [chr(i+97) for i in range(26)]

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
        input_text = input_text.lower().lstrip().rstrip()
        text = [letter for letter in input_text if letter in self.alphabet]
        key = key.lower().lstrip().rstrip()
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

cipher = Simple()
text = 'kdyz se na svete objevi opravdovy genius poznate ho podle toho ze se proti nemu spiknou vsichni hlupaci'
message = cipher.encode(text, 'neprecte toooo')
print(message)