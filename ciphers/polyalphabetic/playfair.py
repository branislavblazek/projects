class Playfair:
    def __init__(self):
        self.alphabet = [chr(i+97) for i in range(26)]
        self.alphabet.remove('q')

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
        table = [[],[],[],[], []]

        self.can_use = key + self.intersection(key, self.alphabet)

        for index in range(25):
            row = index // 5
            table[row].append(self.can_use[index])

        return table

    def encode(self, input_text, key, type=1):
        input_text = input_text.lower().lstrip().rstrip()
        text = ""
        #just allowed letter, rpl special not very used letter with smth else
        for letter in input_text:
            if letter in self.alphabet:
                text += letter
            elif letter == 'q':
                text += 'k'
        #if len is not odd, add z to end
        if len(text) % 2 != 0:
            text += 'x'

        key = key.lower().lstrip().rstrip()
        #create table
        table = self.create_square(key)
        #create bigram
        bigrams = []
        for i in range(0,len(text),2):
            pair = text[i:i+2]
            #same pairs split with x and z
            if pair[0] == pair[1]:
                add = pair[0] + 'x'
                bigrams.append(add)
                pair = pair[1] + 'z'

            bigrams.append(pair)

        encoded_text = ""

        for pair in bigrams:
            #find thier position in table
            p1 = pair[0]
            r1 = None
            c1 = None
            new_p1 = None
            p2 = pair[1]
            r2 = None
            c2 = None
            new_p2 = None
            for row in range(len(table)):
                for column in range(len(table[row])):
                    #check for first 
                    if table[row][column] == p1:
                        r1 = row
                        c1 = column
                    if table[row][column] == p2:
                        r2 = row
                        c2 = column
            #1) if they are in same row add 1 to their column
            if r1 == r2:
                next_c1 = (c1 + type) if c1 + type < 5 else 0
                next_c2 = (c2 + type) if c2 + type < 5 else 0
                new_p1 = table[r1][next_c1]
                new_p2 = table[r2][next_c2]
            #2) if they are in same column, add 1 to thier row
            elif c1 == c2:
                next_r1 = (r1 + type) if r1 + type < 5 else 0
                next_r2 = (r2 + type) if r2 + type < 5 else 0
                new_p1 = table[next_r1][c1]
                new_p2 = table[next_r2][c2]
            #3) take row of first pair item, take column of second pair item and find in table
            else:
                new_p1 = table[r1][c2]
                new_p2 = table[r2][c1]
            encoded_text += new_p1 + new_p2

        if len(encoded_text) % 5 != 0:
            encoded_text += 'x' * (5 - (len(encoded_text) % 5))

        encoded_text = [encoded_text[i:i+5] for i in range(0,len(encoded_text), 5)]
        encoded_text = ' '.join(encoded_text)

        return encoded_text

    def decode(self, input_text, key):
        if len(input_text) % 5 == 0:
            if input_text[-4:] == "xxxx":
                input_text = input_text[:-4]
            elif input_text[-3:] == "xxx":
                input_text = input_text[:-3]
            elif input_text[-2:] == "xx":
                input_text = input_text[:-2]
            elif input_text[-1:] == "x":
                input_text = input_text[:-1]
        decoded_text = self.encode(input_text, key, -1).replace(' ', '')
        if len(decoded_text) % 5 == 0:
            if decoded_text[-4:] == "xxxx":
                decoded_text = decoded_text[:-4]
            elif decoded_text[-3:] == "xxx":
                decoded_text = decoded_text[:-3]
            elif decoded_text[-2:] == "xx":
                decoded_text = decoded_text[:-2]
            elif decoded_text[-1:] == "x":
                decoded_text = decoded_text[:-1]
        
        return decoded_text

cipher = Playfair()
message = cipher.encode('tato sifra je docela jednoducha', 'heslo')
print(message)
text = cipher.decode(message, 'heslo')
print(text)

print(cipher.decode('nb ex cr nk xl ef xl ae bn eo vi fj', 'korona'))