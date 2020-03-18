class Frequency:
    def __init__(self, input_text):
        self.alphabet = [chr(i+97) for i in range(26)]
        self.slovnik = dict()
        self.spolu = 0
        self.input_text = ""
        self.table = dict()

        for letter in self.alphabet:
            self.slovnik[letter] = 0
            self.table[letter] = ""

        self.input_text = input_text.lower().lstrip().rstrip()

        for letter in self.input_text:
            if letter in self.alphabet:
                self.slovnik[letter] += 1
                self.spolu += 1

        percento = self.spolu / 100
        self.per_slovnik = dict()

        for letter, value in self.slovnik.items():
            hodnota = value / percento
            self.per_slovnik[letter] = round(hodnota, 2)

    @property
    def value(self):
        print('Values of letters in text in numbers:')
        return self.slovnik

    @property
    def percentage(self):
        print('Values of letters in text in percetanges:')
        return self.per_slovnik

    @property
    def crypto_table(self):
        return self.table

    @property
    def key(self):
        key = ''.join([item[1] for item in self.table.items()])
        return key

    @property
    def max(self):
        print('First 6 letters found in text with highest repeating:')
        x = sorted(self.per_slovnik.items(), key=lambda item: item[1], reverse=True)
        return x[:6]

    @property
    def text(self):
        return self.input_text

    def replace(self, values):
        what_replace, with_replace = values[0], values[1]
        what_replace = what_replace.lower()
        with_replace = with_replace.upper()

        print('Replacing ' + what_replace + ' with ' + with_replace)
        
        if self.crypto_table[with_replace.lower()] != '':
            print('For this letter is set another letter!')
            return

        self.crypto_table[with_replace.lower()] = what_replace
        self.input_text = self.input_text.replace(what_replace, with_replace)

analysis = Frequency("""ysnaf jwddq (1926 af ushw lgof, kgmlz sxjaus – 10 bsfmsjq 1999 af zwjesfmk, kgmlz sxjaus) osk s kgmlz sxjausf tmkafwkkesf sfv xgjewj uzsajesf gx sfydg sewjausf. zak yjsfvxslzwj osk kaj osdlwj klsfxgjv, ozg sjymwv kljgfydq tml mfkmuuwkkxmddq xgj wfxjsfuzakwewfl xgj fslanw hwghdwk jwysjvdwkk gx jsuw gj ugdgmj sl lzw fslagfsd ugfnwflagf gx 1909, ozauz dwv lg lzw mfagf gx kgmlz sxjaus.[1]
jwddq osk wvmuslwv sl vaguwksf ugddwyw sfv ljafalq ugddwyw, gpxgjv 
twxgjw kwjnafy af alsdq vmjafy lzw kwugfv ogjdv osj. zw twusew lzw 
hjanslw kwujwlsjq gx zsjjq ghhwfzwaewj af 1949.
zw twusew uzsajesf gx sfydg sewjausf af 1982. zw dwv s yjgmh gx kgmlz sxjausf tmkafwkkewf ozg ewl oalz lzw tsffwv sxjausf fslagfsd ugfyjwkk af rsetas af 1985. zw osk kmuuwwvwv tq bmdasf gyadnaw lzgehkgf af 1990.""")
print(analysis.max)

replace = [('w', 'e'), ('l', 't'), ('z', 'h'), ('s', 'a'), ('a', 'i'), ('f', 'n'),
('d', 'l'), ('q', 'y'), ('v', 'd'), ('k', 's'), ('o', 'w'), ('j', 'r'), ('y', 'g'),
('x', 'f'), ('g', 'o'), ('m', 'u'), ('u', 'c'), ('b', 'j'), ('t', 'b'), ('e', 'm'),
('p', 'x'), ('n', 'v'), ('h', 'p'), ('c', 'k')
]

for coom in replace:
    analysis.replace(coom)

print(analysis.text)
print(analysis.table)
print(analysis.key)