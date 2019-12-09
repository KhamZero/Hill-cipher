def is_encryptor():
    question = ('Если хотите зашифровать текст, введите "enc". Расшифрвать - "dec": ')
    answer = input(question)
    if answer == "enc":
        return 1
    elif answer == "dec":
        return 0
    else:
        print("Вы допустили ошибку!")
        exit()

def give_alphabet():
    alphabet = dict()
    j = 0
    for i in range(65, 91):
        alphabet[i] = j
        j += 1
    return alphabet

def give_key():
    key = str()
    while len(key) != 9:
        key = input("Напишите ключ из 9 символов: ")
        key = key.upper()
    return key

def give_matrix(key, alphabet):
    matrix = [[0 for i in range(3)] for j in range(3)]
    num = 0
    for i in range(3):
        num += 1
        if num == 2:
            num += 1
        if num == 4:
            num -= 1
        for j in range(3):
            matrix[i][j] = alphabet[ord(key[i*num+j])]     
    return matrix

def draw_matrix(matrix, num=0):
    subject = "сообщения"
    if num == 1:
        subject = "ключа"
    if num == 2:
        subject = "зашифрованного сообщения"
    print("\nМатрица {}:\n".format(subject))
    for i in matrix:
        print('|', end = ' ')
        for j in i:
            print('{:2}'.format(j), end = ' ')
        print('|')

def is_determinant_zero(matrix):
    det_1 = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix [1][2] * matrix[2][0]
    det_1 += matrix[1][0] * matrix[2][1] * matrix[0][2]

    det_2 = matrix[0][2] * matrix[1][1] * matrix[2][0] + matrix[0][1] * matrix[1][0] * matrix[2][2]
    det_2 += matrix[0][0] * matrix[1][2] * matrix[2][1]
    print("\nDeterminant -", det_1 - det_2)
    if det_1 - det_2 == 0:
        return True

def give_text():
    text = input("\nНапишите текст, который нужно закодировать: ")
    text = text.upper()
    return text

def give_for_crypt_matrix(text, alphabet):
    matrix = list()
    for i in text:
        matrix.append([alphabet[ord(i)]])
    return matrix

def encryptor(matrix_1, matrix_2):
    def compositor(matrix_1, matrix_2):
        composition = [[0], [0], [0]]
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2)):
                composition[i][0] += matrix_1[i][j] * matrix_2[j][0]
        return composition

    def moder(composition):
        for i in range(len(composition)):
            composition[i][0] %= 26
        return composition

    composition = compositor(matrix_1, matrix_2)
    mod_composition = moder(composition)
    return mod_composition

def decryptor(matrix_1, matrix_2):
# I'm not shure I need this function \/
#   def give_identity_matrix(matrix_1):
#       identity_matrix = [[0 for i in range(len(matrix_1[j]))]for j in range(len(matrix_1))]x  
#       for i in range(len(matrix_1)):
#           identity_matrix[i][i] = 1
#       return identity_matrix

    def give_inverse_matrix(matrix_1, indentity_matrix):
        def give_matrix_minors(matrix_1):
            minor_det = [[0 for i in range(len(matrix_1[j])-1)]for j in range(len(matrix_1)-1))]
            matrix_minor = [[0 for i in range(len(matrix_1[j]))]for j in range(matrix_1)]
            for i in len(matrix_1):
                for j in len(matrix_1[i]):

            pass
        pass
#   identity_matrix = give_identity_matrix(matrix_1)
    inverse_matrix = give_inverse_matrix(matrix_1, identity_matrix)


    pass

def give_crypto_text(matrix, alphabet):
    crypto_text = str()
    symbol = str()
    for i in range(len(matrix)):
        for j in range(65, 91):
            if matrix[i][0] == alphabet[j]:
                symbol = j
                break
        crypto_text += chr(symbol)
    return crypto_text

def draw_lines():
    return ('________________________________________________')

def main():
    encrypt_value = is_encryptor()
    alphabet = give_alphabet()
    key = give_key()
    matrix = give_matrix(key, alphabet)
    draw_matrix(matrix, 1)

    if is_determinant_zero(matrix):
        print("Детерминант матрицы ключа выдает ноль! Выберите другой ключ")
        main()
        exit()
    print(draw_lines())

    crypto_text = give_text()
    for_crypt_matrix = give_for_crypt_matrix(crypto_text, alphabet)
    draw_matrix(for_crypt_matrix)
    print(draw_lines())
    if encrypt_value:
        crypto_matrix = encryptor(matrix, for_crypt_matrix)
    else:
        crypto_matrix = decryptor(matrix, for_crypt_matrix)
    draw_matrix(crypto_matrix, 2)
    crypto_text = give_crypto_text(crypto_matrix, alphabet)

    print('\n', crypto_text)




main()
input()