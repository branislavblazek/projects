import sys

def cipher_file():
    print(sys.argv[1:])
    #1. - input file
    #2. - output file
    #3. - mode = en(encode) or de(decode)
    #3. - type of cipher
    #n. - keys
    if len(sys.argv[1:]) < 4:
        print('There isnt a required length of arguments!')
        return False

    #handle input file
    try:
        input_file = open(sys.argv[1], mode='r', encoding='utf8')
    except FileNotFoundError:
        print('Cannot find a file for input!')
        return False

    riadky = [riadok.strip() for riadok in input_file]
    input_file.close()

    #handle output file
    try:
        output_file = open(sys.argv[2], mode='w+', encoding='utf8')
    except FileNotFoundError:
        print('Cannot file a file for output!')
        return False

    for riadok in riadky:
        output_file.write(riadok + '\n')
    
    output_file.close()

cipher_file()