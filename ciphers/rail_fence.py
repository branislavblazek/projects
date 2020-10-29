class Rail_fence:
    def __init__(self, key=3):
        self.key = key

    def create_table(self, text):
        text = text.lower().replace(' ', '')
        table = []
        index = 0
        direction = 1

        for letter in text:
            column = []
            for dot in range(self.key):
                if dot == index:
                    column.append(letter)
                else:
                    column.append('.')
            
            if direction == 1:
                index += 1
            elif direction == 0:
                index -= 1
            
            if index >= self.key and direction == 1:
                direction = 0
                index -= 2
            elif index < 0 and direction == 0:
                direction = 1
                index += 2

            table.append(column)
        
        text = []
        for line in range(self.key):
            text.append([])

        for line in table:
            for index, char in enumerate(line):
                if char != '.':
                    text[index].append(char)

        table_text = []

        for li in text:
            table_text += li

        return "".join(table_text)

cipher = Rail_fence()
message = cipher.create_table('defend')
print(message)